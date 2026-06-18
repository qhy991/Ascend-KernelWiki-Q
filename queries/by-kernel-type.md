# Index: By Kernel Type


## activation (4 pages)

- [CANN Ops Adv — Activation Operators](src/activation) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Fused GDN Gating Operator](csrc/attention/fused_gdn_gating) conf:source-reported arch:ascend910b
- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md) conf:verified arch:ascend910, ascend910b, ascend310p
- [AscendC SwiGLU — Fused Gated Activation](wiki/kernels/swiglu-ascendc.md) conf:source-reported arch:ascend910, ascend910b

## attention (46 pages)

- [CANN Ops Adv — Fused Infer Attention Score](src/transformer/fused_infer_attention_score) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Incremental Flash Attention](src/transformer/incre_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Prompt Flash Attention](src/transformer/prompt_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Flash Attention Inference Example](examples/23_flash_attention_infer) conf:source-reported arch:ascend910b
- [CATLASS MLA Example](examples/19_mla) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Assign Cache Operator](csrc/assign_cache_op) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Block Sparse Attention Operator](csrc/attentions/csrc/ops/block_sparse_attention) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Cache Location Assign Operator](csrc/cache_location_assign) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Native Source](csrc) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Laser Attention Operator](csrc/attentions/csrc/ops/laser_attention) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Lightning Indexer Operator](csrc/lightning_indexer) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU MLA Preprocess Operator](csrc/mla_preprocess) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Python Package](python) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Sparse Block Estimate Operator](csrc/attentions/csrc/ops/sparse_block_estimate) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Tests](tests) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend aclnn Torch Adapter](csrc/aclnn_torch_adapter) conf:source-reported arch:ascend910b
- [vLLM Ascend Attention Backend](vllm_ascend/attention) conf:source-reported arch:ascend910b
- [vLLM Ascend Attention Compressor Operator](csrc/attention/compressor) conf:source-reported arch:ascend910b
- [vLLM Ascend C++/AscendC Extension Source](csrc) conf:source-reported arch:ascend910b
- [vLLM Ascend Fused GDN Gating Operator](csrc/attention/fused_gdn_gating) conf:source-reported arch:ascend910b
- [vLLM Ascend In-place Partial Rotary Operator](csrc/attention/inplace_partial_rotary_mul) conf:source-reported arch:ascend910b
- [vLLM Ascend KV Quant Sparse Attention Operator](csrc/attention/kv_quant_sparse_attn_sharedkv) conf:source-reported arch:ascend910b
- [vLLM Ascend MLA Preprocess Operator](csrc/mla_preprocess) conf:source-reported arch:ascend910b
- [vLLM Ascend Model Runner](vllm_ascend/worker) conf:source-reported arch:ascend910b
- [vLLM Ascend Operator Wrappers](vllm_ascend/ops) conf:source-reported arch:ascend910b
- [vLLM Ascend Sparse Flash Attention Operator](csrc/attention/sparse_flash_attention) conf:source-reported arch:ascend910b
- [vLLM Ascend Kernel and Backend Tests](tests) conf:source-reported arch:ascend910b
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) conf:inferred arch:ascend910, ascend910b
- [Multi-Head Latent Attention (AscendC)](wiki/kernels/mla-ascendc.md) conf:inferred arch:ascend910b
- [Paged Attention (AscendC)](wiki/kernels/paged-attention-ascendc.md) conf:inferred arch:ascend910b
- [AscendC Paged Attention — Block KV Cache for NPU Inference](wiki/kernels/paged-attention-npu.md) conf:source-reported arch:ascend910b
- [Ring Attention & Context Parallelism (AscendC)](wiki/kernels/ring-attention-ascendc.md) conf:inferred arch:ascend910b
- [AscendC Rotary Position Embedding (RoPE)](wiki/kernels/rope-ascendc.md) conf:source-reported arch:ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) conf:source-reported arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) conf:source-reported arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [KV Cache Paging — Block-Table Memory Management for NPU Inference](wiki/techniques/kv-cache-paging.md) conf:source-reported arch:ascend910b
- [Online Softmax — Numerically Stable Streaming Softmax for Flash Attention](wiki/techniques/online-softmax.md) conf:source-reported arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b
- [Tiling Strategy — Host-Side Tiling and Auto-Tiling](wiki/techniques/tiling-strategy.md) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Workspace Management — UB Budgeting and GM Scratch Tensors](wiki/techniques/workspace-management.md) conf:source-reported arch:ascend910, ascend910b

## conv (2 pages)

- [CATLASS Conv Bias Example](examples/24_conv_bias) conf:source-reported arch:ascend910b
- [Convolution on Ascend NPU — im2col + GEMM Approach](wiki/kernels/conv-ascendc.md) conf:inferred arch:ascend910, ascend910b

## elementwise (24 pages)

- [Calling a Custom aclnn Operator from C++ — End to End](sources/blogs/aclnn-custom-op-invocation.md) conf:source-reported arch:ascend910, ascend910b
- [TIK Operator Walkthrough — Writing Vector Add and Softmax in Python](sources/blogs/tik-operator-walkthrough.md) conf:source-reported arch:ascend910, ascend910b
- [Ascend Samples — aclnn Single-Operator Invocation](operator/aclnn) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [CANN Ops Adv — Activation Operators](src/activation) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Conv Bias Example](examples/24_conv_bias) conf:source-reported arch:ascend910b
- [CATLASS Matmul Add Example](examples/03_matmul_add) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Assign Cache Operator](csrc/assign_cache_op) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Cache Location Assign Operator](csrc/cache_location_assign) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Lightning Indexer Operator](csrc/lightning_indexer) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU MLA Preprocess Operator](csrc/mla_preprocess) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend aclnn Torch Adapter](csrc/aclnn_torch_adapter) conf:source-reported arch:ascend910b
- [vLLM Ascend Attention Compressor Operator](csrc/attention/compressor) conf:source-reported arch:ascend910b
- [vLLM Ascend C++/AscendC Extension Source](csrc) conf:source-reported arch:ascend910b
- [vLLM Ascend Fused GDN Gating Operator](csrc/attention/fused_gdn_gating) conf:source-reported arch:ascend910b
- [vLLM Ascend In-place Partial Rotary Operator](csrc/attention/inplace_partial_rotary_mul) conf:source-reported arch:ascend910b
- [vLLM Ascend MLA Preprocess Operator](csrc/mla_preprocess) conf:source-reported arch:ascend910b
- [TIK Vector Add — Elementwise Kernel in Python](wiki/kernels/add-tik.md) conf:source-reported arch:ascend910, ascend910b
- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md) conf:verified arch:ascend910, ascend910b, ascend310p
- [AscendC Rotary Position Embedding (RoPE)](wiki/kernels/rope-ascendc.md) conf:source-reported arch:ascend910b
- [AscendC SwiGLU — Fused Gated Activation](wiki/kernels/swiglu-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [aclnn Vector Add — Single-Operator Invocation in C++](wiki/kernels/vector-add-aclnn.md) conf:source-reported arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [vllm-ascend — Custom AscendC Kernel Support (rotary_embedding)](sources/prs/vllm-ascend/PR-001.md) conf:? arch:ascend910b

## embedding (2 pages)

- [Embedding Lookup on Ascend NPU](wiki/kernels/embedding-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b

## flash-attention (13 pages)

- [CANN Ops Adv — Fused Infer Attention Score](src/transformer/fused_infer_attention_score) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Incremental Flash Attention](src/transformer/incre_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Prompt Flash Attention](src/transformer/prompt_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Flash Attention Inference Example](examples/23_flash_attention_infer) conf:source-reported arch:ascend910b
- [CATLASS MLA Example](examples/19_mla) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Block Sparse Attention Operator](csrc/attentions/csrc/ops/block_sparse_attention) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Laser Attention Operator](csrc/attentions/csrc/ops/laser_attention) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Attention Backend](vllm_ascend/attention) conf:source-reported arch:ascend910b
- [vLLM Ascend Sparse Flash Attention Operator](csrc/attention/sparse_flash_attention) conf:source-reported arch:ascend910b
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Paged Attention — Block KV Cache for NPU Inference](wiki/kernels/paged-attention-npu.md) conf:source-reported arch:ascend910b
- [KV Cache Paging — Block-Table Memory Management for NPU Inference](wiki/techniques/kv-cache-paging.md) conf:source-reported arch:ascend910b
- [Online Softmax — Numerically Stable Streaming Softmax for Flash Attention](wiki/techniques/online-softmax.md) conf:source-reported arch:ascend910, ascend910b

## gemm (38 pages)

- [W8A8 INT8 Quantization on Ascend 910B — SmoothQuant and npu_quant_matmul](sources/blogs/ascend-w8a8-quantization.md) conf:source-reported arch:ascend910b
- [CATLASS — C++ Template GEMM Kernels for Ascend (CUTLASS-style)](sources/blogs/catlass-gemm-templates.md) conf:source-reported arch:ascend910b
- [CANN Ops Adv — Grouped Matmul](src/matmul/grouped_matmul) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Matmul Operators](src/matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Basic Matmul Example](examples/00_basic_matmul) conf:source-reported arch:ascend910b
- [CATLASS Batched Matmul Example](examples/01_batched_matmul) conf:source-reported arch:ascend910b
- [CATLASS Block MMAD Components](include/catlass/gemm/block) conf:source-reported arch:ascend910b
- [CATLASS FP8 Matmul Example](examples/29_a2_fp8_e4m3_matmul) conf:source-reported arch:ascend910b
- [CATLASS Group GEMM Example](examples/16_group_gemm) conf:source-reported arch:ascend910b
- [CATLASS Layout Types](include/catlass/layout) conf:source-reported arch:ascend910b
- [CATLASS Matmul Add Example](examples/03_matmul_add) conf:source-reported arch:ascend910b
- [CATLASS Optimized Matmul Example](examples/06_optimized_matmul) conf:source-reported arch:ascend910b
- [CATLASS Python Extension Example](examples/python_extension) conf:source-reported arch:ascend910b
- [CATLASS Quantized Matmul Example](examples/12_quant_matmul) conf:source-reported arch:ascend910b
- [CATLASS Shared Library Example](examples/shared_lib) conf:source-reported arch:ascend910b
- [CATLASS Split-K Matmul Example](examples/09_splitk_matmul) conf:source-reported arch:ascend910b
- [CATLASS W8A16 Matmul Example](examples/30_w8a16_matmul) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Batch Matmul Transpose Operator](csrc/batch_matmul_transpose) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU CATLASS Utility Kernels](csrc/catlass) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Batch Matmul Transpose Operator](csrc/batch_matmul_transpose) conf:source-reported arch:ascend910b
- [vLLM Ascend Matmul AllReduce Add RMSNorm Operator](csrc/mc2/matmul_allreduce_add_rmsnorm) conf:source-reported arch:ascend910b
- [CATLASS GEMM — C++ Template Matmul on the Cube Unit](wiki/kernels/gemm-catlass-cpp.md) conf:source-reported arch:ascend910b
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC W8A8 INT8 Matmul — npu_quant_matmul](wiki/kernels/quant-matmul-ascendc.md) conf:source-reported arch:ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [torch_npu — npu_quant_matmul Dynamic W8A8 Operator](sources/prs/ascend-pytorch/PR-002.md) conf:? arch:ascend910b
- [CATLASS — Basic Matmul and Group GEMM Examples](sources/prs/catlass/PR-001.md) conf:? arch:ascend910b
- [Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory](wiki/techniques/atomic-accumulation.md) conf:inferred arch:ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) conf:source-reported arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) conf:source-reported arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b
- [INT8 Quantization — Per-Token Activation and Per-Channel Weight (W8A8)](wiki/techniques/quantization-int8.md) conf:source-reported arch:ascend910b
- [Tensor Parallelism — Communication/Compute Overlap with HCCL](wiki/techniques/tensor-parallel-overlap.md) conf:source-reported arch:ascend910b
- [Tiling Strategy — Host-Side Tiling and Auto-Tiling](wiki/techniques/tiling-strategy.md) conf:source-reported arch:ascend910, ascend910b, ascend310p

## grouped-gemm (7 pages)

- [CANN Ops Adv — Grouped Matmul](src/matmul/grouped_matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Group GEMM Example](examples/16_group_gemm) conf:source-reported arch:ascend910b
- [SGL Kernel NPU DeepEP Operators](csrc/deepep/ops) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [CATLASS — Basic Matmul and Group GEMM Examples](sources/prs/catlass/PR-001.md) conf:? arch:ascend910b

## layernorm (10 pages)

- [Ascend Samples — aclnn Single-Operator Invocation](operator/aclnn) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [SGL Kernel NPU Native Source](csrc) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Python Package](python) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Tests](tests) conf:source-reported arch:ascend910, ascend910b
- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC RMSNorm — Fused Vector Normalization](wiki/kernels/rmsnorm-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Workspace Management — UB Budgeting and GM Scratch Tensors](wiki/techniques/workspace-management.md) conf:source-reported arch:ascend910, ascend910b

## matmul (45 pages)

- [W8A8 INT8 Quantization on Ascend 910B — SmoothQuant and npu_quant_matmul](sources/blogs/ascend-w8a8-quantization.md) conf:source-reported arch:ascend910b
- [CATLASS — C++ Template GEMM Kernels for Ascend (CUTLASS-style)](sources/blogs/catlass-gemm-templates.md) conf:source-reported arch:ascend910b
- [Ascend Samples — aclnn Single-Operator Invocation](operator/aclnn) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [CANN Ops Adv — Grouped Matmul](src/matmul/grouped_matmul) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Matmul Operators](src/matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Basic Matmul Example](examples/00_basic_matmul) conf:source-reported arch:ascend910b
- [CATLASS Batched Matmul Example](examples/01_batched_matmul) conf:source-reported arch:ascend910b
- [CATLASS Block MMAD Components](include/catlass/gemm/block) conf:source-reported arch:ascend910b
- [CATLASS FP8 Matmul Example](examples/29_a2_fp8_e4m3_matmul) conf:source-reported arch:ascend910b
- [CATLASS Layout Types](include/catlass/layout) conf:source-reported arch:ascend910b
- [CATLASS Matmul Add Example](examples/03_matmul_add) conf:source-reported arch:ascend910b
- [CATLASS MLA Example](examples/19_mla) conf:source-reported arch:ascend910b
- [CATLASS Optimized Matmul Example](examples/06_optimized_matmul) conf:source-reported arch:ascend910b
- [CATLASS Python Extension Example](examples/python_extension) conf:source-reported arch:ascend910b
- [CATLASS Quantized Matmul Example](examples/12_quant_matmul) conf:source-reported arch:ascend910b
- [CATLASS Shared Library Example](examples/shared_lib) conf:source-reported arch:ascend910b
- [CATLASS Split-K Matmul Example](examples/09_splitk_matmul) conf:source-reported arch:ascend910b
- [CATLASS W8A16 Matmul Example](examples/30_w8a16_matmul) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Batch Matmul Transpose Operator](csrc/batch_matmul_transpose) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU CATLASS Utility Kernels](csrc/catlass) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Native Source](csrc) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU DeepEP Operators](csrc/deepep/ops) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Python Package](python) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Tests](tests) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend aclnn Torch Adapter](csrc/aclnn_torch_adapter) conf:source-reported arch:ascend910b
- [vLLM Ascend Batch Matmul Transpose Operator](csrc/batch_matmul_transpose) conf:source-reported arch:ascend910b
- [vLLM Ascend Matmul AllReduce Add RMSNorm Operator](csrc/mc2/matmul_allreduce_add_rmsnorm) conf:source-reported arch:ascend910b
- [vLLM Ascend Model Runner](vllm_ascend/worker) conf:source-reported arch:ascend910b
- [vLLM Ascend Operator Wrappers](vllm_ascend/ops) conf:source-reported arch:ascend910b
- [vLLM Ascend Kernel and Backend Tests](tests) conf:source-reported arch:ascend910b
- [CATLASS GEMM — C++ Template Matmul on the Cube Unit](wiki/kernels/gemm-catlass-cpp.md) conf:source-reported arch:ascend910b
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC W8A8 INT8 Matmul — npu_quant_matmul](wiki/kernels/quant-matmul-ascendc.md) conf:source-reported arch:ascend910b
- [Quantized GEMM (W4A16/INT8) (AscendC)](wiki/kernels/quantized-gemm-ascendc.md) conf:inferred arch:ascend910b
- [torch_npu — npu_quant_matmul Dynamic W8A8 Operator](sources/prs/ascend-pytorch/PR-002.md) conf:? arch:ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [CATLASS — Basic Matmul and Group GEMM Examples](sources/prs/catlass/PR-001.md) conf:? arch:ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [vllm-ascend — Default MoE w2_weight to NZ Format](sources/prs/vllm-ascend/PR-002.md) conf:? arch:ascend910b
- [Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory](wiki/techniques/atomic-accumulation.md) conf:inferred arch:ascend910b
- [INT8 Quantization — Per-Token Activation and Per-Channel Weight (W8A8)](wiki/techniques/quantization-int8.md) conf:source-reported arch:ascend910b
- [Tensor Parallelism — Communication/Compute Overlap with HCCL](wiki/techniques/tensor-parallel-overlap.md) conf:source-reported arch:ascend910b
- [Tiling Strategy — Host-Side Tiling and Auto-Tiling](wiki/techniques/tiling-strategy.md) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Workspace Management — UB Budgeting and GM Scratch Tensors](wiki/techniques/workspace-management.md) conf:source-reported arch:ascend910, ascend910b

## moe (12 pages)

- [CANN Ops Adv — Grouped Matmul](src/matmul/grouped_matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Group GEMM Example](examples/16_group_gemm) conf:source-reported arch:ascend910b
- [SGL Kernel NPU DeepEP Operators](csrc/deepep/ops) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [vLLM Ascend Model Runner](vllm_ascend/worker) conf:source-reported arch:ascend910b
- [vLLM Ascend Operator Wrappers](vllm_ascend/ops) conf:source-reported arch:ascend910b
- [vLLM Ascend Kernel and Backend Tests](tests) conf:source-reported arch:ascend910b
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Top-K — Expert Routing and Sampling Reduction](wiki/kernels/topk-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [vllm-ascend — Default MoE w2_weight to NZ Format](sources/prs/vllm-ascend/PR-002.md) conf:? arch:ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [Tensor Parallelism — Communication/Compute Overlap with HCCL](wiki/techniques/tensor-parallel-overlap.md) conf:source-reported arch:ascend910b

## paged-attention (5 pages)

- [CANN Ops Adv — Incremental Flash Attention](src/transformer/incre_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Block Sparse Attention Operator](csrc/attentions/csrc/ops/block_sparse_attention) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Attention Backend](vllm_ascend/attention) conf:source-reported arch:ascend910b
- [vLLM Ascend KV Quant Sparse Attention Operator](csrc/attention/kv_quant_sparse_attn_sharedkv) conf:source-reported arch:ascend910b
- [vLLM Ascend Sparse Flash Attention Operator](csrc/attention/sparse_flash_attention) conf:source-reported arch:ascend910b

## quant-matmul (7 pages)

- [CANN Ops Adv — Matmul Operators](src/matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS FP8 Matmul Example](examples/29_a2_fp8_e4m3_matmul) conf:source-reported arch:ascend910b
- [CATLASS Quantized Matmul Example](examples/12_quant_matmul) conf:source-reported arch:ascend910b
- [CATLASS W8A16 Matmul Example](examples/30_w8a16_matmul) conf:source-reported arch:ascend910b
- [SGL Kernel NPU CATLASS Utility Kernels](csrc/catlass) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [vLLM Ascend KV Quant Sparse Attention Operator](csrc/attention/kv_quant_sparse_attn_sharedkv) conf:source-reported arch:ascend910b

## reduce (7 pages)

- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [CATLASS Split-K Matmul Example](examples/09_splitk_matmul) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Sparse Block Estimate Operator](csrc/attentions/csrc/ops/sparse_block_estimate) conf:source-reported arch:ascend910, ascend910b
- [Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU](wiki/kernels/reduction-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC Top-K — Expert Routing and Sampling Reduction](wiki/kernels/topk-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory](wiki/techniques/atomic-accumulation.md) conf:inferred arch:ascend910b

## reduction (1 pages)

- [TopK & Sort (AscendC)](wiki/kernels/topk-sort-ascendc.md) conf:inferred arch:ascend910b

## rmsnorm (3 pages)

- [vLLM Ascend Matmul AllReduce Add RMSNorm Operator](csrc/mc2/matmul_allreduce_add_rmsnorm) conf:source-reported arch:ascend910b
- [LayerNorm / RMSNorm on Ascend NPU](wiki/kernels/layernorm-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC RMSNorm — Fused Vector Normalization](wiki/kernels/rmsnorm-ascendc.md) conf:source-reported arch:ascend910, ascend910b

## rope (6 pages)

- [SGL Kernel NPU MLA Preprocess Operator](csrc/mla_preprocess) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend C++/AscendC Extension Source](csrc) conf:source-reported arch:ascend910b
- [vLLM Ascend In-place Partial Rotary Operator](csrc/attention/inplace_partial_rotary_mul) conf:source-reported arch:ascend910b
- [vLLM Ascend MLA Preprocess Operator](csrc/mla_preprocess) conf:source-reported arch:ascend910b
- [vLLM Ascend Operator Wrappers](vllm_ascend/ops) conf:source-reported arch:ascend910b
- [vLLM Ascend Kernel and Backend Tests](tests) conf:source-reported arch:ascend910b

## softmax (15 pages)

- [TIK Operator Walkthrough — Writing Vector Add and Softmax in Python](sources/blogs/tik-operator-walkthrough.md) conf:source-reported arch:ascend910, ascend910b
- [Ascend Samples — aclnn Single-Operator Invocation](operator/aclnn) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [SGL Kernel NPU Native Source](csrc) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Python Package](python) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Tests](tests) conf:source-reported arch:ascend910, ascend910b
- [AscendC Softmax — Vector Unit Implementation](wiki/kernels/softmax-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Online Softmax — Numerically Stable Streaming Softmax for Flash Attention](wiki/techniques/online-softmax.md) conf:source-reported arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b

## swiglu (1 pages)

- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b