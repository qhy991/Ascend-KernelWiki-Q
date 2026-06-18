---
id: technique-pr-vllm-ascend-7019
title: "PR Insight: vllm-project/vllm-ascend #7019"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - slot-mapping
  - qwen
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7019"
---

# PR Insight: vllm-project/vllm-ascend #7019

**Title:** [Bugfix] Obtain kernel block size for computing slot mapping correctly

## Overview
Fixes incorrect slot mapping computation in Qwen3.5 models by using `kernel_block_size` instead of incorrect block size. The kernel block size is obtained during model loading when `draft_attn_layers` are available, ensuring correct slot mapping computation.

## Technical Significance
Corrects slot mapping computation for MTP scenarios in Qwen3.5 models by using the proper kernel block size. This fix is essential for accurate memory allocation and KV cache management in speculative decoding.

## Related
- `technique-mtp`, `technique-slot-mapping`, `technique-kv-cache`, `technique-qwen`