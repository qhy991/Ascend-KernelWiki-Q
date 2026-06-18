---
id: technique-pr-mindspeed-2651
title: "PR Insight: Ascend/MindSpeed #2651"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - bugfix
  - megatron
  - precision
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2651"
---

# PR Insight: Ascend/MindSpeed #2651

**Title:** [mindspore][bugfix][master]megatron0.12 precision alignment modification

## Overview
This PR modifies precision alignment settings for Megatron 0.12 integration with MindSpore. The changes ensure proper handling of mixed-precision training (FP16/BF16) and tensor dtypes across the framework boundaries.

## Technical Significance
Precision alignment is critical for numerical stability and performance in mixed-precision training. This fix ensures that dtype conversions between MindSpeed, Megatron 0.12, and MindSpore are handled correctly, preventing precision loss, overflow, or underflow issues during training.

## Related