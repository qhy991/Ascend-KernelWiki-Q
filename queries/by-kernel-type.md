# Index: By Kernel Type


## activation (12 pages)

- [CANN Ops Adv — Activation Operators](src/activation) conf:source-reported arch:ascend910, ascend910b
- [MultiKernelBench — AscendC Direct Launch Backend](backends/ascendc_direct_launch_backend.py) conf:verified arch:ascend910b
- [vLLM Ascend Fused GDN Gating Operator](csrc/attention/fused_gdn_gating) conf:source-reported arch:ascend910b
- [AscendC Fused Operator Programming — Matmul + Activation](sources/docs/ascendc-fused-operator-matmul.md) conf:verified arch:ascend910, ascend910b
- [torch_npu.npu_ffn — Fused FFN / MoE FFN Operator](sources/docs/torch-npu-npu-ffn.md) conf:verified arch:ascend910b
- [Activation Functions in Ascend C](wiki/kernels/activation-ascendc.md) conf:verified arch:ascend910, ascend910b
- [Elementwise Operations — AscendC Vector Template](wiki/kernels/elementwise-ascendc.md) conf:verified arch:ascend910, ascend910b, ascend310p
- [AscendC FFN Fused Kernel — Dual GEMM + Activation](wiki/kernels/ffn-fused-ascendc.md) conf:source-reported arch:ascend910b
- [MKB Working Kernel Examples — Verified Submissions](wiki/kernels/mkb-working-examples.md) conf:verified arch:ascend910b
- [AscendC SwiGLU — Fused Gated Activation](wiki/kernels/swiglu-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues](wiki/techniques/ascend-gmm-fusion-epilogues.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Multi-Dtype Support — fp16, bf16, fp32](wiki/techniques/ascendc-multi-dtype.md) conf:verified arch:ascend910, ascend910b

## attention (73 pages)

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
- [CATLASS Flash Attention Grad TND — Backward Attention Case Study](wiki/kernels/flash-attention-grad-tnd-catlass.md) conf:inferred arch:ascend910, ascend910b
- [Flash Attention Infer in CATLASS](wiki/kernels/flash-attention-infer-catlass.md) conf:source-reported arch:ascend910, ascend910b
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) conf:inferred arch:ascend910, ascend910b
- [Multi-Head Latent Attention (AscendC)](wiki/kernels/mla-ascendc.md) conf:inferred arch:ascend910b
- [AscendC Paged Attention — Block KV Cache for NPU Inference](wiki/kernels/paged-attention-npu.md) conf:source-reported arch:ascend910b
- [Ring Attention (AscendC)](wiki/kernels/ring-attention-ascendc.md) conf:inferred arch:ascend910b
- [AscendC Rotary Position Embedding (RoPE)](wiki/kernels/rope-ascendc.md) conf:source-reported arch:ascend910b
- [KV Block Semantic Drift — Physical, Compressed, SWA, and Hybrid Blocks Mixed](wiki/patterns/kv-block-semantic-drift.md) conf:source-reported arch:ascend910, ascend910b
- [Online Softmax Wait Boundary — Tail Row Synchronization Drift](wiki/patterns/online-softmax-wait-boundary.md) conf:source-reported arch:ascend910, ascend910b
- [Workspace Offset Under-allocation — Host Tiling and Kernel Path Mismatch](wiki/patterns/workspace-offset-underallocation.md) conf:source-reported arch:ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [CATLASS — Flash Attention Grad TND Example and Block Components](sources/prs/catlass/PR-169.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Flash Attention Infer Base Implementation](sources/prs/catlass/PR-200.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Online Softmax RowNum=1 Wait Boundary Fix](sources/prs/catlass/PR-237.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — MLA Supports Ring Attention and Tensor Parallel Context Parallel](sources/prs/mindspeed/PR-2796.md) conf:source-reported arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [vllm-ascend — D-side Partial-Group Caching for Hybrid Mamba Models](sources/prs/vllm-ascend/PR-10009.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Ascend 950 QLI Workspace Sizing for Long Context](sources/prs/vllm-ascend/PR-10041.md) conf:source-reported arch:ascend910b
- [vllm-ascend — Layerwise KV Pooling for AscendStore](sources/prs/vllm-ascend/PR-10077.md) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend — Zigzag Context Parallel Optimization for DSA Prefill](sources/prs/vllm-ascend/PR-10169.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Mooncake PP Layer Index and MTP Block Flattening Fix](sources/prs/vllm-ascend/PR-10202.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — AscendStore Grouped Hash Lookup Encoding Alignment](sources/prs/vllm-ascend/PR-10217.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Trim SWA KV Transfer Blocks Before Window Clipping](sources/prs/vllm-ascend/PR-10255.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — DeepSeek-V4 Compressed Prefix-Cache Lookup Granularity](sources/prs/vllm-ascend/PR-10298.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Remove Manual DeepSeek-V4 Patch Environment Gate](sources/prs/vllm-ascend/PR-10333.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Mooncake Connector Support for DeepSeek-V4 Hybrid KV](sources/prs/vllm-ascend/PR-10342.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Skip Pre-KV Graph Memory Profiling for DeepSeek-V4 Compressed Attention](sources/prs/vllm-ascend/PR-10369.md) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend — Async O-Projection TP Weight AllGather in DSA-CP](sources/prs/vllm-ascend/PR-10694.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — AscendStore Hybrid/Mamba Aligned Prefix Cache](sources/prs/vllm-ascend/PR-9533.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — DeepSeek-V4 Support for Ascend 950](sources/prs/vllm-ascend/PR-9757.md) conf:source-reported arch:ascend910b
- [vllm-ascend — Keep DeepSeek-V4 DSA Forward Outside Piecewise Graph Capture](sources/prs/vllm-ascend/PR-9935.md) conf:source-reported arch:ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [DeepSeek-V4 on Ascend 950 — Compressed Attention Runtime Adaptation](wiki/techniques/deepseek-v4-ascend950-runtime.md) conf:inferred arch:ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) conf:source-reported arch:ascend910, ascend910b
- [DSA Context-Parallel Prefill Overlap on Ascend](wiki/techniques/dsa-context-parallel-prefill-overlap.md) conf:source-reported arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) conf:source-reported arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [KV Cache Paging — Block-Table Memory Management for NPU Inference](wiki/techniques/kv-cache-paging.md) conf:source-reported arch:ascend910b
- [MLA Ring Context Parallel on Ascend — Heterogeneous K/V P2P](wiki/techniques/mla-ring-context-parallel.md) conf:inferred arch:ascend910, ascend910b
- [Online Softmax — Numerically Stable Streaming Softmax for Flash Attention](wiki/techniques/online-softmax.md) conf:source-reported arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b
- [Tiling Strategy — Host-Side Tiling and Auto-Tiling](wiki/techniques/tiling-strategy.md) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [vLLM Ascend Hybrid/Mamba KV Cache — Group-Aware Transfer and Prefix Caching](wiki/techniques/vllm-hybrid-mamba-kv-cache.md) conf:inferred arch:ascend910, ascend910b
- [Workspace Management — UB Budgeting and GM Scratch Tensors](wiki/techniques/workspace-management.md) conf:source-reported arch:ascend910, ascend910b

## conv (2 pages)

- [CATLASS Conv Bias Example](examples/24_conv_bias) conf:source-reported arch:ascend910b
- [Convolution on Ascend NPU — im2col + GEMM Approach](wiki/kernels/conv-ascendc.md) conf:inferred arch:ascend910, ascend910b

## elementwise (31 pages)

- [Calling a Custom aclnn Operator from C++ — End to End](sources/blogs/aclnn-custom-op-invocation.md) conf:source-reported arch:ascend910, ascend910b
- [TIK Operator Walkthrough — Writing Vector Add and Softmax in Python](sources/blogs/tik-operator-walkthrough.md) conf:source-reported arch:ascend910, ascend910b
- [Ascend Samples — aclnn Single-Operator Invocation](operator/aclnn) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [CANN Ops Adv — Activation Operators](src/activation) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Conv Bias Example](examples/24_conv_bias) conf:source-reported arch:ascend910b
- [CATLASS Matmul Add Example](examples/03_matmul_add) conf:source-reported arch:ascend910b
- [MultiKernelBench — AscendC Direct Launch Backend](backends/ascendc_direct_launch_backend.py) conf:verified arch:ascend910b
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
- [MKB Working Kernel Examples — Verified Submissions](wiki/kernels/mkb-working-examples.md) conf:verified arch:ascend910b
- [AscendC Rotary Position Embedding (RoPE)](wiki/kernels/rope-ascendc.md) conf:source-reported arch:ascend910b
- [AscendC SwiGLU — Fused Gated Activation](wiki/kernels/swiglu-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [aclnn Vector Add — Single-Operator Invocation in C++](wiki/kernels/vector-add-aclnn.md) conf:source-reported arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [cann-ops-adv — GroupedMatmulAdd Operator for MoE Fusion](sources/prs/cann-ops-adv/PR-140.md) conf:source-reported arch:ascend910, ascend910b
- [sgl-kernel-npu — Fused GDN Gating + solve_tril Performance](sources/prs/sgl-kernel-npu/PR-003.md) conf:? arch:ascend910, ascend910b
- [vllm-ascend — Custom AscendC Kernel Support (rotary_embedding)](sources/prs/vllm-ascend/PR-001.md) conf:? arch:ascend910b
- [vllm-ascend — AscendC store_kv_block Op (Scatter into Paged KV Cache)](sources/prs/vllm-ascend/PR-003.md) conf:? arch:ascend910b
- [GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues](wiki/techniques/ascend-gmm-fusion-epilogues.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Multi-Dtype Support — fp16, bf16, fp32](wiki/techniques/ascendc-multi-dtype.md) conf:verified arch:ascend910, ascend910b

## embedding (2 pages)

- [Embedding Lookup on Ascend NPU](wiki/kernels/embedding-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b

## flash-attention (20 pages)

- [CANN Ops Adv — Fused Infer Attention Score](src/transformer/fused_infer_attention_score) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Incremental Flash Attention](src/transformer/incre_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [CANN Ops Adv — Prompt Flash Attention](src/transformer/prompt_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Flash Attention Inference Example](examples/23_flash_attention_infer) conf:source-reported arch:ascend910b
- [CATLASS MLA Example](examples/19_mla) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Block Sparse Attention Operator](csrc/attentions/csrc/ops/block_sparse_attention) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Laser Attention Operator](csrc/attentions/csrc/ops/laser_attention) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Attention Backend](vllm_ascend/attention) conf:source-reported arch:ascend910b
- [vLLM Ascend Sparse Flash Attention Operator](csrc/attention/sparse_flash_attention) conf:source-reported arch:ascend910b
- [CATLASS Flash Attention Grad TND — Backward Attention Case Study](wiki/kernels/flash-attention-grad-tnd-catlass.md) conf:inferred arch:ascend910, ascend910b
- [Flash Attention Infer in CATLASS](wiki/kernels/flash-attention-infer-catlass.md) conf:source-reported arch:ascend910, ascend910b
- [Flash Attention on Ascend NPU](wiki/kernels/flash-attention-npu.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Paged Attention — Block KV Cache for NPU Inference](wiki/kernels/paged-attention-npu.md) conf:source-reported arch:ascend910b
- [Online Softmax Wait Boundary — Tail Row Synchronization Drift](wiki/patterns/online-softmax-wait-boundary.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Flash Attention Grad TND Example and Block Components](sources/prs/catlass/PR-169.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Flash Attention Infer Base Implementation](sources/prs/catlass/PR-200.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Online Softmax RowNum=1 Wait Boundary Fix](sources/prs/catlass/PR-237.md) conf:source-reported arch:ascend910, ascend910b
- [KV Cache Paging — Block-Table Memory Management for NPU Inference](wiki/techniques/kv-cache-paging.md) conf:source-reported arch:ascend910b
- [MLA Ring Context Parallel on Ascend — Heterogeneous K/V P2P](wiki/techniques/mla-ring-context-parallel.md) conf:inferred arch:ascend910, ascend910b
- [Online Softmax — Numerically Stable Streaming Softmax for Flash Attention](wiki/techniques/online-softmax.md) conf:source-reported arch:ascend910, ascend910b

## gemm (51 pages)

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
- [CATLASS Flash Attention Grad TND — Backward Attention Case Study](wiki/kernels/flash-attention-grad-tnd-catlass.md) conf:inferred arch:ascend910, ascend910b
- [CATLASS GEMM — C++ Template Matmul on the Cube Unit](wiki/kernels/gemm-catlass-cpp.md) conf:source-reported arch:ascend910b
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC W8A8 INT8 Matmul — npu_quant_matmul](wiki/kernels/quant-matmul-ascendc.md) conf:source-reported arch:ascend910b
- [Grouped GEMM Empty-K Output Init — No Compute Still Needs Semantics](wiki/patterns/grouped-gemm-empty-k-output-init.md) conf:source-reported arch:ascend910, ascend910b
- [Manifest-Driven Kernel Autotune — Separate Kernel Inventory from Shape Selection](wiki/patterns/manifest-driven-kernel-autotune.md) conf:source-reported arch:ascend910, ascend910b
- [Preload nextBlock Metadata Reuse — Current Tile State Leaks into Next Tile](wiki/patterns/preload-nextblock-metadata-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [torch_npu — npu_quant_matmul Dynamic W8A8 Operator](sources/prs/ascend-pytorch/PR-002.md) conf:? arch:ascend910b
- [cann-ops-adv — grouped_matmul_swiglu_quant Fused MoE FFN Kernel](sources/prs/cann-ops-adv/PR-001.md) conf:? arch:ascend910, ascend910b
- [CATLASS — Basic Matmul and Group GEMM Examples](sources/prs/catlass/PR-001.md) conf:? arch:ascend910b
- [CATLASS — BlockMmad Preload nextBlock K-Tile Index Fix](sources/prs/catlass/PR-159.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Flash Attention Grad TND Example and Block Components](sources/prs/catlass/PR-169.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Grouped Matmul Slice-K Ki=0 Output Clear](sources/prs/catlass/PR-214.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — mstuner_catlass Kernel Manifest and Tuning Toolchain](sources/prs/catlass/PR-266.md) conf:source-reported arch:ascend910, ascend910b
- [sgl-kernel-npu — LoRA Kernels on the CUBE Unit (sgemmc)](sources/prs/sgl-kernel-npu/PR-002.md) conf:? arch:ascend910, ascend910b
- [vllm-ascend — W8A8FP8 Dynamic Quantization on Ascend 950](sources/prs/vllm-ascend/PR-004.md) conf:? arch:ascend910b
- [vllm-ascend — DeepSeek-V4 Support for Ascend 950](sources/prs/vllm-ascend/PR-9757.md) conf:source-reported arch:ascend910b
- [Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory](wiki/techniques/atomic-accumulation.md) conf:inferred arch:ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [DeepSeek-V4 on Ascend 950 — Compressed Attention Runtime Adaptation](wiki/techniques/deepseek-v4-ascend950-runtime.md) conf:inferred arch:ascend910b
- [Double Buffering — Overlapping Data Transfer with Compute](wiki/techniques/double-buffering.md) conf:source-reported arch:ascend910, ascend910b
- [ND ↔ NZ Format Conversion Optimization](wiki/techniques/format-conversion.md) conf:source-reported arch:ascend910, ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b
- [INT8 Quantization — Per-Token Activation and Per-Channel Weight (W8A8)](wiki/techniques/quantization-int8.md) conf:source-reported arch:ascend910b
- [Tensor Parallelism — Communication/Compute Overlap with HCCL](wiki/techniques/tensor-parallel-overlap.md) conf:source-reported arch:ascend910b
- [Tiling Strategy — Host-Side Tiling and Auto-Tiling](wiki/techniques/tiling-strategy.md) conf:source-reported arch:ascend910, ascend910b, ascend310p

## grouped-gemm (15 pages)

- [CANN Ops Adv — Grouped Matmul](src/matmul/grouped_matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Group GEMM Example](examples/16_group_gemm) conf:source-reported arch:ascend910b
- [SGL Kernel NPU DeepEP Operators](csrc/deepep/ops) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [Grouped GEMM on Ascend NPU — Batched Matrix Multiply for MoE and GQA](wiki/kernels/grouped-gemm-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [Grouped GEMM Empty-K Output Init — No Compute Still Needs Semantics](wiki/patterns/grouped-gemm-empty-k-output-init.md) conf:source-reported arch:ascend910, ascend910b
- [Manifest-Driven Kernel Autotune — Separate Kernel Inventory from Shape Selection](wiki/patterns/manifest-driven-kernel-autotune.md) conf:source-reported arch:ascend910, ascend910b
- [cann-ops-adv — GroupedMatmulAdd Operator for MoE Fusion](sources/prs/cann-ops-adv/PR-140.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Basic Matmul and Group GEMM Examples](sources/prs/catlass/PR-001.md) conf:? arch:ascend910b
- [CATLASS — Grouped Matmul Slice-K Ki=0 Output Clear](sources/prs/catlass/PR-214.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — mstuner_catlass Kernel Manifest and Tuning Toolchain](sources/prs/catlass/PR-266.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — all_to_all_v_c Variable-Count MoE Communication Optimization](sources/prs/mindspeed/PR-2828.md) conf:source-reported arch:ascend910, ascend910b
- [GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues](wiki/techniques/ascend-gmm-fusion-epilogues.md) conf:inferred arch:ascend910, ascend910b
- [Training Communication Scheduling for MoE and Param-Gather Overlap](wiki/techniques/training-communication-scheduling-overlap.md) conf:source-reported arch:ascend910, ascend910b

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

## matmul (67 pages)

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
- [MultiKernelBench — AscendC Direct Launch Backend](backends/ascendc_direct_launch_backend.py) conf:verified arch:ascend910b
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
- [AscendC Fused Operator Programming — Matmul + Activation](sources/docs/ascendc-fused-operator-matmul.md) conf:verified arch:ascend910, ascend910b
- [torch_npu.npu_ffn — Fused FFN / MoE FFN Operator](sources/docs/torch-npu-npu-ffn.md) conf:verified arch:ascend910b
- [AscendC FFN Fused Kernel — Dual GEMM + Activation](wiki/kernels/ffn-fused-ascendc.md) conf:source-reported arch:ascend910b
- [Flash Attention Infer in CATLASS](wiki/kernels/flash-attention-infer-catlass.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS GEMM — C++ Template Matmul on the Cube Unit](wiki/kernels/gemm-catlass-cpp.md) conf:source-reported arch:ascend910b
- [AscendC Matmul — GEMM via Cube Unit and Catlass](wiki/kernels/matmul-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [MKB Working Kernel Examples — Verified Submissions](wiki/kernels/mkb-working-examples.md) conf:verified arch:ascend910b
- [AscendC W8A8 INT8 Matmul — npu_quant_matmul](wiki/kernels/quant-matmul-ascendc.md) conf:source-reported arch:ascend910b
- [Grouped GEMM Empty-K Output Init — No Compute Still Needs Semantics](wiki/patterns/grouped-gemm-empty-k-output-init.md) conf:source-reported arch:ascend910, ascend910b
- [Manifest-Driven Kernel Autotune — Separate Kernel Inventory from Shape Selection](wiki/patterns/manifest-driven-kernel-autotune.md) conf:source-reported arch:ascend910, ascend910b
- [Preload nextBlock Metadata Reuse — Current Tile State Leaks into Next Tile](wiki/patterns/preload-nextblock-metadata-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [torch_npu — npu_quant_matmul Dynamic W8A8 Operator](sources/prs/ascend-pytorch/PR-002.md) conf:? arch:ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [cann-ops-adv — grouped_matmul_swiglu_quant Fused MoE FFN Kernel](sources/prs/cann-ops-adv/PR-001.md) conf:? arch:ascend910, ascend910b
- [CATLASS — Basic Matmul and Group GEMM Examples](sources/prs/catlass/PR-001.md) conf:? arch:ascend910b
- [CATLASS — BlockMmad Preload nextBlock K-Tile Index Fix](sources/prs/catlass/PR-159.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Flash Attention Infer Base Implementation](sources/prs/catlass/PR-200.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Grouped Matmul Slice-K Ki=0 Output Clear](sources/prs/catlass/PR-214.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — mstuner_catlass Kernel Manifest and Tuning Toolchain](sources/prs/catlass/PR-266.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — Bucket Group Reordering for Param-Gather Overlap](sources/prs/mindspeed/PR-2823.md) conf:source-reported arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [sgl-kernel-npu — LoRA Kernels on the CUBE Unit (sgemmc)](sources/prs/sgl-kernel-npu/PR-002.md) conf:? arch:ascend910, ascend910b
- [vllm-ascend — Default MoE w2_weight to NZ Format](sources/prs/vllm-ascend/PR-002.md) conf:? arch:ascend910b
- [vllm-ascend — W8A8FP8 Dynamic Quantization on Ascend 950](sources/prs/vllm-ascend/PR-004.md) conf:? arch:ascend910b
- [vLLM Ascend — Zigzag Context Parallel Optimization for DSA Prefill](sources/prs/vllm-ascend/PR-10169.md) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend — Async O-Projection TP Weight AllGather in DSA-CP](sources/prs/vllm-ascend/PR-10694.md) conf:source-reported arch:ascend910, ascend910b
- [GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues](wiki/techniques/ascend-gmm-fusion-epilogues.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Multi-Dtype Support — fp16, bf16, fp32](wiki/techniques/ascendc-multi-dtype.md) conf:verified arch:ascend910, ascend910b
- [Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory](wiki/techniques/atomic-accumulation.md) conf:inferred arch:ascend910b
- [DSA Context-Parallel Prefill Overlap on Ascend](wiki/techniques/dsa-context-parallel-prefill-overlap.md) conf:source-reported arch:ascend910, ascend910b
- [INT8 Quantization — Per-Token Activation and Per-Channel Weight (W8A8)](wiki/techniques/quantization-int8.md) conf:source-reported arch:ascend910b
- [Tensor Parallelism — Communication/Compute Overlap with HCCL](wiki/techniques/tensor-parallel-overlap.md) conf:source-reported arch:ascend910b
- [Tiling Strategy — Host-Side Tiling and Auto-Tiling](wiki/techniques/tiling-strategy.md) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Training Communication Scheduling for MoE and Param-Gather Overlap](wiki/techniques/training-communication-scheduling-overlap.md) conf:source-reported arch:ascend910, ascend910b
- [Workspace Management — UB Budgeting and GM Scratch Tensors](wiki/techniques/workspace-management.md) conf:source-reported arch:ascend910, ascend910b

## moe (27 pages)

- [CANN Ops Adv — Grouped Matmul](src/matmul/grouped_matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Group GEMM Example](examples/16_group_gemm) conf:source-reported arch:ascend910b
- [SGL Kernel NPU DeepEP Operators](csrc/deepep/ops) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [vLLM Ascend Model Runner](vllm_ascend/worker) conf:source-reported arch:ascend910b
- [vLLM Ascend Operator Wrappers](vllm_ascend/ops) conf:source-reported arch:ascend910b
- [vLLM Ascend Kernel and Backend Tests](tests) conf:source-reported arch:ascend910b
- [MoE (Mixture of Experts) Kernel on Ascend NPU](wiki/kernels/moe-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [AscendC Top-K — Expert Routing and Sampling Reduction](wiki/kernels/topk-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [cann-ops-adv — grouped_matmul_swiglu_quant Fused MoE FFN Kernel](sources/prs/cann-ops-adv/PR-001.md) conf:? arch:ascend910, ascend910b
- [cann-ops-adv — GroupedMatmulAdd Operator for MoE Fusion](sources/prs/cann-ops-adv/PR-140.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — Fused MoE Token Permute and Unpermute on NPU](sources/prs/mindspeed/PR-2703.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — Pipeline Parallel P2P Uses isend/irecv on NPU](sources/prs/mindspeed/PR-2707.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — MindSpore MoE All-to-All Compute/Communication Overlap](sources/prs/mindspeed/PR-2730.md) conf:source-reported arch:ascend910, ascend910b
- [MindSpeed — all_to_all_v_c Variable-Count MoE Communication Optimization](sources/prs/mindspeed/PR-2828.md) conf:source-reported arch:ascend910, ascend910b
- [sgl-kernel-npu — DeepEP Low-Latency Alltoall (dispatch/combine) on NPU](sources/prs/sgl-kernel-npu/PR-004.md) conf:? arch:ascend910b
- [sgl-kernel-npu — DeepEP Low-Latency CCU Offload Path](sources/prs/sgl-kernel-npu/PR-478.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Default MoE w2_weight to NZ Format](sources/prs/vllm-ascend/PR-002.md) conf:? arch:ascend910b
- [vllm-ascend — W8A8FP8 Dynamic Quantization on Ascend 950](sources/prs/vllm-ascend/PR-004.md) conf:? arch:ascend910b
- [vllm-ascend — DeepSeek-V4 Support for Ascend 950](sources/prs/vllm-ascend/PR-9757.md) conf:source-reported arch:ascend910b
- [GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues](wiki/techniques/ascend-gmm-fusion-epilogues.md) conf:inferred arch:ascend910, ascend910b
- [DeepSeek-V4 on Ascend 950 — Compressed Attention Runtime Adaptation](wiki/techniques/deepseek-v4-ascend950-runtime.md) conf:inferred arch:ascend910b
- [HCCL Collective Communication Optimization](wiki/techniques/hccl-optimization.md) conf:inferred arch:ascend910, ascend910b
- [MindSpeed MoE Training Communication — P2P, All-to-All Overlap, and Token Permute Fusion](wiki/techniques/mindspeed-moe-training-communication.md) conf:inferred arch:ascend910, ascend910b
- [SGL DeepEP MoE Communication — Strategy, All-to-All, CCU, and MXFP8](wiki/techniques/sgl-deepep-moe-communication.md) conf:inferred arch:ascend910, ascend910b
- [Tensor Parallelism — Communication/Compute Overlap with HCCL](wiki/techniques/tensor-parallel-overlap.md) conf:source-reported arch:ascend910b
- [Training Communication Scheduling for MoE and Param-Gather Overlap](wiki/techniques/training-communication-scheduling-overlap.md) conf:source-reported arch:ascend910, ascend910b

## paged-attention (13 pages)

- [CANN Ops Adv — Incremental Flash Attention](src/transformer/incre_flash_attention) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Block Sparse Attention Operator](csrc/attentions/csrc/ops/block_sparse_attention) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Attention Backend](vllm_ascend/attention) conf:source-reported arch:ascend910b
- [vLLM Ascend KV Quant Sparse Attention Operator](csrc/attention/kv_quant_sparse_attn_sharedkv) conf:source-reported arch:ascend910b
- [vLLM Ascend Sparse Flash Attention Operator](csrc/attention/sparse_flash_attention) conf:source-reported arch:ascend910b
- [KV Block Semantic Drift — Physical, Compressed, SWA, and Hybrid Blocks Mixed](wiki/patterns/kv-block-semantic-drift.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — D-side Partial-Group Caching for Hybrid Mamba Models](sources/prs/vllm-ascend/PR-10009.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Layerwise KV Pooling for AscendStore](sources/prs/vllm-ascend/PR-10077.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Mooncake PP Layer Index and MTP Block Flattening Fix](sources/prs/vllm-ascend/PR-10202.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — AscendStore Grouped Hash Lookup Encoding Alignment](sources/prs/vllm-ascend/PR-10217.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — Mooncake Connector Support for DeepSeek-V4 Hybrid KV](sources/prs/vllm-ascend/PR-10342.md) conf:source-reported arch:ascend910, ascend910b
- [vllm-ascend — AscendStore Hybrid/Mamba Aligned Prefix Cache](sources/prs/vllm-ascend/PR-9533.md) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Hybrid/Mamba KV Cache — Group-Aware Transfer and Prefix Caching](wiki/techniques/vllm-hybrid-mamba-kv-cache.md) conf:inferred arch:ascend910, ascend910b

## quant-matmul (8 pages)

- [CANN Ops Adv — Matmul Operators](src/matmul) conf:source-reported arch:ascend910, ascend910b
- [CATLASS FP8 Matmul Example](examples/29_a2_fp8_e4m3_matmul) conf:source-reported arch:ascend910b
- [CATLASS Quantized Matmul Example](examples/12_quant_matmul) conf:source-reported arch:ascend910b
- [CATLASS W8A16 Matmul Example](examples/30_w8a16_matmul) conf:source-reported arch:ascend910b
- [SGL Kernel NPU CATLASS Utility Kernels](csrc/catlass) conf:source-reported arch:ascend910, ascend910b
- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [vLLM Ascend KV Quant Sparse Attention Operator](csrc/attention/kv_quant_sparse_attn_sharedkv) conf:source-reported arch:ascend910b
- [GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues](wiki/techniques/ascend-gmm-fusion-epilogues.md) conf:inferred arch:ascend910, ascend910b

## reduce (8 pages)

- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [CATLASS Split-K Matmul Example](examples/09_splitk_matmul) conf:source-reported arch:ascend910b
- [SGL Kernel NPU Sparse Block Estimate Operator](csrc/attentions/csrc/ops/sparse_block_estimate) conf:source-reported arch:ascend910, ascend910b
- [Reduction Operations (ReduceSum/ReduceMax) on Ascend NPU](wiki/kernels/reduction-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC Top-K — Expert Routing and Sampling Reduction](wiki/kernels/topk-ascendc.md) conf:inferred arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [sgl-kernel-npu — Fused GDN Gating + solve_tril Performance](sources/prs/sgl-kernel-npu/PR-003.md) conf:? arch:ascend910, ascend910b
- [Atomic Accumulation — Split-K and Cross-Core Reduction to Global Memory](wiki/techniques/atomic-accumulation.md) conf:inferred arch:ascend910b

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

## softmax (21 pages)

- [TIK Operator Walkthrough — Writing Vector Add and Softmax in Python](sources/blogs/tik-operator-walkthrough.md) conf:source-reported arch:ascend910, ascend910b
- [Ascend Samples — aclnn Single-Operator Invocation](operator/aclnn) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [Ascend Samples — AscendC Operator Examples](operator/ascendc) conf:source-reported arch:ascend910, ascend910b, ascend310p
- [SGL Kernel NPU Native Source](csrc) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Python Package](python) conf:source-reported arch:ascend910, ascend910b
- [SGL Kernel NPU Tests](tests) conf:source-reported arch:ascend910, ascend910b
- [CATLASS Flash Attention Grad TND — Backward Attention Case Study](wiki/kernels/flash-attention-grad-tnd-catlass.md) conf:inferred arch:ascend910, ascend910b
- [Flash Attention Infer in CATLASS](wiki/kernels/flash-attention-infer-catlass.md) conf:source-reported arch:ascend910, ascend910b
- [AscendC Softmax — Vector Unit Implementation](wiki/kernels/softmax-ascendc.md) conf:source-reported arch:ascend910, ascend910b
- [Online Softmax Wait Boundary — Tail Row Synchronization Drift](wiki/patterns/online-softmax-wait-boundary.md) conf:source-reported arch:ascend910, ascend910b
- [PyTorch Ascend Backend — Custom Operator Integration](sources/prs/ascend-pytorch/PR-001.md) conf:? arch:ascend910, ascend910b
- [CANN Sample Code — Reference AscendC Implementations](sources/prs/ascend-samples/PR-001.md) conf:? arch:ascend910, ascend910b, ascend310p
- [CATLASS — Flash Attention Grad TND Example and Block Components](sources/prs/catlass/PR-169.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Flash Attention Infer Base Implementation](sources/prs/catlass/PR-200.md) conf:source-reported arch:ascend910, ascend910b
- [CATLASS — Online Softmax RowNum=1 Wait Boundary Fix](sources/prs/catlass/PR-237.md) conf:source-reported arch:ascend910, ascend910b
- [SGLang NPU Kernel — Ascend Backend Support](sources/prs/sgl-kernel-npu/PR-001.md) conf:? arch:ascend910, ascend910b
- [UB Bank Conflict Avoidance](wiki/techniques/bank-conflict-avoidance.md) conf:inferred arch:ascend910, ascend910b
- [Cube/Vector Overlap — Exploiting Independent Instruction Queues](wiki/techniques/cube-vector-overlap.md) conf:inferred arch:ascend910, ascend910b
- [UB Data Reuse — Minimizing GM Bandwidth Pressure](wiki/techniques/data-reuse.md) conf:source-reported arch:ascend910, ascend910b
- [Online Softmax — Numerically Stable Streaming Softmax for Flash Attention](wiki/techniques/online-softmax.md) conf:source-reported arch:ascend910, ascend910b
- [Pipeline Scheduling — CopyIn/Compute/CopyOut Queue Coordination](wiki/techniques/pipeline-scheduling.md) conf:source-reported arch:ascend910, ascend910b

## swiglu (2 pages)

- [vLLM Ascend Grouped Matmul SwiGLU Quant Operator](csrc/gmm/grouped_matmul_swiglu_quant) conf:source-reported arch:ascend910b
- [AscendC FFN Fused Kernel — Dual GEMM + Activation](wiki/kernels/ffn-fused-ascendc.md) conf:source-reported arch:ascend910b