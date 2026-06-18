---
id: technique-pr-mindspeed-2279
title: "PR Insight: Ascend/MindSpeed #2279"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - pp
  - megatron
  - bugfix
  - args
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2279"
---

# PR Insight: Ascend/MindSpeed #2279

**Title:** bugfix: 修复pp和megatron_basic获取args参数的错误

## Overview
This PR fixes an error in argument handling for Pipeline Parallelism (PP) and Megatron basic configurations. The fix addresses how arguments are retrieved and passed in these parallel training modes.

## Technical Significance
Argument handling errors can cause misconfigurations or crashes during distributed training. PP and Megatron are critical distributed training strategies, and proper argument passing is essential for correct parallel execution. This fix ensures these modes work as intended with proper parameter configurations.

## Related
- `technique-pipeline-scheduling`
- `technique-megatron-parallelism`
- `pattern-configuration-management`