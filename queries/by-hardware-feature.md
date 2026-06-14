# Index: By Hardware Feature


## cube-unit (17 pages)

- [Ascend 910B Deep Dive — Architecture Improvements over 910A](sources/blogs/ascend-910b-deep-dive.md) `[source-blog]` arch:ascend910b
- [Understanding FRACTAL_NZ — Ascend's 5D Data Format for Matrix Computation](sources/blogs/nz-format-explained.md) `[source-blog]` arch:ascend910, ascend910b
- [Operator Fusion Patterns on Ascend NPU](sources/docs/ascend-operator-fusion.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Profiling with msprof](sources/docs/ascend-profiling-guide.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Quantization — FP8/INT8 Operator Development](sources/docs/ascend-quantization-guide.md) `[source-doc]` arch:ascend910b
- [AscendC API Reference (CANN 8.0)](sources/docs/ascendc-api-reference.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Catlass — Modular GEMM Framework for Ascend (CUTLASS equivalent)](sources/docs/catlass-framework.md) `[source-doc]` arch:ascend910, ascend910b
- [Cube Unit — Matrix Multiply Accelerator (Ascend 910/910B)](wiki/hardware/cube-unit.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [Data Formats: ND vs FRACTAL_NZ](wiki/hardware/data-formats.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [Convolution on Ascend NPU — im2col + GEMM Approach](wiki/kernels/conv-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) `[source-pr]` arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) `[wiki-technique]` arch:ascend910, ascend910b
- [FRACTAL_NZ Tiling Strategy for Cube Unit](wiki/techniques/nz-tiling.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Triton Optimization for Ascend NPUs](wiki/techniques/triton-ascend-optimization.md) `[wiki-technique]` arch:ascend910, ascend910b

## event-sync (1 pages)

- [Instruction Queue System — 4-Queue Pipeline Architecture](wiki/hardware/instruction-queue.md) `[wiki-hardware]` arch:ascend910, ascend910b

## global-memory (3 pages)

- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md) `[source-doc]` arch:ascend910, ascend910b
- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Ascend Memory Hierarchy (GM → L1 → UB → L0)](wiki/hardware/memory-hierarchy.md) `[wiki-hardware]` arch:ascend910, ascend910b

## hccs (3 pages)

- [Ascend 910B Deep Dive — Architecture Improvements over 910A](sources/blogs/ascend-910b-deep-dive.md) `[source-blog]` arch:ascend910b
- [HCCL Collective Communication Library](sources/docs/hccl-collective.md) `[source-doc]` arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) `[wiki-technique]` arch:ascend910, ascend910b

## instruction-queue (5 pages)

- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Instruction Queue System — 4-Queue Pipeline Architecture](wiki/hardware/instruction-queue.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) `[wiki-technique]` arch:ascend910, ascend910b
- [TQue Deadlock Pattern in Ascend C](wiki/patterns/tque-deadlock.md) `[wiki-pattern]` arch:ascend910, ascend910b

## l0-buffer (2 pages)

- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Memory Hierarchy (GM → L1 → UB → L0)](wiki/hardware/memory-hierarchy.md) `[wiki-hardware]` arch:ascend910, ascend910b

## l1-buffer (3 pages)

- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md) `[source-doc]` arch:ascend910, ascend910b
- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Ascend Memory Hierarchy (GM → L1 → UB → L0)](wiki/hardware/memory-hierarchy.md) `[wiki-hardware]` arch:ascend910, ascend910b

## mte (9 pages)

- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Profiling with msprof](sources/docs/ascend-profiling-guide.md) `[source-doc]` arch:ascend910, ascend910b
- [AscendC API Reference (CANN 8.0)](sources/docs/ascendc-api-reference.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Ascend Memory Hierarchy (GM → L1 → UB → L0)](wiki/hardware/memory-hierarchy.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [MTE (Memory Transfer Engine) in Ascend AICore](wiki/hardware/mte.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) `[wiki-technique]` arch:ascend910, ascend910b

## nd-format (2 pages)

- [Data Formats: ND vs FRACTAL_NZ](wiki/hardware/data-formats.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) `[wiki-technique]` arch:ascend910, ascend910b

## nz-format (5 pages)

- [Understanding FRACTAL_NZ — Ascend's 5D Data Format for Matrix Computation](sources/blogs/nz-format-explained.md) `[source-blog]` arch:ascend910, ascend910b
- [Data Formats: ND vs FRACTAL_NZ](wiki/hardware/data-formats.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [FRACTAL_NZ Format Traps — Common Pitfalls and Solutions](wiki/patterns/nz-format-traps.md) `[wiki-pattern]` arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) `[wiki-technique]` arch:ascend910, ascend910b
- [FRACTAL_NZ Tiling Strategy for Cube Unit](wiki/techniques/nz-tiling.md) `[wiki-technique]` arch:ascend910, ascend910b

## scalar-unit (2 pages)

- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Scalar Unit in Ascend AICore](wiki/hardware/scalar-unit.md) `[wiki-hardware]` arch:ascend910, ascend910b

## unified-buffer (17 pages)

- [Ascend 910B Deep Dive — Architecture Improvements over 910A](sources/blogs/ascend-910b-deep-dive.md) `[source-blog]` arch:ascend910b
- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md) `[source-doc]` arch:ascend910, ascend910b
- [Operator Fusion Patterns on Ascend NPU](sources/docs/ascend-operator-fusion.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Profiling with msprof](sources/docs/ascend-profiling-guide.md) `[source-doc]` arch:ascend910, ascend910b
- [AscendC API Reference (CANN 8.0)](sources/docs/ascendc-api-reference.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Catlass — Modular GEMM Framework for Ascend (CUTLASS equivalent)](sources/docs/catlass-framework.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Memory Hierarchy (GM → L1 → UB → L0)](wiki/hardware/memory-hierarchy.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [MTE (Memory Transfer Engine) in Ascend AICore](wiki/hardware/mte.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [Unified Buffer (UB) — On-Chip Scratchpad Memory](wiki/hardware/unified-buffer.md) `[wiki-hardware]` arch:ascend910, ascend910b
- [CUDA Memory Model → Ascend Memory Model Mapping](wiki/migration/memory-model-mapping.md) `[wiki-migration]` arch:
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) `[source-pr]` arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) `[wiki-technique]` arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) `[wiki-technique]` arch:ascend910, ascend910b
- [Triton Optimization for Ascend NPUs](wiki/techniques/triton-ascend-optimization.md) `[wiki-technique]` arch:ascend910, ascend910b

## vector-unit (16 pages)

- [Ascend 910B Deep Dive — Architecture Improvements over 910A](sources/blogs/ascend-910b-deep-dive.md) `[source-blog]` arch:ascend910b
- [Operator Fusion Patterns on Ascend NPU](sources/docs/ascend-operator-fusion.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Profiling with msprof](sources/docs/ascend-profiling-guide.md) `[source-doc]` arch:ascend910, ascend910b
- [Ascend Quantization — FP8/INT8 Operator Development](sources/docs/ascend-quantization-guide.md) `[source-doc]` arch:ascend910b
- [AscendC API Reference (CANN 8.0)](sources/docs/ascendc-api-reference.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [CANN Architecture Guide — AICore Hardware Principles](sources/docs/cann-architecture-guide.md) `[source-doc]` arch:ascend910, ascend910b, ascend310p
- [Vector Unit — SIMD Processing Engine](wiki/hardware/vector-unit.md) `[wiki-hardware]` arch:ascend910, ascend910b, ascend310p
- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b, ascend310p
- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU](wiki/kernels/reduction-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [AscendC Softmax — Vector Unit Implementation](wiki/kernels/softmax-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) `[source-pr]` arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) `[wiki-technique]` arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) `[wiki-technique]` arch:ascend910, ascend910b
- [RoPE (Rotary Positional Embedding) Implementation in Ascend C](wiki/kernels/rope-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b
- [SwiGLU Activation Implementation in Ascend C](wiki/kernels/swiglu-ascendc.md) `[wiki-kernel]` arch:ascend910, ascend910b