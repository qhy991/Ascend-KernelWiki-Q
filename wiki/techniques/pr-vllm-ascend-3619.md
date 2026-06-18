---
id: technique-pr-vllm-ascend-3619
title: "PR Insight: vllm-project/vllm-ascend #3619"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3619"
---

# PR Insight: vllm-project/vllm-ascend #3619

**Title:** [BugFix][v0.11.0] Fix quantization related mtp bug with patch

## Overview
This PR fixes a quantization-related MTP bug in vLLM 0.11.0 where the prefix for MTP's SharedHead was missing. The fix is implemented via a patch to vLLM's deepseek_mtp, adding 55 lines to `vllm_ascend/patch/worker/patch_deepseek_mtp.py` and initializing the patch system with 15 additional lines.

## Technical Significance
When upstream vLLM changes are not immediately integrated into the Ascend version, patch files are used to apply necessary fixes. This patch addresses a missing SharedHead prefix that likely affected quantized MTP inference, where proper tensor naming and prefix handling are critical for correct weight loading and computation.

## Related
- `technique-mtp`
- `technique-quantization`
- `technique-patch-management`