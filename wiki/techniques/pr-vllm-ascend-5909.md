---
id: technique-pr-vllm-ascend-5909
title: "PR Insight: vllm-project/vllm-ascend #5909"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v32
  - mtp
  - spec-decode
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5909"
---

# PR Insight: vllm-project/vllm-ascend #5909

**Title:** [0.13.0][cherry-pick][bugfix]support dsv3.2 enable both mtp and full_decode_only (#5849)

## Overview
This is a cherry-pick of PR #5849 for the v0.13.0 release branch. It fixes the same shape error when enabling both MTP and full_decode_only for DeepSeek V3.2 models. The issue was caused by unnecessary unpadding that transformed positions and num_input_tokens.

## Technical Significance
This fix ensures the v0.13.0 branch maintains compatibility with DeepSeek V3.2 models using both MTP and full_decode_only modes. The cherry-pick removes the unnecessary unpad operation that was causing shape mismatches in the cos and sin calculations. By maintaining alignment with the community code structure, the fix prevents shape errors while preserving functionality.

## Related
- `technique-pr-vllm-ascend-5849`, `technique-spec-decode`, `technique-mtp`