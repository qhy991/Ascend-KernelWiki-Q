---
id: technique-pr-sgl-moe-1024
title: "PR Insight: DeepEP 1024-Expert MoE Scaling"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - deepseek
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/515"
---

# PR Insight: DeepEP 1024-Expert MoE Scaling

**Source:** [sgl-kernel-npu PR #515](https://github.com/sgl-project/sgl-kernel-npu/pull/515)

As Mixture-of-Experts (MoE) models scale, the number of experts increases dramatically. While standard models might use 8 or 16 experts, cutting-edge architectures are pushing towards massive expert pools.

## Pushing the Limits on Atlas A3

This PR expands the MoE specifications supported by the DeepEP (Expert Parallelism) `intranode_dispatch` and `combine` kernels, specifically targeting the newer **Atlas A3** hardware limits.

### Expanded Specifications
- **Experts**: Up to **1024** experts per node.
- **Routing**: Support for up to **Top-16** routing (selecting 16 experts per token).
- **Hidden Size**: Support for hidden sizes up to **8192**.

## Technical Implications

To support such massive routing on a single NPU node without blowing up the L1 or Unified Buffer (UB) during the dispatch phase:
1. **Long-Sequence Adaptation**: The kernels were modified to handle extremely long sequences without OOMing the UB. Instead of attempting to sort or permute the entire batch of tokens in one go, the NPU breaks the token permutations into hardware-friendly tiles.
2. **Intra-node Dispatch**: The `intranode_dispatch` logic utilizes the ultra-high-speed HBM bandwidth of the A3 to rapidly scatter token slices to the localized expert matrix shards, ensuring that even with a Top-16 spread across 1024 experts, the dispatch latency remains microseconds.
