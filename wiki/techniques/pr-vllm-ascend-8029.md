---
id: technique-pr-vllm-ascend-8029
title: "PR Insight: vllm-project/vllm-ascend #8029"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - attention
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8029"
---

# PR Insight: vllm-project/vllm-ascend #8029

**Title:** [BugFix] Fix attention state of short prompt for correct forwarding

## Overview
This PR fixes a critical bug where short prompts (with prefill tokens less than or equal to `num_spec_tokens + 1`) were incorrectly classified as decode requests by `split_decodes_and_prefills`. This caused these short prompts to be passed into mismatched attention computation branches, leading to incorrect processing because their `PrefillNoCache` attention state contradicted the decode path assumptions. The fix is implemented in `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
The bug affected attention computation path selection on Ascend NPUs, particularly for the common case of short prompt sequences. The issue could cause incorrect routing through the attention implementation, potentially leading to wrong results or errors. The fix ensures that short prompts maintain their correct prefill attention state rather than being incorrectly demoted to decode paths, maintaining the semantic correctness of the attention computation for variable-length inputs.

## Related
- `kernel-attention` (Attention computation)
- `pattern-batch-routing` (Batch request classification)