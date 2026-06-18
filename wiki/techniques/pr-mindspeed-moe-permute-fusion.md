---
id: technique-pr-mindspeed-moe-permute-fusion
title: "PR Insight: Fused MoE Permute"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - training
  - mindspeed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2825"
---

# PR Insight: Fused MoE Permute

**Source:** [MindSpeed PR #2825](https://gitee.com/ascend/MindSpeed/pulls/2825)

Mixture of Experts (MoE) networks spend a massive portion of their compute budget routing tokens. Before computing the expert MLPs, tokens must be gathered ("permuted") to be physically contiguous in memory, and after computation, they must be scattered ("unpermuted") back to their original sequence order.

## The Dispatch Bottleneck
In early training implementations on Ascend, `token_permute` and `token_unpermute` were handled by separate PyTorch/CANN operators. 
- This resulted in multiple read/write trips to the NPU's Global Memory (HBM).
- The host CPU suffered overhead sequentially dispatching these small memory-shuffling kernels.

## Fusing the Permute Operations

This PR introduces the `--moe-permute-fusion` flag to the MindSpeed launcher, which invokes a specialized fused operator within CANN.

### How It Works
Instead of dispatching separate `index_select` and `scatter` kernels, the NPU fuses the logic:
1. The routing matrix (which token goes to which expert) is loaded into the Unified Buffer (UB).
2. As the Expert MatMul finishes computing in the Cube unit, the Vector unit intercepts the output in the UB.
3. The Vector unit immediately applies the reverse permutation map while writing the data directly back to the final HBM destination in a single burst transfer via the DMA Out engine.

**Fallback Mechanism**: The PR notes that if older CANN versions are detected which lack this specific fused interface, developers must explicitly set `--moe-permute-fusion false` to prevent runtime crashes.
