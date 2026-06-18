---
id: technique-pr-modellink-2309
title: "PR Insight: Ascend/ModelLink #2309"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - evaluation
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2309"
---

# PR Insight: Ascend/ModelLink #2309

**Title:** 优化大集群moe模型评估

## Overview
This PR optimizes MoE model evaluation workflows for large-scale Ascend clusters. The improvements address performance and scalability challenges when evaluating Mixture-of-Experts models across many nodes.

## Technical Significance
Evaluating MoE models on large clusters requires efficient communication patterns for expert routing and load balancing. The optimization likely improves all-to-all communication for expert selection, reduces synchronization overhead, and optimizes memory access patterns for scattered expert parameters. These improvements enable faster evaluation cycles for large MoE models like DeepSeekV3 and HunyuanLargeMoE on production Ascend clusters.

## Related
- `technique-moe-training`
- `technique-hccl-optimization`
- `technique-alltoall`