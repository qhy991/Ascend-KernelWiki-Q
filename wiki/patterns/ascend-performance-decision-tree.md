---
id: pattern-ascend-performance-decision-tree
title: "Ascend Performance Optimization Decision Tree"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [performance, profiling, msprof, diagnosis, pattern]
confidence: inferred
sources: [doc-torch-npu-npu-ffn, doc-msprof-profiling-overview, blog-ascendc-performance-tips, tool-msprof-guide]
symptoms: ["speedup below 1.0x", "low cube utilization", "host dispatch overhead", "memory bound", "launch overhead dominates"]
techniques: [pipeline-scheduling, tiling-strategy, cube-vector-overlap, operator-fusion]
related: [pattern-host-dispatch-bound, pattern-low-cube-utilization, pattern-memory-bound, pattern-tiling-too-small, kernel-ffn-fused-ascendc, kernel-matmul-ascendc]
---

# Ascend Performance Optimization Decision Tree

Guides optimization strategy selection for AscendC kernels — especially when agent sessions stall at correctness-passing but speedup < 1.0x.

## Step 0: Measure First

```bash
# MKB eval
python3 eval_single_runner.py -i submission.json -o 2_ffn -l ascendc_direct_launch -r result.json

# Profile (if compiled + correct)
msprof --application="python3 run_kernel.py" --output=./prof
```

Record: `mean` latency, Cube util %, Vector util %, MTE busy %, launch count.

## Decision Tree

```
Speedup < 1.0x?
│
├─ compiled=false → pattern-ascendc-compile-troubleshooting
│
├─ cheating=true → lang-mkb-integration-rules (move compute to C++)
│
├─ correctness=false → technique-ascendc-multi-dtype, pattern-nz-format-traps
│
└─ compiled + correct + slow:
    │
    ├─ M < 128 (decode)?
    │   ├─ YES → likely host-dispatch-bound
    │   │   ├─ Using unfused torch ops? → fuse via npu_ffn or custom fused kernel
    │   │   ├─ Multiple kernel launches? → single fused GEMM+act+GEMM
    │   │   └─ Still slow? → accept ~1.0x; optimize launch count not tiling
    │   │
    │   └─ NO (M ≥ 128) → continue
    │
    ├─ Cube util < 40%?
    │   ├─ YES → pattern-low-cube-utilization
    │   │   ├─ NZ format wrong? → pattern-nz-format-traps
    │   │   ├─ tile too small? → pattern-tiling-too-small
    │   │   └─ fp32 on Cube? → switch fp16/bf16 or check Cube fp32 path
    │   │
    │   └─ NO → continue
    │
    ├─ MTE busy > 60%?
    │   └─ pattern-memory-bound / pattern-mte-saturation
    │       ├─ Add double buffering → technique-double-buffering
    │       └─ Reduce GM round-trips → operator fusion
    │
    ├─ Vector idle during GEMM?
    │   └─ technique-cube-vector-overlap (pipeline GEMM + activation)
    │
    └─ Everything looks good but still slow?
        ├─ Compare vs aclnn ceiling (see below)
        └─ Consider Catlass for GEMM-heavy ops → kernel-gemm-catlass-cpp
```

## Small M vs Large M Strategies

| Dimension | M < 128 (decode) | M ≥ 1024 (prefill) |
|-----------|------------------|---------------------|
| Primary bottleneck | Launch overhead, dispatch | Cube utilization, memory BW |
| blockDim | 1–4 cores | Full core count |
| Tiling | Minimal — single tile OK | MultiCoreMatmulTiling required |
| Fusion priority | Critical (fewer launches) | Important (GM bandwidth) |
| Catlass vs hand | Hand-write simple kernel | Catlass for GEMM tiles |
| Realistic speedup | 0.8–1.1x vs npu_ffn | 1.0–1.5x |

## Catlass vs Hand-Written Cube Tiling

| Choose **Catlass** when | Choose **hand-written** when |
|-------------------------|------------------------------|
| Large square GEMM (M,N,K > 512) | Simple elementwise / activation |
| Need proven NZ tiling | FFN fusion across GEMM+Vector |
| Template reuse across shapes | MKB direct-launch minimal example |
| Quantized GEMM (W8A8) | Custom non-GEMM data movement |

See **kernel-gemm-catlass-cpp** and **kernel-matmul-ascendc**.

## Launch Overhead Analysis

If NPU event timing shows high variance (std/mean > 0.3) at small M:

1. Count ACL launches in msprof timeline
2. Each separate `kernel<<<>>>` adds ~10–50 μs overhead
3. Fused FFN = 1 launch vs unfused = 3+ launches

**pattern-host-dispatch-bound**: when launch > compute time.

## msprof Metrics → Action Mapping

| msprof observation | Likely cause | Action |
|--------------------|--------------|--------|
| Cube pipe idle during Vector busy | Sequential not overlapped | cube-vector-overlap |
| MTE queue saturated | Memory bound | double-buffer, larger tiles |
| Scalar queue long stalls | Complex indexing | simplify tile addressing |
| Low instruction count | Wrong format / wrong data region | NZ traps checklist |
| Many small kernel blocks | Over-parallelized small M | reduce blockDim |

See **tool-msprof-guide** for timeline reading.

## aclnn Operator Ceiling Reference

Custom kernels compete against fused aclnn ops (e.g., `npu_ffn`). Approximate ceilings on 910B:

| Op | Typical latency regime | Implication |
|----|------------------------|-------------|
| `npu_ffn` (fused) | Highly optimized aclnn op; hard to beat at small M ([official caveat](doc-torch-npu-npu-ffn): swiglu fusion needs vector>30µs & >10% network) | Match via C++ wrap first; custom fuse to beat |
| `torch.matmul` (unfused) | 2–5x slower than fused | Never use in forward() |
| `npu_rms_norm` | Near peak Vector BW | Custom only if fused with neighbor |
| Elementwise Vector | Easy to match | Not worth custom unless fused |

**Rule**: if custom kernel ≈ npu_ffn timing, check you're not accidentally calling aclnn inside pybind without additional fusion benefit.

## FFN-Specific Guidance

1. **Round 1–2 failure mode**: can't compile → ignore perf tree; fix project template
2. **Round 3 pass mode**: pybind wrap npu_ffn → ~1.0x (correctness baseline)
3. **Round 4+ target**: fused AscendC GEMM+act+GEMM → seek 1.1x+ at M ≥ 512
4. **SwiGLU**: fusion mandatory for bandwidth — see kernel-ffn-fused-ascendc

## Related Pages

- **pattern-host-dispatch-bound** — launch overhead diagnosis
- **pattern-low-cube-utilization** — Cube tuning
- **kernel-ffn-fused-ascendc** — FFN-specific implementation
- **tool-msprof-guide** — profiling workflow
