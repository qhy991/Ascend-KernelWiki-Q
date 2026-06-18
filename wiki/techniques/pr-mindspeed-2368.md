---
id: technique-pr-mindspeed-2368
title: "PR Insight: Ascend/MindSpeed #2368"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - allgather
  - moe
  - share-experts
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2368"
---

# PR Insight: Ascend/MindSpeed #2368

**Title:** BugFix: Fix unexpected value of allgather share_experts_output

## Overview
This PR fixes an unexpected value issue in the allgather operation for share_experts_output. This relates to MoE (Mixture of Experts) where expert outputs are shared across devices.

## Technical Significance
Resolves data integrity issues in expert output sharing for MoE models. Correct allgather operations ensure that expert outputs are properly distributed and available to all devices that need them.

## Related
- `technique-moe`
- `technique-hccl-optimization`
- `technique-expert-routing`
- `hw-hccs`