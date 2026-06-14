# Ascend-KernelWiki-Q — Index

> Knowledge base for Huawei Ascend NPU kernel optimization (74 pages)

## Quick Links

### Hardware Features
- [Cube Unit (Matrix Multiply)](wiki/hardware/cube-unit.md) — Tensor Core equivalent
- [Vector Unit (SIMD)](wiki/hardware/vector-unit.md) — CUDA Core equivalent
- [Unified Buffer](wiki/hardware/unified-buffer.md) — Shared Memory equivalent
- [Memory Hierarchy](wiki/hardware/memory-hierarchy.md) — GM → L1 → UB → L0
- [Instruction Queues](wiki/hardware/instruction-queue.md) — 4-queue pipeline
- [Ascend 910B Architecture Evolution](wiki/hardware/ascend-910b-evolution.md) — Evolution from 910A to 910B/C
- [Hardware Synchronization Primitives](wiki/hardware/sync-primitives.md) — Barriers and EVENT management

### Optimization Techniques
- [Pipeline Scheduling](wiki/techniques/pipeline-scheduling.md) — CopyIn/Compute/CopyOut
- [Double Buffering](wiki/techniques/double-buffering.md) — Overlap transfer with compute
- [NZ Tiling](wiki/techniques/nz-tiling.md) — FRACTAL_NZ 5D format strategy
- [Cube/Vector Overlap](wiki/techniques/cube-vector-overlap.md) — Independent queue exploitation
- [Format Conversion](wiki/techniques/format-conversion.md) — ND ↔ NZ optimization
- [Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) — UB access optimization
- [Data Reuse](wiki/techniques/data-reuse.md) — Minimize GM bandwidth pressure
- [HCCL Optimization](wiki/techniques/hccl-optimization.md) — Collective communication tuning
- [Operator Fusion](wiki/techniques/operator-fusion.md) — UB/L1 Fusion strategies
- [Multi-Core Grid Scheduling](wiki/techniques/multicore-grid-scheduling.md) — BlockDim scaling & core-affinity
- [Precision Tuning & Accumulation](wiki/techniques/precision-tuning.md) — Mixed precision handling
- [Asynchronous DMA & Multi-stage Pipelines](wiki/techniques/async-dma-multistage.md) — Ping-pong buffering configurations

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
- [Paged Attention (AscendC)](wiki/kernels/paged-attention-ascendc.md) — vLLM KV cache management
- [Multi-Head Latent Attention (AscendC)](wiki/kernels/mla-ascendc.md) — DeepSeek specific optimizations
- [Quantized GEMM (AscendC)](wiki/kernels/quantized-gemm-ascendc.md) — W4A16/INT8 matmul
- [TopK & Sort (AscendC)](wiki/kernels/topk-sort-ascendc.md) — MoE routing and sampling
- [Ring Attention (AscendC)](wiki/kernels/ring-attention-ascendc.md) — Context parallelism and HCCL overlap

### Problem Diagnosis
- [Memory-Bound Kernel](wiki/patterns/memory-bound.md) — Diagnosis → solutions
- [Low Cube Utilization](wiki/patterns/low-cube-utilization.md) — Diagnosis → solutions
- [NZ Format Traps](wiki/patterns/nz-format-traps.md) — Common pitfalls + fixes
- [Pipeline Stall](wiki/patterns/pipeline-stall.md) — Queue dependency bottleneck
- [UB OOM (Unified Buffer Overflow)](wiki/patterns/ub-oom.md) — Out of memory diagnosis
- [Precision Loss & NaN Debugging](wiki/patterns/precision-nan-debugging.md) — Overflow/underflow troubleshooting
- [MTE Saturation](wiki/patterns/mte-saturation.md) — DMA bottleneck diagnosis
- [Scalar Unit Bottleneck](wiki/patterns/scalar-bottleneck.md) — Pipeline stalling from scalar unit

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
- [PyTorch OP-Plugin & CustomOp](wiki/migration/pytorch-custom-op.md) — Framework integration
- [ROCm/HIP to AscendC](wiki/migration/rocm-to-ascendc.md) — AMD mapping to Ascend
- [CANN aclnn API](wiki/migration/aclnn-api.md) — Utilizing standard operator libraries

### Tools & References
- [Profiling (msprof)](sources/docs/ascend-profiling-guide.md) — Performance analysis
- [Debugging](sources/docs/ascend-debugging-guide.md) — Twin debug + log analysis
- [Quantization (FP8/INT8)](sources/docs/ascend-quantization-guide.md) — Quantized operator development
- [Operator Fusion](sources/docs/ascend-operator-fusion.md) — Fusion patterns and templates
- [Multi-Stream](sources/docs/ascend-multi-stream-guide.md) — Concurrent execution model
- [Ascend 910B Deep Dive](sources/blogs/ascend-910b-deep-dive.md) — Architecture improvements
- [Top 10 Performance Tips](sources/blogs/ascendc-performance-tips.md) — Optimization checklist
- [MindStudio Profiling (msprof) Deep Dive](wiki/tools/msprof-guide.md) — Timeline & memory analysis
- [Ascend Simulator (Camodel)](wiki/tools/camodel-simulator.md) — CPU simulation guide
- [Auto-Tuning with AOE](wiki/tools/aoe-autotuning.md) — Automated tiling strategies

## Query Indices
- [By Hardware Feature](queries/by-hardware-feature.md)
- [By Technique](queries/by-technique.md)
- [By Kernel Type](queries/by-kernel-type.md)
- [By Language](queries/by-language.md)
- [By Problem](queries/by-problem.md)
