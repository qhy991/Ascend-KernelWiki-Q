---
id: technique-bank-conflict-avoidance
title: "UB Bank Conflict Avoidance"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [bank-conflict, unified-buffer, optimization]
confidence: inferred
techniques: [bank-conflict-avoidance]
hardware_features: [unified-buffer]
kernel_types: [gemm, attention, softmax]
related: [wiki-hardware-unified-buffer, technique-data-reuse]
sources: [blog-cann-training-camp, doc-ascend-memory-hierarchy]
reproducibility: concept
---

# UB Bank Conflict Avoidance

The Unified Buffer (UB) is organized into multiple banks to enable parallel access. However, concurrent Vector and Cube unit operations targeting the same bank can cause serialization stalls, significantly degrading performance.

## Bank Organization

Ascend UB architecture uses bank-based memory organization where:
- Multiple banks operate in parallel for independent addresses
- Same-bank accesses from different units must serialize
- Bank conflicts are particularly impactful in pipelined operations

## Conflict Detection

Bank conflicts typically manifest as:
- Unexplained pipeline stalls during UB reads/writes
- Performance degradation at specific tile dimensions
- Timing variations correlated with access pattern changes

## Avoidance Strategies

### 1. Dimension Padding
Pad tile dimensions to avoid bank-aligned boundaries:

```cpp
// Example: padding from 48 to 64 elements
const int original_dim = 48;
const int padded_dim = 64;  // Avoids bank conflicts

// AscendC implementation
constexpr int TILE_M = 64;  // Padded dimension
constexpr int TILE_N = 64;
```

This approach trades modest memory overhead for significant performance gains.

### 2. Access Pattern Rearrangement
Reorder operations so consecutive accesses target different banks:
- Interleave reads from different tensor regions
- Alternate between read and write operations where possible
- Schedule dependent operations with bank-aware timing

### 3. NZ Format Alignment
Leverage NZ format's natural 16×16 block structure which typically provides bank-friendly alignment:
- 16-element boundaries naturally distribute across banks
- Block-based access patterns reduce same-bank contention
- Works synergistically with Cube unit requirements

## Performance Impact

Proper bank conflict avoidance can recover 10-20% of lost performance in memory-bandwidth-bound kernels. The optimization is particularly effective for:
- Large matrix operations with regular access patterns
- Attention mechanisms with repeated Q×K^T operations
- Softmax operations requiring multiple passes over the same data