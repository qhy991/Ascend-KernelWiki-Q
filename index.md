# Ascend-KernelWiki-Q — Index

> Knowledge base for Huawei Ascend NPU kernel optimization (212 pages, spanning AscendC, TIK (Python), aclnn & AscendCL (C/C++), PyTorch `torch_npu`, MindSpore, and CATLASS)

## Quick Links

### Hardware Features
- [Cube Unit (Matrix Multiply)](wiki/hardware/cube-unit.md) — Tensor Core equivalent
- [Vector Unit (SIMD)](wiki/hardware/vector-unit.md) — CUDA Core equivalent
- [Unified Buffer](wiki/hardware/unified-buffer.md) — Shared Memory equivalent
- [Memory Hierarchy](wiki/hardware/memory-hierarchy.md) — GM → L1 → UB → L0
- [Instruction Queues](wiki/hardware/instruction-queue.md) — 4-queue pipeline
- [Ascend 910B Architecture Evolution](wiki/hardware/ascend-910b-evolution.md) — Evolution from 910A to 910B/C
- [Hardware Synchronization Primitives](wiki/hardware/sync-primitives.md) — Barriers and EVENT management
- [MTE — Memory Transfer Engine](wiki/hardware/mte.md) — Async DMA, TMA equivalent
- [Scalar Unit](wiki/hardware/scalar-unit.md) — Control flow + address generation
- [FRACTAL_NZ Format](wiki/hardware/nz-format.md) — Cube unit's 5D tiled layout
- [L1 / L0 Buffers](wiki/hardware/l1-l0-buffer.md) — Cube staging hierarchy
- [HCCS Interconnect](wiki/hardware/hccs.md) — NVLink equivalent

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
- [Tiling Strategy](wiki/techniques/tiling-strategy.md) — Host-side + auto tiling
- [Online Softmax](wiki/techniques/online-softmax.md) — Streaming stable softmax (flash attn)
- [Atomic Accumulation](wiki/techniques/atomic-accumulation.md) — Split-K / cross-core reduce
- [Workspace Management](wiki/techniques/workspace-management.md) — UB budgeting + GM scratch
- [KV Cache Paging](wiki/techniques/kv-cache-paging.md) — Block-table inference memory
- [Tensor Parallel Overlap](wiki/techniques/tensor-parallel-overlap.md) — HCCL/compute overlap
- [INT8 Quantization (W8A8)](wiki/techniques/quantization-int8.md) — Per-token / per-channel

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
- [Multi-Head Latent Attention (AscendC)](wiki/kernels/mla-ascendc.md) — DeepSeek specific optimizations
- [Ring Attention (AscendC)](wiki/kernels/ring-attention-ascendc.md) — Context parallelism and HCCL overlap
- [RMSNorm (AscendC)](wiki/kernels/rmsnorm-ascendc.md) — Fused vector normalization
- [RoPE (AscendC)](wiki/kernels/rope-ascendc.md) — Rotary position embedding
- [Paged Attention (NPU)](wiki/kernels/paged-attention-npu.md) — Block KV-cache attention
- [Quant Matmul (W8A8)](wiki/kernels/quant-matmul-ascendc.md) — INT8 `npu_quant_matmul`
- [SwiGLU (AscendC)](wiki/kernels/swiglu-ascendc.md) — Fused gated activation
- [Top-K (AscendC)](wiki/kernels/topk-ascendc.md) — MoE routing / sampling
- [Vector Add (TIK / Python)](wiki/kernels/add-tik.md) — Elementwise add in TIK
- [Vector Add (aclnn / C++)](wiki/kernels/vector-add-aclnn.md) — Single-operator invocation
- [GEMM (CATLASS / C++)](wiki/kernels/gemm-catlass-cpp.md) — Template matmul on Cube

### Problem Diagnosis
- [Memory-Bound Kernel](wiki/patterns/memory-bound.md) — Diagnosis → solutions
- [Low Cube Utilization](wiki/patterns/low-cube-utilization.md) — Diagnosis → solutions
- [NZ Format Traps](wiki/patterns/nz-format-traps.md) — Common pitfalls + fixes
- [Pipeline Stall](wiki/patterns/pipeline-stall.md) — Queue dependency bottleneck
- [UB OOM (Unified Buffer Overflow)](wiki/patterns/ub-oom.md) — Out of memory diagnosis
- [Precision Loss & NaN Debugging](wiki/patterns/precision-nan-debugging.md) — Overflow/underflow troubleshooting
- [MTE Saturation](wiki/patterns/mte-saturation.md) — DMA bottleneck diagnosis
- [Scalar Unit Bottleneck](wiki/patterns/scalar-bottleneck.md) — Pipeline stalling from scalar unit
- [Host-Dispatch-Bound](wiki/patterns/host-dispatch-bound.md) — Launch overhead dominates
- [Format-Conversion Overhead](wiki/patterns/format-conversion-overhead.md) — Excess ND↔NZ transposes
- [Tiling Too Small](wiki/patterns/tiling-too-small.md) — Under-utilized Cube / MTE

### Programming Guides (by language)
- [AscendC Guide](wiki/languages/ascendc-guide.md) — C/C++ kernel programming tutorial
- [TBE-DSL Guide](wiki/languages/tbe-dsl-guide.md) — Deprecated Python DSL
- [TIK Guide](wiki/languages/tik-guide.md) — Low-level Python kernel DSL
- [aclnn C++ Guide](wiki/languages/aclnn-cpp-guide.md) — Single-operator API (two-phase)
- [AscendCL Host Guide](wiki/languages/ascendcl-host-guide.md) — Host runtime (C/C++ & pyACL)
- [PyTorch (torch_npu) Guide](wiki/languages/pytorch-npu-guide.md) — PyTorch on Ascend
- [MindSpore Ascend Guide](wiki/languages/mindspore-ascend-guide.md) — AOT AscendC custom ops
- [Triton Ascend Guide](wiki/languages/triton-ascend-guide.md) — Triton on Ascend

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
- [CUDA Runtime → AscendCL](wiki/migration/cuda-runtime-to-acl.md) — Streams / events / device memory
- [cuBLAS / cuDNN → aclnn](wiki/migration/cublas-to-aclnn.md) — Library-call operator migration
- [PyTorch CUDA → NPU](wiki/migration/pytorch-cuda-to-npu.md) — `torch.cuda` → `torch_npu`

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

### Ecosystem Sources (languages & frameworks)
- [vLLM Ascend Backend](sources/docs/vllm-ascend.md) — NPU inference plugin (paged attention)
- [aclnn Operator API](sources/docs/aclnn-operator-api.md) — Two-phase single-operator interface
- [AscendCL Runtime](sources/docs/ascendcl-runtime.md) — Host runtime (streams/memory/events)
- [Ascend C Tiling API](sources/docs/ascendc-tiling-api.md) — Host-side TilingData
- [TIK API Reference](sources/docs/tik-api-reference.md) — Low-level Python operator API
- [torch_npu Adapter](sources/docs/torch-npu-adapter.md) — PyTorch Ascend backend
- [MindSpore AscendC Custom Op](sources/docs/mindspore-ascendc-custom-op.md) — AOT custom operators
- [W8A8 Quantization](sources/blogs/ascend-w8a8-quantization.md) — INT8 inference on 910B
- [CATLASS GEMM Templates](sources/blogs/catlass-gemm-templates.md) — CUTLASS-style C++ GEMM
- [vllm-ascend Custom Kernels (PR)](sources/prs/vllm-ascend/PR-001.md) — AscendC rotary_embedding

## Query Indices
- [By Hardware Feature](queries/by-hardware-feature.md)
- [By Technique](queries/by-technique.md)
- [By Kernel Type](queries/by-kernel-type.md)
- [By Language](queries/by-language.md)
- [By Problem](queries/by-problem.md)
