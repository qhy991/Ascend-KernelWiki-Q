---
id: technique-pr-vllm-ascend-1131
title: "PR Insight: vllm-project/vllm-ascend #1131"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - nz-format
  - nd-format
  - format-conversion
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1131"
---

# PR Insight: vllm-project/vllm-ascend #1131

**Title:** Waiting for BMM NZ support(Improve TPOP 2ms performance)

## Overview
This PR improves performance by avoiding unnecessary NZ format conversions. The issue was that W_UV and W_UK_T weights were being converted to NZ format but then immediately converted back to ND format because the fused TransposeBatchMatmul operation doesn't support NZ format. By removing these redundant conversions, the PR achieves a 2ms improvement in TPOT (Time Per Output Token).

## Technical Significance
This optimization eliminates wasteful format conversions that were hurting performance in DeepSeek attention operations. The fix demonstrates the importance of matching operator format requirements to avoid unnecessary data transformations, achieving a measurable 2.21ms TPOT improvement (90.79ms → 88.58ms) in production scenarios.

## Related
- `technique-nz-format`
- `technique-nd-format`
- `technique-format-conversion`
- `technique-deepseek`