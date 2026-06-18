---
id: technique-pr-vllm-ascend-1636
title: "PR Insight: vllm-project/vllm-ascend #1636"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - torchair
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1636"
---

# PR Insight: vllm-project/vllm-ascend #1636

**Title:** [BugFix] Fix max_num_tokens_across_dp calculation bugs in attention_v1_torchair

## Overview
This PR fixes incorrect calculation of `max_num_tokens_across_dp` in TorchAir attention V1, ensuring correct batch sizing.

## Technical Significance
Corrects token counting across data parallel ranks in TorchAir graph mode, preventing buffer overflows and incorrect attention computation. The fix is critical for maintaining correctness in distributed inference with TorchAir optimization.

## Related
- `technique-torchair`
- `kernel-attention`
- `technique-data-parallel`