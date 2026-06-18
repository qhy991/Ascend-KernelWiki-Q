---
id: technique-pr-vllm-ascend-8209
title: "PR Insight: vllm-project/vllm-ascend #8209"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decoding
  - eagle
  - bugfix
  - mrv2
  - gumbel-sample
  - runtime-error
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8209"
---

# PR Insight: vllm-project/vllm-ascend #8209

**Title:** [MRV2][Spec Decoding][BugFix] fix mrv2 runtime error with speculative decoding

## Overview
This PR fixes a runtime error in MRV2 (Model Runner V2) when using speculative decoding with Eagle. The issue occurred because the `gumbel_sample` function override was removed in a previous PR (#8155), causing the speculator module to incorrectly use the upstream implementation instead of the Ascend-specific version. The fix restores the Ascend-specific override in the patch_triton.py file.

## Technical Significance
This fix ensures correct speculative decoding behavior on Ascend hardware by maintaining the NPU-optimized implementation of sampling operations. The gumbel_sample function is critical for proper draft token generation in speculative decoding, and using the GPU-optimized version would cause runtime errors and incorrect behavior. The PR highlights the importance of maintaining device-specific overrides during refactoring.

## Related
- `technique-speculative-decoding`
- `technique-sampling-optimization`
- `technique-eagle`