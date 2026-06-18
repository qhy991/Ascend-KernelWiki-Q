---
id: technique-pr-modellink-2361
title: "PR Insight: Ascend/ModelLink #2361"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deepseek3
  - vpp
  - weight-conversion
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2361"
---

# PR Insight: Ascend/ModelLink #2361

**Title:** ds3权重转换部分vpp场景下层索引逻辑修正

## Overview
This PR fixes layer index logic during DeepSeekV3 weight conversion for specific VPP (Virtual Pipeline Parallelism) scenarios. The correction ensures proper weight mapping when pipeline parallelism is enabled.

## Technical Significance
VPP introduces virtual stages that partition layers across devices differently than standard pipeline parallelism. The layer index mapping must account for these virtual stage boundaries to ensure each device receives the correct weight tensors. This fix prevents weight mismatches that could cause incorrect model behavior or crashes during distributed training with pipeline parallelism on Ascend hardware.

## Related
- `technique-pipeline-scheduling`
- `technique-weight-conversion`
- `technique-vpp`