---
id: technique-pr-vllm-ascend-3620
title: "PR Insight: vllm-project/vllm-ascend #3620"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - quantization
  - deepseek
  - patch
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3620"
---

# PR Insight: vllm-project/vllm-ascend #3620

**Title:** [BugFix][main] Fix quantization related mtp bug with patch

## Overview
This is the main branch version of the quantization-related MTP bug fix, applying the same patch for the missing SharedHead prefix in vLLM's deepseek_mtp. The fix adds 54 lines to `vllm_ascend/patch/worker/patch_deepseek_mtp.py` and initializes the patch system, enabling main branch to support vLLM v0.11.0.

## Technical Significance
This duplicate fix of #3619 for the main branch ensures consistency across release branches. Patches are essential for maintaining compatibility with upstream vLLM versions while providing Ascend-specific optimizations and bug fixes that haven't yet been merged upstream.

## Related
- `technique-mtp`
- `technique-quantization`
- `technique-patch-management`