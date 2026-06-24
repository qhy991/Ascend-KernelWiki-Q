---
id: technique-atomic-accumulation
title: "Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory"
type: wiki-technique
architectures: [ascend910b]
tags: [atomic-accumulation, reduce, split-k, optimization]
confidence: inferred
techniques: [atomic-accumulation]
hardware_features: [global-memory, mte, cube-unit]
kernel_types: [matmul, gemm, reduce]
related: [kernel-matmul-ascendc, technique-workspace-management, wiki-hardware-mte]
sources: [doc-ascendc-api-reference, doc-ascend-memory-hierarchy]
reproducibility: pseudocode
---

# Atomic Accumulation to Global Memory

Atomic accumulation lets multiple AICores write partial results into the *same* Global Memory (GM) location and have the hardware add them together, rather than overwrite. On Ascend 910B this is enabled by wrapping a `DataCopy` to GM between `SetAtomicAdd<T>()` and `SetAtomicNone()`, turning the store into a read-modify-write add. It is the building block for split-K GEMM and for cross-core scatter-add reductions, both of which would otherwise need a host-side or second-pass reduction.

## When It Applies

Atomic accumulation is useful whenever multiple producers contribute to one output and you want to avoid a separate reduce stage:

- **Split-K GEMM**: The K dimension is partitioned across cores; each core computes a `C_partial` over its K-slice and atom-adds into the shared `C`.
- **Cross-core reductions**: Many cores reduce different input ranges into a small shared accumulator (e.g. a global sum or histogram).
- **Scatter-add**: Indexed writes that collide, such as embedding-bag gather/sum or MoE combine, where several experts/tokens land on the same output row.

## Mechanism

The MTE store path supports an accumulate mode. Setting the atomic mode before the copy makes the subsequent GM write perform `GM[addr] += UB_value` atomically across cores instead of `GM[addr] = UB_value`. The mode is sticky, so it must be cleared afterward to avoid corrupting later plain stores.

```
Without atomic:   GM[addr]  =  partial          (last writer wins — WRONG for split-K)
With atomic-add:  GM[addr] +=  partial          (all contributions summed — correct)
```

Two rules matter:

1. The output region **must be zero-initialized** before the first contributor runs, because every core only adds.
2. The accumulator dtype should be **fp32** even when inputs are fp16, so that summing many partials does not lose precision.

## AscendC Pseudocode — Split-K GEMM

Each core owns one K-slice. It performs a local `Matmul` of its slice into a UB tile, then atom-adds that tile into the shared `C` in GM. See `kernel-matmul-ascendc` for the non-split (single-K-pass) baseline this specializes.

```cpp
// Split-K GEMM: K is partitioned across `num_k_slices` cores.
// C is pre-zeroed in GM before launch (all cores only ADD into it).
template<typename T>  // T = float for the accumulator
void SplitKGemmAtomic(GM_ADDR a, GM_ADDR b, GM_ADDR c,
                      int M, int N, int K, int k_slice_id, int num_k_slices) {
    TPipe pipe;

    // This core's K-range: [k0, k1)
    int k_per_slice = K / num_k_slices;
    int k0 = k_slice_id * k_per_slice;
    int k1 = k0 + k_per_slice;

    LocalTensor<T> partial = pipe.AllocTensor<T>();  // UB tile, M_tile x N_tile

    // 1. Compute this core's partial product over its K-slice (Cube unit).
    pipe.Matmul(/*Aslice*/ a + k0, /*Bslice*/ b + k0,
                partial, M_tile, N_tile, /*k=*/ k1 - k0);

    // 2. Accumulate the partial into the shared C with atomic-add.
    SetAtomicAdd<T>();                 // next GM store becomes read-modify-write +=
    DataCopy(c /*GM*/, partial, M_tile * N_tile);
    SetAtomicNone();                   // restore plain-store mode (sticky flag!)
}
```

After all `num_k_slices` cores finish, `C` in GM holds the full `sum over k` of the partials — no host reduction, no extra kernel launch.

## AscendC Pseudocode — Scatter-Add (Embedding-Bag / MoE Combine)

For indexed reductions, the destination address is data-dependent and rows collide. Atomic-add makes the colliding writes safe.

```cpp
// Scatter-add: out[index[i]] += value[i], where multiple i may map to the same row.
template<typename T>  // T = float
void ScatterAddAtomic(GM_ADDR out, GM_ADDR value, GM_ADDR index, int num_rows) {
    TPipe pipe;
    LocalTensor<T> row = pipe.AllocTensor<T>();

    for (int i = core_offset; i < num_rows; i += core_stride) {
        DataCopy(row, value + i * ROW_LEN, ROW_LEN);     // load contribution

        int dst = LoadIndex(index, i);                   // target output row
        SetAtomicAdd<T>();
        DataCopy(out + dst * ROW_LEN, row, ROW_LEN);     // out[dst] += row
        SetAtomicNone();
    }
}
```

## Cost and Contention

Atomic-add is a read-modify-write at the GM/memory-controller level. When many cores target the *same* address, those updates serialize, so throughput on contended addresses is bounded by the atomic path rather than by raw bandwidth.

- **Best case** — wide, well-spread outputs (large `C`, sparse index collisions): contention is low and the atomic path is nearly free relative to the store it replaces.
- **Worst case** — a small accumulator (e.g. a single global scalar) hammered by every core: updates effectively serialize and the technique can be slower than a structured tree reduction.

Mitigations: keep the contended footprint large, reduce the number of contributors per address (e.g. partial local reduction before the atomic store), or fall back to the workspace approach below.

## Dtype Support

| Accumulate dtype | Use case | Notes |
| --- | --- | --- |
| fp32 | Preferred for split-K and reductions | Avoids precision loss when summing many partials; recommended accumulator type |
| fp16 | Bandwidth-sensitive, few contributors | Higher rounding error as the number of accumulated terms grows |

Even when A/B operands are fp16, accumulate in fp32 and only downcast the final `C` once all atomic-adds complete.

## Alternative: Workspace + Separate Reduce Kernel

Instead of atom-adding into a shared output, each core can write its `C_partial` to a *distinct* slot in a scratch GM workspace, followed by a second kernel that reduces across slots. This is the `technique-workspace-management` pattern.

| Aspect | Atomic-add to GM | Workspace + reduce pass |
| --- | --- | --- |
| Extra GM memory | None (writes into final output) | `num_slices x` output size of scratch |
| Kernel launches | One | Two (compute, then reduce) |
| Behavior under contention | Serializes on hot addresses | No atomic contention; deterministic |
| Pre-zeroing | Output must be zeroed first | Not required (reduce overwrites) |
| Best when | Outputs wide / collisions rare | Heavy contention or many K-slices |

The choice is a contention-vs-memory trade-off: atomic-add saves a workspace and a pass but pays serialization on hot addresses; the workspace path spends memory and a launch to get contention-free, deterministic reduction.

## Pitfalls and Notes

1. **Zero the output first.** Every contributor only adds; a non-zeroed `C` yields garbage. The workspace alternative does not need this.
2. **Always pair `SetAtomicAdd<T>()` with `SetAtomicNone()`.** The mode is sticky — a missing reset turns the *next* unrelated GM store into an accidental accumulate.
3. **Accumulate in fp32.** fp16 accumulation drifts as the term count grows; prefer fp32 and downcast once at the end.
4. **Floating-point sums are non-associative.** Atomic-add order across cores is non-deterministic, so results can differ run-to-run in the last bits. Use the workspace + reduce path when bit-exact reproducibility is required.
5. **Watch the contended footprint.** A small shared accumulator serializes; widen the output or pre-reduce locally before the atomic store.

> Confidence: **inferred**. The `SetAtomicAdd` / `SetAtomicNone` API contract and fp32-accumulate guidance follow the AscendC API reference (`doc-ascendc-api-reference`) and the GM/MTE store model (`doc-ascend-memory-hierarchy`); the split-K and scatter-add kernel structures here are illustrative pseudocode, not measured implementations.
