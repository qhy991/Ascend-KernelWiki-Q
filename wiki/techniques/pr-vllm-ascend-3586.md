---
id: technique-pr-vllm-ascend-3586
title: "PR Insight: vllm-project/vllm-ascend #3586"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - shared-expert
  - deepseek
  - revert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3586"
---

# PR Insight: vllm-project/vllm-ascend #3586

**Title:** Revert "[Feat] Shared expert dp for deepseek and deepseek_mtp (#3495)"

## Overview
This PR reverts the shared expert data parallelism (DP) feature for DeepSeek and DeepSeek-MTP models from commit bf87606932fa66c92a444c2e0187b60be7b576de. The revert affected multiple files including `vllm_ascend/models/layers/mla.py`, `vllm_ascend/ops/register_custom_ops.py`, `vllm_ascend/attention/mla_v1.py`, and test files, removing the shared expert DP implementation.

## Technical Significance
Shared expert DP was intended to optimize MoE inference by parallelizing shared expert computation across data parallel ranks. However, this feature was reverted, likely due to correctness or performance issues. The revert affects MLA (Multi-Head Latent Attention) implementations, layernorm operations, and custom operator registration, indicating deep integration with the MoE execution path.

## Related
- `technique-moe`
- `technique-shared-expert`
- `technique-mla`