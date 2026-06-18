---
id: technique-pr-vllm-ascend-2560
title: "PR Insight: vllm-project/vllm-ascend #2560"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - bugfix
  - custom-op
  - torch-npu
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2560"
---

# PR Insight: vllm-project/vllm-ascend #2560

**Title:** [Bugfix][LoRA][Patch] Fix the LoRA inference bug after upstream vLLM codebase changed

## Overview
This PR fixes a LoRA inference bug caused by upstream vLLM changes. The issue occurred because NPU tensors have both `is_cuda=True` and `is_npu=True` attributes, causing vLLM's `apply_repetition_penalties` function to incorrectly use CUDA custom operators instead of NPU-compatible operations.

## Technical Significance
The fix adds a patch in `vllm_ascend/patch/worker/patch_common/patch_logits.py` that checks for NPU tensors and applies NPU-compatible repetition penalty calculation instead of falling through to CUDA custom ops. This resolves compatibility issues between vLLM's repetition penalty implementation and Ascend NPU's tensor attributes, ensuring correct LoRA inference functionality.

## Related
- `technique-lora`
- `technique-custom-op`