# Ascend-KernelWiki-Q — Index

> Knowledge base for Huawei Ascend NPU kernel optimization (53 pages)

## Quick Links

### Hardware Features
- [Cube Unit (Matrix Multiply)](wiki/hardware/cube-unit.md) — Tensor Core equivalent
- [Vector Unit (SIMD)](wiki/hardware/vector-unit.md) — CUDA Core equivalent
- [Unified Buffer](wiki/hardware/unified-buffer.md) — Shared Memory equivalent
- [Memory Hierarchy](wiki/hardware/memory-hierarchy.md) — GM → L1 → UB → L0
- [Instruction Queues](wiki/hardware/instruction-queue.md) — 4-queue pipeline

### Optimization Techniques
- [Pipeline Scheduling](wiki/techniques/pipeline-scheduling.md) — CopyIn/Compute/CopyOut
- [Double Buffering](wiki/techniques/double-buffering.md) — Overlap transfer with compute
- [NZ Tiling](wiki/techniques/nz-tiling.md) — FRACTAL_NZ 5D format strategy
- [Cube/Vector Overlap](wiki/techniques/cube-vector-overlap.md) — Independent queue exploitation
- [Format Conversion](wiki/techniques/format-conversion.md) — ND ↔ NZ optimization
- [Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) — UB access optimization
- [Data Reuse](wiki/techniques/data-reuse.md) — Minimize GM bandwidth pressure
- [HCCL Optimization](wiki/techniques/hccl-optimization.md) — Collective communication tuning

### Kernel Implementations
- [Matmul (AscendC)](wiki/kernels/matmul-ascendc.md) — GEMM via Cube + Catlass
- [Grouped GEMM](wiki/kernels/grouped-gemm-ascendc.md) — Batched matmul for MoE/GQA
- [Flash Attention (NPU)](wiki/kernels/flash-attention-npu.md) — Attention with Cube/Vector overlap
- [Softmax (AscendC)](wiki/kernels/softmax-ascendc.md) — Vector unit three-pass
- [MoE (AscendC)](wiki/kernels/moe-ascendc.md) — Mixture of Experts routing + grouped GEMM
- [LayerNorm / RMSNorm](wiki/kernels/layernorm-ascendc.md) — Normalization on Vector unit
- [Reduction](wiki/kernels/reduction-ascendc.md) — ReduceSum / ReduceMax
- [Elementwise](wiki/kernels/elementwise-ascendc.md) — Generic vector op template
- [Embedding](wiki/kernels/embedding-ascendc.md) — Lookup / gather operations
- [Convolution](wiki/kernels/conv-ascendc.md) — im2col + GEMM approach

### Problem Diagnosis
- [Memory-Bound Kernel](wiki/patterns/memory-bound.md) — Diagnosis → solutions
- [Low Cube Utilization](wiki/patterns/low-cube-utilization.md) — Diagnosis → solutions
- [NZ Format Traps](wiki/patterns/nz-format-traps.md) — Common pitfalls + fixes
- [Pipeline Stall](wiki/patterns/pipeline-stall.md) — Queue dependency bottleneck

### Programming Guides
- [AscendC Guide](wiki/languages/ascendc-guide.md) — Complete programming tutorial
- [TBE-DSL Guide](wiki/languages/tbe-dsl-guide.md) — Deprecated Python DSL

### Migration Guides
- [CUDA → AscendC](wiki/migration/cuda-to-ascendc.md) — Concept mapping + migration steps
- [Memory Model Mapping](wiki/migration/memory-model-mapping.md) — Shared mem → UB
- [API Equivalents](wiki/migration/api-equivalents.md) — Complete API reference table
- [Triton → AscendC](wiki/migration/triton-to-ascendc.md) — Triton programming model mapping
- [TBE → AscendC](wiki/migration/tbe-to-ascendc.md) — Huawei's recommended migration path
- [CUTLASS → Catlass](wiki/migration/cutlass-to-catlass.md) — GEMM framework migration

### Tools & References
- [Profiling (msprof)](sources/docs/ascend-profiling-guide.md) — Performance analysis
- [Debugging](sources/docs/ascend-debugging-guide.md) — Twin debug + log analysis
- [Quantization (FP8/INT8)](sources/docs/ascend-quantization-guide.md) — Quantized operator development
- [Operator Fusion](sources/docs/ascend-operator-fusion.md) — Fusion patterns and templates
- [Multi-Stream](sources/docs/ascend-multi-stream-guide.md) — Concurrent execution model
- [Ascend 910B Deep Dive](sources/blogs/ascend-910b-deep-dive.md) — Architecture improvements
- [Top 10 Performance Tips](sources/blogs/ascendc-performance-tips.md) — Optimization checklist

## Query Indices
- [By Hardware Feature](queries/by-hardware-feature.md)
- [By Technique](queries/by-technique.md)
- [By Kernel Type](queries/by-kernel-type.md)
- [By Language](queries/by-language.md)
- [By Problem](queries/by-problem.md)
