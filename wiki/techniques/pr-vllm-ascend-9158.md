---
id: technique-pr-vllm-ascend-9158
title: "PR Insight: vllm-project/vllm-ascend #9158"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - eagle
  - mtp
  - bugfix
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9158"
---

# PR Insight: vllm-project/vllm-ascend #9158

**Title:** [Ascend950][BugFix] Fix eagle3 speculative decode: use use_eagle() to cover eagle/eagle3/mtp methods

## Overview
This PR fixes a dimension mismatch issue in eagle3 speculative decoding on Ascend NPUs. The sequence length alignment logic in `AscendMLAImpl` previously only checked for the "mtp" method. By replacing this check with `speculative_config.use_eagle()`, the logic now correctly applies to all eagle-family methods (eagle, eagle3, and mtp).

## Technical Significance
The fix ensures proper handling of `seq_lens_list` padding and `actual_seq_lengths` calculation across all eagle-family speculative decoding methods. This prevents dimension mismatch errors and corrects attention state management during speculative decoding workflows, improving reliability for models using eagle, eagle3, or mtp speculative decoding approaches.

## Related
- `technique-speculative-decoding`, `kernel-attention-ascendc`, `kernel-mla-ascendc`