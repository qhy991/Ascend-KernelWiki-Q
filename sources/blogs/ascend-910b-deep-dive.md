---
id: blog-ascend-910b-deep-dive
title: "Ascend 910B Deep Dive — Architecture Improvements over 910A"
type: source-blog
author: ascend-community
date: '2026-03-20'
url: https://www.hiascend.com/forum/thread-0290101.html
architectures: [ascend910b]
tags: [ascend910b, architecture, hardware, comparison]
hardware_features: [cube-unit, vector-unit, unified-buffer, hccs]
confidence: source-reported
---

# Ascend 910B Architecture Deep Dive

Community technical analysis of architectural improvements in Ascend 910B compared to previous-generation Ascend 910A.

## Key Architectural Changes

### 1. Enhanced Cube Unit

**FP16/BF16 Throughput**: 256 TFLOPS (910A) → 320 TFLOPS (910B), ~25% improvement

**FP8 Support**: New support for E4M3/E5M2 formats, enabling:
- 2× throughput improvement for FP8 matmul
- FP8 input with FP32 accumulation (similar to NVIDIA H100)
- Memory bandwidth savings for training workloads

**Improved Precision**: Better numerical stability for reduced-precision training

### 2. Larger Unified Buffer

**Per-AICore UB**: 1 MB (910A) → 1.5 MB (910B), 50% increase

**Impact for Kernel Developers**:
- Larger tile sizes → better arithmetic intensity
- More aggressive double buffering → improved pipeline overlap
- Reduced frequency of GM accesses

**Example**: For GEMM with NZ format:
- 910A: Max tile M=128, N=256 for FP16
- 910B: Max tile M=192, N=384 for FP16 (1.5× larger tiles)

### 3. Improved HCCS Bandwidth

**Inter-NPU Communication**: 100 GB/s (910A) → 150 GB/s (910B)

**Benefit**: Faster AllReduce/AllGather for distributed training
- 8-NPU AllReduce: ~15% faster
- Enables larger model training with higher throughput

### 4. Increased AICore Count

**Compute Units**: 56 AICores (910A) → 64 AICores (910B)

**Concurrency**: 14% more parallel kernel instances
- Multi-stream execution benefits
- Better batch processing throughput

## Performance Comparison

| Metric | Ascend 910A | Ascend 910B | Improvement |
|--------|-------------|-------------|-------------|
| FP16 TFLOPS | 256 | 320 | +25% |
| FP8 TFLOPS | N/A | 640 | New |
| UB per AICore | 1 MB | 1.5 MB | +50% |
| AICore count | 56 | 64 | +14% |
| HCCS bandwidth | 100 GB/s | 150 GB/s | +50% |

## Implications for Kernel Development

### Tile Size Optimization

Larger UB enables more aggressive tiling strategies:
```ascendc
// 910A: Conservative tiling
tile_M = 128;
tile_K = 128;

// 910B: Larger tiles for better intensity
tile_M = 192;  // 1.5× larger
tile_K = 192;  // 1.5× larger
// Reduces GM accesses by 56% (1 - 1/(1.5×1.5))
```

### Grouped GEMM Improvements

More AICores + larger UB = better load balancing:
- 64 groups can run truly concurrently (vs 56 on 910A)
- Larger tiles reduce imbalance for irregular group sizes

### Memory Hierarchy

New memory bandwidth characteristics require re-profiling:
- L1 cache size unchanged, but UB increase shifts optimal tile boundaries
- GM → L1 → UB pipeline tuning needed for 910B

## Software Stack Compatibility

**CANN Version**: Requires CANN 7.0 or later for full 910B feature support

**Binary Compatibility**: 910A kernels run on 910B, but performance not optimal without recompilation

**Compiler Tuning**: CANN compiler automatically selects 910B-specific optimizations when target architecture specified

## Community Observations

- **Real-world performance**: Training BERT-base achieves 1.3× speedup on 910B vs 910A
- **Power efficiency**: 910B maintains similar TDP at higher performance
- **Availability**: 910B in mass production since 2025

## Related Resources

- [Cube Unit Architecture](hw-cube-unit) — detailed hardware specification
- [Unified Buffer Management](technique-nz-tiling) — UB optimization strategies
- [Memory Hierarchy](hw-memory-hierarchy) — GM/L1/UB/L0 architecture
