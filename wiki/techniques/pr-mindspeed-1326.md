---
id: technique-pr-mindspeed-1326
title: "PR Insight: Ascend/MindSpeed #1326"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - documentation
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1326"
---

# PR Insight: Ascend/MindSpeed #1326

**Title:** [master]: 增加共享专家资料说明 和 MLA 测试脚本

## Overview
This PR adds documentation for shared experts and MLA (Multi-Head Latent Attention) testing scripts on the master branch. The documentation explains shared expert mechanisms and provides test utilities.

## Technical Significance
Improves documentation and tooling for shared experts in MoE models and MLA testing. Shared experts are an optimization in MoE architectures, and proper documentation helps users understand and implement this feature correctly.

## Related
- `kernel-moe`
- `kernel-attention`