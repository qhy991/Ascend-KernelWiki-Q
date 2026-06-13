# Index: By Kernel Type


## activation (1 pages)

- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md) conf:verified arch:ascend910, ascend910b, ascend310p

## attention (10 pages)

- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) conf:inferred arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) conf:source-reported arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) conf:source-reported arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b

## conv (1 pages)

- [Convolution on Ascend NPU — im2col + GEMM Approach](wiki/kernels/conv-ascendc.md) conf:inferred arch:ascend910, ascend910b

## elementwise (2 pages)

- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md) conf:verified arch:ascend910, ascend910b, ascend310p
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p

## embedding (2 pages)

- [Embedding Lookup on Ascend NPU](wiki/kernels/embedding-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b

## flash-attention (1 pages)

- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) conf:inferred arch:ascend910, ascend910b

## gemm (9 pages)

- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) conf:source-reported arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) conf:source-reported arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b

## grouped-gemm (2 pages)

- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md) conf:inferred arch:ascend910, ascend910b

## layernorm (4 pages)

- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b

## matmul (3 pages)

- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b

## moe (2 pages)

- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b

## reduce (2 pages)

- [Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU](wiki/kernels/reduction-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p

## rmsnorm (1 pages)

- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md) conf:source-reported arch:ascend910, ascend910b

## softmax (8 pages)

- [AscendC Softmax — Vector Unit Implementation](wiki/kernels/softmax-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b