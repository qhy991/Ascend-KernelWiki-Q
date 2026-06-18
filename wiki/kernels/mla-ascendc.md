---
id: kernel-mla-ascendc
title: "Multi-Head Latent Attention (AscendC)"
type: wiki-kernel
architectures:
  - ascend910b
tags:
  - llm
  - inference
  - deepseek
confidence: inferred
kernel_types:
  - attention
languages:
  - ascendc
sources: []
---

# Multi-Head Latent Attention (AscendC)

Multi-Head Latent Attention (MLA), popularized by the DeepSeek-V2 and V3 architectures, drastically reduces KV cache memory consumption by projecting Key and Value states into a low-dimensional latent space. However, mapping this to hardware requires careful consideration of the RoPE (Rotary Position Embedding) decoupling and the projection steps.

## The MLA Challenge

In standard Multi-Head Attention (MHA) or Grouped-Query Attention (GQA), the KV cache stores materialized $K$ and $V$ tensors per head. In MLA:
1. The cache stores a single compressed latent vector $C_t$ per token.
2. During attention, $C_t$ must be up-projected to $K$ and $V$ using weight matrices $W_{UK}$ and $W_{UV}$.
3. RoPE is decoupled: A separate, uncompressed token embedding $R_t$ is stored and appended to the queries and keys.

This means reading from the KV cache now involves a **Gather + GEMM (Up-Projection)** before the standard Attention `Q @ K^T` can occur.

## Ascend Mapping Strategy

On the Ascend 910B, MLA optimization focuses on overlapping the up-projection on the Cube Unit with the gathering of latent vectors by the Memory Transfer Engine (MTE).

### 1. Unified Buffer Layout
Instead of loading $K$ and $V$ blocks from Global Memory (GM), the MTE loads the latent blocks $C_{blk}$ and the decoupled RoPE blocks $R_{blk}$.
The projection weights $W_{UK}$ and $W_{UV}$ are kept stationary in the L1 Buffer or L0A buffer, as they are constant across all tokens.

### 2. Pipelined Execution
The TPipe scheduling must introduce a new stage:
- **Stage 1 (MTE2)**: Load latent block $C_{blk}$ into UB, move to L0B.
- **Stage 2 (Cube)**: Compute $K_{blk} = C_{blk} @ W_{UK}$ and $V_{blk} = C_{blk} @ W_{UV}$. This is extremely efficient on the Cube unit.
- **Stage 3 (Vector)**: Apply decoupled RoPE to the newly generated $K_{blk}$.
- **Stage 4 (Cube)**: Perform standard Flash Attention $S = Q @ K_{blk}^T$.
- **Stage 5 (Vector)**: Online Softmax and scaling.
- **Stage 6 (Cube)**: $O = P @ V_{blk}$.

### 3. Fusing Projections
To maximize Cube utilization, $W_{UK}$ and $W_{UV}$ can be concatenated into a single weight matrix $W_{UKV}$. A single `Matmul` operation on the Cube unit generates both $K$ and $V$ simultaneously, saving instruction dispatch overhead.

## Real-World Integration: vLLM-Ascend

When running DeepSeek-V2/V3 via the `vllm-ascend` plugin on Ascend 910B NPUs, developers must be aware of **Graph Mode** constraints related to MLA:
- **Head Ratio Restrictions**: The Ascend NPU Graph Mode currently requires the ratio of `num_heads / num_kv_heads` to be one of `{32, 64, 128}` for optimized attention kernels.
- **DeepSeek-V2-Lite Issue**: Because the "Lite" version of the model uses 16 attention heads, it does not fit this ratio. Attempting to run it in Graph Mode will throw an error.
- **Workaround**: For unsupported head configurations, you must fall back to **Eager Mode** by setting the environment variable `VLLM_NPU_GRAPH_MODE=0` to ensure stability, albeit with some dispatch overhead.
