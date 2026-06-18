---
id: technique-pr-vllm-ascend-10309
title: "PR Insight: vllm-project/vllm-ascend #10309"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - mtp
  - speculative-decoding
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10309"
---

# PR Insight: vllm-project/vllm-ascend #10309

**Title:** [Feature][310p]Qwen3.5 Support MTP and graphmode

## Overview
This PR enables Multi-Token Prediction (MTP) speculative decoding on the Ascend 310P architecture for Qwen3.5 models. It introduces `AscendKVBlockZeroer310` to zero newly allocated KV blocks directly via tensor writes since Triton is not supported on 310P. The PR updates the 310P attention backend to support the SpecDecoding state, adapts the model runner for MTP graph capture/replay, and updates the sampler to use CPU RNG for exponential value generation. Additionally, it adds support for GDN (Gated Down-projection Network) operations specific to 310P.

## Technical Significance
This feature brings MTP speculative decoding to Ascend 310P, which is challenging because 310P lacks Triton support. The solution uses direct tensor writes for KV block zeroing instead of Triton kernels, and adapts the attention backend to work without Triton. The 310P-specific GDN implementation and graph mode support demonstrate how to adapt advanced inference techniques for lower-tier NPU hardware. This enables significant performance improvements for 310P deployments while maintaining compatibility with the MTP framework.

## Related
- `technique-mtp`
- `technique-speculative-decoding`
- `technique-graph-mode`
- `hw-ascend310p`