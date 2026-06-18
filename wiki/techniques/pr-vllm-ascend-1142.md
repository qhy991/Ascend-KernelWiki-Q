---
id: technique-pr-vllm-ascend-1142
title: "PR Insight: vllm-project/vllm-ascend #1142"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - bugfix
  - moe
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1142"
---

# PR Insight: vllm-project/vllm-ascend #1142

**Title:** [fix] fix compatibility for non-EPLB scenarios

## Overview
This PR fixes a compatibility issue introduced in PR #1116 that affected non-EPLB (Expert Parallel Load Balancing) scenarios. The bug in `vllm_ascend/quantization/w8a8_dynamic.py` prevented proper operation when EPLB was not enabled, requiring a fix to conditional logic.

## Technical Significance
This fix ensures that vLLM-Ascend works correctly in both EPLB and non-EPLB configurations, maintaining backward compatibility. The fix is critical for users running quantized MoE models without static expert mapping, ensuring robust operation across different deployment scenarios.

## Related
- `technique-eplb`
- `technique-quantization`
- `technique-moe`