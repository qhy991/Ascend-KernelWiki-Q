---
id: technique-pr-mindspeed-1681
title: "PR Insight: Ascend/MindSpeed #1681"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - profiling
  - configuration
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1681"
---

# PR Insight: Ascend/MindSpeed #1681

**Title:** --profile-ranks的默认值修改

## Overview
This PR modifies the default value of the --profile-ranks argument. The change affects which ranks are profiled by default during distributed training runs.

## Technical Significance
Default profiling configuration impacts performance analysis overhead and data collection. Changing the default value likely improves the profiling experience by defaulting to a more efficient or informative rank selection strategy on Ascend NPUs.

## Related
- profiling techniques
- distributed training
- performance-optimization