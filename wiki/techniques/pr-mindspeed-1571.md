---
id: technique-pr-mindspeed-1571
title: "PR Insight: Ascend/MindSpeed #1571"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1571"
---

# PR Insight: Ascend/MindSpeed #1571

**Title:** 【Fix】【master】修复VPP send recv 掩盖参数校验问题

## Overview
This PR fixes an issue where VPP (Vector Pre-processing or Virtual Parallel Pipeline) send/recv operations were masking or bypassing parameter validation. The fix ensures proper validation is performed and errors are correctly reported.

## Technical Significance
Restores proper error handling and validation for VPP communication operations, preventing silent failures or incorrect behavior in distributed training scenarios. Proper validation is crucial for debugging and ensuring correct execution.

## Related
- `technique-hccl-optimization`
- `pattern-validation`