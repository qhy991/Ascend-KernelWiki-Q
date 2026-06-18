---
id: technique-pr-vllm-ascend-2619
title: "PR Insight: vllm-project/vllm-ascend #2619"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - linear
  - nz-format
  - unquantized
  - format-conversion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2619"
---

# PR Insight: vllm-project/vllm-ascend #2619

**Title:** [Feat] Unquantized linear nz support

## Overview
This PR adds support for FRACTAL_NZ format in unquantized Linear layer operations. When `VLLM_ASCEND_ENABLE_MLP_OPTIMIZE=1` and CANN version is 8.3, the weights of Linear layers are converted from ND format to FRACTAL_NZ format for improved performance.

## Technical Significance
The feature improves Linear layer performance by converting weights to the more efficient FRACTAL_NZ format, which is optimized for Ascend hardware. Previously, unquantized Linear layers used the slower ND format. The format conversion is enabled through environment variable control and CANN version checking, providing better performance for unquantized and skipped ascend scenarios.

## Related
- `technique-nz-format`
- `technique-linear`
- `technique-format-conversion`