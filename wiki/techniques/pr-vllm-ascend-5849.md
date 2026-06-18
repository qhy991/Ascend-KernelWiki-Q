---
id: technique-pr-vllm-ascend-5849
title: "PR Insight: vllm-project/vllm-ascend #5849"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v32
  - mtp
  - spec-decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5849"
---

# PR Insight: vllm-project/vllm-ascend #5849

**Title:** [bugfix]support dsv3.2 enable both mtp and full_decode_only

## Overview
This PR fixes a shape error when enabling both MTP (Multi-Token Prediction) and full_decode_only for DeepSeek V3.2 models. After PR #5626 aligned branch logic with the community, an unpad operation was added that transformed positions and num_input_tokens, causing dimension mismatches in the sfa_v1.py operator's cos and sin calculations.

## Technical Significance
The issue stems from unnecessary unpadding. The community's unpad function doesn't have num_input_tokens and positions parameters, but positions were split and num_input_tokens was set to num_actual_tokens. However, attention_v1 doesn't actually use these parameters. The cropping was done to prevent future shape mismatches, but since positions aren't cropped from the source, the unpad operation is unnecessary. Removing it eliminates the shape error while maintaining alignment with the community code.

## Related
- `technique-spec-decode`, `technique-mtp`, `technique-deepseek-v3`