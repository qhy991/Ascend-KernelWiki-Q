---
id: technique-pr-vllm-ascend-7082
title: "PR Insight: vllm-project/vllm-ascend #7082"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - triton
  - bugfix
  - accuracy
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7082"
---

# PR Insight: vllm-project/vllm-ascend #7082

**Title:** [BugFix] Fix implementation bug of triton rope_siso

## Overview
Fixes a bug in the Triton `rope_siso` implementation where the second half of RoPE results was not being stored. This caused accuracy problems in Neox-style scenarios and undefined behavior overflow in non-Neox-style scenarios. The fix also adds nightly test cases.

## Technical Significance
Corrects critical RoPE implementation bugs that caused accuracy issues and potential memory corruption. The fix ensures proper storage of all RoPE computation results, maintaining correctness across different RoPE style configurations.

## Related
- `technique-rope`, `technique-triton`, `technique-accuracy`, `technique-memory-safety`