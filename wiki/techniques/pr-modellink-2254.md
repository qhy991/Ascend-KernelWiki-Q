---
id: technique-pr-modellink-2254
title: "PR Insight: Ascend/ModelLink #2254"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - attention
  - mla
  - performance-optimization
  - deepseek3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2254"
---

# PR Insight: Ascend/ModelLink #2254

**Title:** [deepseek3]增加MLA两个性能优化点开关

## Overview
Adds two performance optimization switches for MLA (Multi-Head Latent Attention) in DeepSeek3. These tunable parameters enable or disable specific optimization techniques for MLA attention mechanisms.

## Technical Significance
Performance optimization that provides fine-grained control over MLA execution strategies. The switches allow users to trade off between different optimization techniques based on their specific workload requirements and hardware characteristics.

## Related
- technique-attention
- technique-operator-fusion