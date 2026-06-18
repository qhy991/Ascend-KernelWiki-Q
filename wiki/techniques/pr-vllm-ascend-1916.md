---
id: technique-pr-vllm-ascend-1916
title: "PR Insight: vllm-project/vllm-ascend #1916"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - super-kernel
  - torchair
  - multistream
  - operator-fusion
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1916"
---

# PR Insight: vllm-project/vllm-ascend #1916

**Title:** add super kernel in decode moe

## Overview
This PR adds super kernel support for decode-stage MoE, which fuses multiple operators together to reduce device scheduling overhead. The super kernel feature is only valid when both torchair graph mode and enable_multistream_moe are enabled.

## Technical Significance
Operator fusion optimization for MoE decode. Super kernels reduce the number of kernel launches and improve data locality by fusing related MoE operations, particularly beneficial in graph mode with multistream enabled.

## Related
- `kernel-moe-ascendc`
- `technique-super-kernel`
- `technique-operator-fusion`
- `technique-torchair-graph`