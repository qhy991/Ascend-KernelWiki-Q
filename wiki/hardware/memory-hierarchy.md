---
id: wiki-hardware-memory-hierarchy
title: "Ascend Memory Hierarchy (GM → L1 → UB → L0)"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [memory, hierarchy, global-memory, unified-buffer, hardware]
confidence: verified
hardware_features: [global-memory, l1-buffer, unified-buffer, l0-buffer, mte]
related: [hw-unified-buffer, hw-instruction-queue]
sources: [doc-ascend-memory-hierarchy, doc-cann-architecture-guide]
cuda_equivalent: null
---

# Ascend Memory Hierarchy

Ascend chips employ a 4-level memory hierarchy designed to balance capacity, bandwidth, and latency for deep learning workloads. Understanding this hierarchy is critical for kernel optimization.

## Hierarchy Overview

```
┌─────────────────────────────────────────────────────────┐
│ Level 0: L0 Buffer (Registers)                          │
│ Size: ~64 KB per AICore | Latency: ~1 cycle            │
│ Usage: Cube/Vector operands, accumulation               │
└─────────────────────────────────────────────────────────┘
                          ↑↓
┌─────────────────────────────────────────────────────────┐
│ Level 1: Unified Buffer (UB)                            │
│ Size: 1-2 MB per AICore | Latency: ~10-20 cycles       │
│ Usage: Compute workspace, data staging                   │
└─────────────────────────────────────────────────────────┘
                          ↑↓
┌─────────────────────────────────────────────────────────┐
│ Level 2: L1 Buffer (Optional)                           │
│ Size: ~8-16 MB per AICore | Latency: ~50-100 cycles    │
│ Usage: Staging between GM and UB                         │
└─────────────────────────────────────────────────────────┘
                          ↑↓
┌─────────────────────────────────────────────────────────┐
│ Level 3: Global Memory (HBM/DDR)                        │
│ Size: 32-64 GB (chip) | Latency: ~100+ cycles          │
│ Usage: Main memory storage, model weights, activations  │
└─────────────────────────────────────────────────────────┘
```

## Level-by-Level Breakdown

### Level 0: L0 Buffer (Registers)
- **Size**: ~64 KB per AICore
- **Latency**: ~1 cycle
- **Bandwidth**: Highest (multi-THz/s)
- **Usage**: Holds operands for active Cube/Vector instructions
- **Management**: Implicit (allocated during instruction execution)
- **Lifetime**: Single instruction duration

### Level 1: Unified Buffer (UB)
- **Size**: 1-2 MB per AICore
- **Latency**: ~10-20 cycles
- **Bandwidth**: 2-4 TB/s per AICore
- **Usage**: Scratchpad for compute operations
- **Management**: Explicit via AscendC `TPipe`/`TBuf` APIs
- **Lifetime**: User-controlled (kernel scope)

### Level 2: L1 Buffer (Optional)
- **Size**: ~8-16 MB per AICore
- **Latency**: ~50-100 cycles
- **Bandwidth**: Intermediate between GM and UB
- **Usage**: Optional staging layer for data pre-fetching
- **Management**: Optional; often bypassed for direct GM↔UB transfers
- **Lifetime**: User-controlled if used

### Level 3: Global Memory (GM)
- **Size**: 32-64 GB per chip (HBM or DDR)
- **Latency**: ~100+ cycles
- **Bandwidth**: ~1.2-2 TB/s total (shared across all AICores)
- **Usage**: Main storage for model weights, activations, gradients
- **Management**: Explicit allocation/deallocation
- **Lifetime**: Across kernel launches

## Data Movement APIs

**GM ↔ UB** (Primary path):
```cpp
// Direct copy with MTE
DataCopy(src_gm, dst_ub, size);

// With padding for alignment
DataCopyPad(src_gm, dst_ub, {pad_size});
```

**GM → L1 → UB** (Optional staging):
```cpp
// Stage via L1
DataCopy(src_gm, dst_l1, size);
DataCopy(src_l1, dst_ub, size);
```

**UB ↔ L0** (Automatic):
- Implicit during Cube/Vector instruction execution
- No explicit API required

## Performance Characteristics

| Level | Capacity | Bandwidth | Latency | Primary Use |
|-------|----------|-----------|---------|-------------|
| L0 | ~64 KB | Highest | ~1 cycle | Instruction operands |
| UB | 1-2 MB | High | ~10-20 cycles | Compute workspace |
| L1 | 8-16 MB | Medium | ~50-100 cycles | Optional staging |
| GM | 32-64 GB | Lower | ~100+ cycles | Main storage |

## Optimization Principles

**Minimize GM Traffic**:
- Maximize data reuse in UB
- Tile computations to fit in UB
- Avoid repeated GM↔UB transfers

**Exploit Hierarchy**:
- Keep hot data in UB/L0
- Prefetch next tiles during computation
- Use L1 for intermediate staging if beneficial

**Overlap Transfers**:
- Double buffering in UB
- Asynchronous GM↔UB transfers via MTE queue
- Pipeline with compute instructions

**Bandwidth Awareness**:
- UB bandwidth >> GM bandwidth
- Design algorithms to maximize UB reuse
- Access patterns that exploit UB's bank structure

## Comparison with CUDA Memory Hierarchy

| Ascend | CUDA | Function |
|--------|------|----------|
| L0 Buffer | Registers | Instruction operands |
| Unified Buffer | Shared Memory | Compute workspace |
| L1 Buffer | L1 Cache | Staging/caching |
| Global Memory | Global Memory | Main storage |

**Key Differences**:
- UB is **larger** (1-2 MB vs. 48-228 KB)
- UB requires **explicit management** (no automatic caching)
- L1 is **optional** staging, not transparent cache
- No L2 cache equivalent (GM is main memory)

These differences make UB management more critical than shared memory management in CUDA.

## Best Practices

1. **Profile Memory Access**: Identify hot data paths and keep them in UB
2. **Tile Strategically**: Partition workloads to maximize UB reuse
3. **Use Double Buffering**: Overlap computation and data transfer
4. **Minimize GM Access**: Each GM transfer is expensive; amortize over reuse
5. **Consider L1**: For workloads with predictable access patterns, L1 staging can help
6. **Align Accesses**: Avoid bank conflicts in UB through padding and access pattern design
