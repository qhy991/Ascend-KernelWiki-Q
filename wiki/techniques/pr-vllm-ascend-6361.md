---
id: technique-pr-vllm-ascend-6361
title: "PR Insight: vllm-project/vllm-ascend #6361"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - moe
  - shared-experts
  - tensor-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6361"
---

# PR Insight: vllm-project/vllm-ascend #6361

**Title:** [BugFix] Disable enable_shared_expert_dp by default if tensor_parallel_size=1

## Overview
This PR disables the `enable_shared_expert_dp` configuration option by default when `tensor_parallel_size=1` in `vllm_ascend/ascend_config.py`, preventing unnecessary complexity in single-card MoE inference.

## Technical Significance
Shared expert data parallelism is only beneficial in multi-card scenarios. Enabling it by default for single-card inference adds unnecessary overhead. This fix ensures optimal default configuration based on tensor parallel size.

## Related
- `technique-moe`
- `technique-shared-experts`
- `technique-tensor-parallel`