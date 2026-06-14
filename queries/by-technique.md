# Index: By Technique


## bank-conflict-avoidance (2 pages)

- [Top 10 AscendC Performance Optimization Tips](sources/blogs/ascendc-performance-tips.md)
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md)

## cube-unit (3 pages)

- [Cube Unit — Matrix Multiply Accelerator (Ascend 910/910B)](wiki/hardware/cube-unit.md)
- [Data Formats: ND vs FRACTAL_NZ](wiki/hardware/data-formats.md)
- [Triton Optimization for Ascend NPUs](wiki/techniques/triton-ascend-optimization.md)

## cube-vector-overlap (9 pages)

- [Top 10 AscendC Performance Optimization Tips](sources/blogs/ascendc-performance-tips.md)
- [CANN Training Camp — Advanced Operator Optimization Techniques](sources/blogs/cann-training-camp.md)
- [Operator Fusion Patterns on Ascend NPU](sources/docs/ascend-operator-fusion.md)
- [Ascend Profiling with msprof](sources/docs/ascend-profiling-guide.md)
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md)
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md)
- [Low Cube Utilization — Diagnosis and Resolution](wiki/patterns/low-cube-utilization.md)
- [Pipeline Stall — Queue Dependency Bottleneck](wiki/patterns/pipeline-stall.md)
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md)

## data-reuse (10 pages)

- [Top 10 AscendC Performance Optimization Tips](sources/blogs/ascendc-performance-tips.md)
- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md)
- [Operator Fusion Patterns on Ascend NPU](sources/docs/ascend-operator-fusion.md)
- [Convolution on Ascend NPU — im2col + GEMM Approach](wiki/kernels/conv-ascendc.md)
- [Embedding Lookup on Ascend NPU](wiki/kernels/embedding-ascendc.md)
- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md)
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md)
- [Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU](wiki/kernels/reduction-ascendc.md)
- [Memory-Bound Kernel — Diagnosis and Resolution](wiki/patterns/memory-bound.md)
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md)

## double-buffering (8 pages)

- [Top 10 AscendC Performance Optimization Tips](sources/blogs/ascendc-performance-tips.md)
- [CANN Training Camp — Advanced Operator Optimization Techniques](sources/blogs/cann-training-camp.md)
- [Ascend Memory Hierarchy and Data Movement](sources/docs/ascend-memory-hierarchy.md)
- [Catlass — Modular GEMM Framework for Ascend (CUTLASS equivalent)](sources/docs/catlass-framework.md)
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md)
- [Memory-Bound Kernel — Diagnosis and Resolution](wiki/patterns/memory-bound.md)
- [Pipeline Stall — Queue Dependency Bottleneck](wiki/patterns/pipeline-stall.md)
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md)

## format-conversion (4 pages)

- [Understanding FRACTAL_NZ — Ascend's 5D Data Format for Matrix Computation](sources/blogs/nz-format-explained.md)
- [Data Formats: ND vs FRACTAL_NZ](wiki/hardware/data-formats.md)
- [FRACTAL_NZ Format Traps — Common Pitfalls and Solutions](wiki/patterns/nz-format-traps.md)
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md)

## hccl-optimization (3 pages)

- [Multi-Stream Execution on Ascend NPU](sources/docs/ascend-multi-stream-guide.md)
- [HCCL Collective Communication Library](sources/docs/hccl-collective.md)
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md)

## nz-format (1 pages)

- [Data Formats: ND vs FRACTAL_NZ](wiki/hardware/data-formats.md)

## nz-tiling (13 pages)

- [Top 10 AscendC Performance Optimization Tips](sources/blogs/ascendc-performance-tips.md)
- [Understanding FRACTAL_NZ — Ascend's 5D Data Format for Matrix Computation](sources/blogs/nz-format-explained.md)
- [Ascend Quantization — FP8/INT8 Operator Development](sources/docs/ascend-quantization-guide.md)
- [Catlass — Modular GEMM Framework for Ascend (CUTLASS equivalent)](sources/docs/catlass-framework.md)
- [Convolution on Ascend NPU — im2col + GEMM Approach](wiki/kernels/conv-ascendc.md)
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md)
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md)
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md)
- [Low Cube Utilization — Diagnosis and Resolution](wiki/patterns/low-cube-utilization.md)
- [Memory-Bound Kernel — Diagnosis and Resolution](wiki/patterns/memory-bound.md)
- [FRACTAL_NZ Format Traps — Common Pitfalls and Solutions](wiki/patterns/nz-format-traps.md)
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md)
- [FRACTAL_NZ Tiling Strategy for Cube Unit](wiki/techniques/nz-tiling.md)

## pipeline-scheduling (22 pages)

- [Top 10 AscendC Performance Optimization Tips](sources/blogs/ascendc-performance-tips.md)
- [Notes on Ascend C Operator Development — Comparative Study with CUDA](sources/blogs/ascendc-programming-guide.md)
- [CANN Training Camp — Advanced Operator Optimization Techniques](sources/blogs/cann-training-camp.md)
- [Multi-Stream Execution on Ascend NPU](sources/docs/ascend-multi-stream-guide.md)
- [Operator Fusion Patterns on Ascend NPU](sources/docs/ascend-operator-fusion.md)
- [Ascend Profiling with msprof](sources/docs/ascend-profiling-guide.md)
- [Catlass — Modular GEMM Framework for Ascend (CUTLASS equivalent)](sources/docs/catlass-framework.md)
- [MTE (Memory Transfer Engine) in Ascend AICore](wiki/hardware/mte.md)
- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md)
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md)
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md)
- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md)
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md)
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md)
- [AscendC Softmax — Vector Unit Implementation](wiki/kernels/softmax-ascendc.md)
- [Low Cube Utilization — Diagnosis and Resolution](wiki/patterns/low-cube-utilization.md)
- [Pipeline Stall — Queue Dependency Bottleneck](wiki/patterns/pipeline-stall.md)
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md)
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md)
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md)
- [TQue Deadlock Pattern in Ascend C](wiki/patterns/tque-deadlock.md)
- [Triton Optimization for Ascend NPUs](wiki/techniques/triton-ascend-optimization.md)