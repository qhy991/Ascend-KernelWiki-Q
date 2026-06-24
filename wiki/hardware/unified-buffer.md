---
id: wiki-hardware-unified-buffer
title: "Unified Buffer (UB) — On-Chip Scratchpad Memory"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [unified-buffer, memory, hardware]
confidence: verified
hardware_features: [unified-buffer]
related: [wiki-hardware-cube-unit, wiki-hardware-vector-unit, wiki-hardware-memory-hierarchy]
sources: [doc-ascend-memory-hierarchy, doc-cann-architecture-guide]
cuda_equivalent: shared_memory
---

# Unified Buffer (UB) — On-Chip Scratchpad Memory

The Unified Buffer (UB) is Ascend's on-chip scratchpad memory, serving as the primary workspace for Vector and Cube operations. It's analogous to CUDA's shared memory but with several architectural distinctions.

## Physical Characteristics

**Size**: ~1-2 MB per AICore (varies by chip generation)
- **Ascend 910**: Larger UB for high-bandwidth workloads
- **Ascend 910B**: Optimized bank structure for improved throughput
- **Ascend 310P**: Smaller UB (edge inference chip)

**Bandwidth**: Significantly higher than HBM/DDR
- Typical bandwidth: 2-4 TB/s per AICore
- Latency: ~10-20 cycles (vs. 100+ cycles to global memory)

## Role in Memory Hierarchy

UB sits at the center of Ascend's memory hierarchy:

```
Global Memory (HBM/DDR) ←→ Unified Buffer ←→ L0 Buffer (Cube/Vector)
```

**Primary Functions**:
1. **Compute Workspace**: Holds operands for Vector and Cube operations
2. **Data Staging**: Temporary storage for data being processed
3. **Reuse Buffer**: Enables data reuse across multiple operations
4. **Transfer Hub**: Intermediary between GM and L0 buffers

## Data Movement APIs

**GM ↔ UB** (via MTE - Memory Transfer Engine):
```cpp
// Basic data copy
DataCopy(src_gm, dst_ub, size);

// With padding for alignment
DataCopyPad(src_gm, dst_ub, {pad_size});
```

**UB ↔ L0** (for Cube operands):
- Automatic during Matmul calls
- Explicit for Vector operations

## Memory Allocation

**AscendC Memory Management**:
```cpp
// Create buffer queue (TPipe)
TPipe pipe;

// Allocate Unified Buffer
TBuf ub_queue;
pipe.InitBuffer(ub_queue, {num_buffers, size_bytes});
```

**Allocation Strategy**:
- Static allocation recommended for performance
- Double buffering for compute/transfer overlap
- Bank-aware allocation to avoid conflicts

## Bank Structure and Conflicts

UB is organized into multiple banks for parallel access:
- **Bank Count**: Typically 32-64 banks
- **Conflict**: Simultaneous accesses to same bank cause serialization
- **Mitigation**: Pad data or use non-strided access patterns

## Double Buffering Pattern

Critical for performance optimization:

```cpp
// Allocate two buffers
TBuf ub_current, ub_next;

// While processing current buffer
ProcessData(ub_current);

// Transfer next buffer asynchronously
DataCopy(gm_next, ub_next, size);

// Swap and repeat
```

**Benefits**:
- Hides memory latency
- Achieves near 100% compute utilization
- Enables pipeline depth

## Comparison with CUDA Shared Memory

| Aspect | Ascend UB | CUDA Shared Memory |
|--------|-----------|-------------------|
| Size | 1-2 MB per AICore | 48-228 KB per SM |
| Scope | Per-AICore | Per-SM (warp-synchronous) |
| Programming | Explicit API (DataCopy) | __shared__ declaration |
| Synchronization | Event-based | __syncthreads() |
| Access Pattern | MTE-managed | Load/store instructions |

UB's larger size enables bigger tiles and more reuse opportunities, but requires explicit data movement management.

## Best Practices

1. **Maximize Reuse**: Keep frequently accessed data in UB across multiple operations
2. **Tile Computation**: Partition workloads to fit in UB and minimize GM access
3. **Bank Conflicts**: Analyze access patterns and pad data to avoid bank serialization
4. **Overlap Transfers**: Use double buffering to hide memory latency
5. **Align Allocations**: Align buffer sizes to bank boundaries for optimal throughput
