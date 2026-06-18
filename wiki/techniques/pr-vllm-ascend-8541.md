---
id: technique-pr-vllm-ascend-8541
title: "PR Insight: vllm-project/vllm-ascend #8541"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pd-separation
  - mtp
  - kv-cache
  - mooncake
  - bugfix
  - tp-imbalance
  - connector
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8541"
---

# PR Insight: vllm-project/vllm-ascend #8541

**Title:** [BugFix] [P/D] [CherryPick] 8540 In scenarios where TP is not equal, the KV cache at the MTP layer is not handled.

## Overview
This PR is a cherry-pick of #8540 to fix the issue where the Mooncake connector does not handle the MTP (Multi-Tensor Parallel) layer KV cache when TP is unbalanced. The fix ensures proper KV cache handling for MTP layers in scenarios with uneven tensor parallelism distribution.

## Technical Significance
This cherry-pick ensures consistency between main and release branches for KV cache handling in MTP scenarios. The fix is critical for correct inference in complex deployment scenarios with unbalanced TP configurations. Maintaining the fix across release branches ensures reliable behavior for users on different vLLM versions.

## Related
- `technique-pd-separation`
- `technique-kv-pooling`
- `technique-tensor-parallel`