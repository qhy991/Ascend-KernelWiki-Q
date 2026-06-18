---
id: hw-mte
title: "MTE — Memory Transfer Engine (Async Data Movement)"
type: wiki-hardware
architectures: [ascend910, ascend910b, ascend310p]
tags: [mte, memory, dma, hardware]
confidence: source-reported
hardware_features: [mte, unified-buffer, l1-buffer, global-memory]
cuda_equivalent: tma
related: [hw-unified-buffer, hw-memory-hierarchy, technique-double-buffering]
sources: [doc-ascend-memory-hierarchy, doc-ascendc-api-reference, blog-ascend-910b-deep-dive]
---

# MTE — Memory Transfer Engine (Async Data Movement)

The Memory Transfer Engine (MTE) is the DaVinci architecture's family of DMA units that move data across the on-chip memory hierarchy — Global Memory, L1 Buffer, Unified Buffer, and L0 — **asynchronously**, so the Cube and Vector pipelines never have to wait on a load or store. Because MTE runs on its own instruction queue, transfers for the *next* tile overlap with compute on the *current* tile, which is the foundation of double buffering on Ascend. The closest NVIDIA analog is the Tensor Memory Accelerator (TMA).

## Role in the Hierarchy

MTE is the data-movement counterpart to the compute units described in [hw-memory-hierarchy](memory-hierarchy.md). Where Cube and Vector consume operands, MTE is responsible for *staging* those operands into fast on-chip memory and *evicting* results back out:

```
Global Memory (HBM/DDR)
        ↑↓   MTE2 (load)        MTE3 (store)
   L1 Buffer
        ↑↓   MTE1 (L1 → L0/UB)
Unified Buffer / L0 Buffer  →  Cube / Vector
```

Compute units operate only on data already resident in UB/L0. MTE is the only mechanism that brings data *in* from GM and writes results *out*, so for any non-trivial kernel MTE traffic is on the critical path and overlapping it with compute is the primary optimization lever.

## MTE Stages

The DaVinci core exposes several MTE pipes, each responsible for a different leg of the hierarchy. These roughly map as follows:

### MTE2 — GM → L1 / UB (load)
- Reads from Global Memory into L1 Buffer or directly into the Unified Buffer.
- The widest, highest-latency hop; subject to HBM/DDR bandwidth limits.
- Issued by `DataCopy` / `DataCopyPad` for the GM-side source.

### MTE1 — L1 → L0 / UB (stage)
- Moves data already on-chip from the L1 Buffer down into L0 (Cube operands) or UB.
- Lower latency than MTE2; used when a kernel stages through L1 before compute.
- Often implicit when the matmul flow uses L1 as an intermediate, as in [kernel-matmul-ascendc](../kernels/matmul-ascendc.md).

### MTE3 — UB → GM (store)
- Writes computed results from the Unified Buffer back to Global Memory.
- Issued by `DataCopy` / `DataCopyPad` for the GM-side destination.
- Overlapping MTE3 of the previous output tile with compute of the current tile keeps the store off the critical path.

> The exact stage numbering and which buffer a copy targets are inferred from the source/destination operands you pass to the AscendC `DataCopy` family; the framework selects the appropriate MTE pipe.

## Independent Instruction Queue

MTE has its **own hardware instruction queue**, separate from the Scalar, Vector, and Cube queues described in [hw-instruction-queue](instruction-queue.md). This is what makes asynchronous overlap possible: a `DataCopy` issued on the MTE queue returns control immediately, and the Cube/Vector queues continue executing in parallel.

```
MTE Queue:    DataCopy(tile N+1) ───────────► DataCopy(tile N+2) ──►
Cube Queue:          Matmul(tile N) ──────────► Matmul(tile N+1) ──►
Vector Queue:               Add(tile N-1) ────► Add(tile N) ───────►
```

Correctness across queues is enforced with event-based synchronization (`SetFlag` / `WaitFlag`, `PipeBarrier`, `SyncEvent`) — you wait on an MTE flag only at the point where compute actually needs the loaded data, not before. Over-synchronizing serializes the queues and destroys the overlap.

## Format-Aware Moves (ND ↔ NZ)

MTE is not a dumb byte copier — it honors the FRACTAL_NZ tiling that the Cube unit requires. A tensor stored in row-major **ND** in Global Memory can be moved into the **NZ** (zN/nZ fractal) layout expected on-chip, with the engine handling the fractal reordering during the transfer rather than requiring a separate transpose kernel. This means:

- Operands destined for the Cube unit arrive already in the fractal layout it needs.
- ND ↔ NZ conversion piggybacks on a transfer that has to happen anyway, avoiding an extra GM round-trip.
- Elementwise/Vector data that stays in ND can be moved without conversion.

## Alignment, Burst, and Stride

MTE achieves peak bandwidth only when transfers are aligned and contiguous. Practical constraints reported for the DaVinci DMA path:

- **32-byte alignment** for the base address of UB-side operands.
- **512-byte alignment** is preferred for the GM-side burst to fully utilize the memory interface.
- **Strided / non-contiguous** access (e.g. a column slice of an ND tensor) reduces effective bandwidth because it breaks the burst into smaller bursts.
- `DataCopyPad` exists precisely to handle the un-aligned tail of a tile: it pads the copy to a legal width so the engine can issue a clean burst, instead of forcing the kernel author to over-read.

| Concern | Aligned / contiguous | Misaligned / strided |
|---------|----------------------|----------------------|
| Burst size | Full 512B bursts | Fragmented small bursts |
| Effective BW | Near peak | Degraded |
| API choice | `DataCopy` | `DataCopyPad` (pads the tail) |

## Role in Double Buffering

MTE's asynchrony is what makes [technique-double-buffering](../techniques/double-buffering.md) work. With two UB buffers, the kernel loads tile *N+1* on the MTE queue while the Cube/Vector queues consume tile *N*, then swaps. The MTE transfer latency is hidden entirely behind compute, pushing the AICore toward full utilization.

```cpp
// AscendC: ping-pong load via MTE, overlapping with compute
TPipe pipe;
TQue<QuePosition::VECIN, 2> inQueue;   // depth 2 => double buffer
TQue<QuePosition::VECOUT, 2> outQueue;
pipe.InitBuffer(inQueue, 2, tileBytes);
pipe.InitBuffer(outQueue, 2, tileBytes);

for (int32_t i = 0; i < tileCount; ++i) {
    // MTE2: GM -> UB. Async; the queue's depth-2 backing gives ping-pong.
    LocalTensor<half> inLocal = inQueue.AllocTensor<half>();
    DataCopy(inLocal, srcGlobal[i * tileLen], tileLen);
    inQueue.EnQue(inLocal);

    // Compute consumes the previously-loaded tile (Vector queue).
    LocalTensor<half> x = inQueue.DeQue<half>();
    LocalTensor<half> y = outQueue.AllocTensor<half>();
    Add(y, x, x, tileLen);
    inQueue.FreeTensor(x);
    outQueue.EnQue(y);

    // MTE3: UB -> GM. Async store of the result tile.
    LocalTensor<half> z = outQueue.DeQue<half>();
    DataCopy(dstGlobal[i * tileLen], z, tileLen);
    outQueue.FreeTensor(z);
}
```

`InitBuffer(..., 2, ...)` requests a depth-2 queue, so the framework allocates two physical UB slots and inserts the `SetFlag`/`WaitFlag` events between the MTE and compute queues automatically — the load of iteration *i+1* overlaps the compute of iteration *i*. For an unaligned trailing tile, swap the `DataCopy` for `DataCopyPad` with a `DataCopyExtParams` describing the real width.

## Comparison with NVIDIA TMA

| Aspect | Ascend MTE | NVIDIA TMA |
|--------|------------|------------|
| Role | Async GM ↔ L1 ↔ UB/L0 DMA | Async GMEM ↔ SMEM DMA |
| Async unit | Dedicated MTE instruction queue | Dedicated copy engine (Hopper+) |
| Layout awareness | ND ↔ NZ fractal during transfer | Multi-dim tiled / swizzled descriptors |
| Sync | `SetFlag`/`WaitFlag`, `PipeBarrier` | `mbarrier` / `cp.async` completion |
| Issuing API | `DataCopy` / `DataCopyPad` | `cuda::memcpy_async` / `cp.async.bulk` |
| Overlap idiom | Double buffering via depth-2 `TQue` | Software pipelining via `pipeline` |

The conceptual contract is the same: a descriptor-driven, hardware-managed bulk copy that decouples data movement from compute. The main DaVinci-specific twist is built-in fractal (NZ) reformatting, where TMA leans on tile/swizzle descriptors that the programmer configures.

## Trade-offs, Pitfalls, and Notes

- **Over-synchronizing kills overlap.** A `WaitFlag` or `PipeBarrier` placed too early forces the compute queue to stall on MTE. Wait only where data is genuinely consumed.
- **Misalignment is a silent slowdown, not an error.** A strided or unaligned `DataCopy` still produces correct results but issues fragmented bursts. Use `DataCopyPad` for ragged tails and align UB allocations to 32B.
- **MTE bandwidth is shared.** GM bandwidth (MTE2/MTE3) is shared across all AICores, so a kernel that is MTE2-bound will not speed up by adding compute — reduce GM traffic via tiling and reuse in the UB ([hw-unified-buffer](unified-buffer.md)).
- **Format conversion isn't free of constraints.** ND ↔ NZ moves require the tile dimensions to be compatible with the 16×16 fractal; pad to the fractal boundary when they are not.
- **L1 staging is optional.** MTE1 only matters if the kernel routes through L1; many elementwise kernels go GM↔UB directly (MTE2/MTE3 only) and skip MTE1 entirely.

## Best Practices

1. **Prefetch one tile ahead.** Issue the next MTE2 load before consuming the current tile so the transfer hides behind compute.
2. **Use depth-2+ `TQue`.** Let the framework manage the ping-pong buffers and inter-queue flags rather than hand-rolling events.
3. **Align and batch.** Keep UB operands 32B-aligned and prefer large contiguous bursts over many small strided copies.
4. **Convert formats during transfer.** Fold ND→NZ into the load so Cube operands arrive ready, avoiding a separate transpose pass.
5. **Profile MTE occupancy.** If the MTE queue is the bottleneck, the kernel is memory-bound — attack GM traffic, not the compute kernels.
