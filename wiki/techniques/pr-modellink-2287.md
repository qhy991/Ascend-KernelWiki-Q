---
id: technique-pr-modellink-2287
title: "PR Insight: Ascend/ModelLink #2287"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - deepseek3
  - routing
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2287"
---

# PR Insight: Ascend/ModelLink #2287

**Title:** [deepseek3]新增n_group参数以满足不同限制路由场景

## Overview
Adds an n_group parameter for DeepSeek3 to accommodate different routing scenarios with various constraints. This parameter controls group-based routing strategies for the MoE architecture.

## Technical Significance
Enhances DeepSeek3's routing flexibility by supporting group-based expert selection. This allows for more sophisticated load balancing and routing strategies that can adapt to different computational constraints and performance requirements.

## Related
- technique-moe
- technique-hccl-optimization