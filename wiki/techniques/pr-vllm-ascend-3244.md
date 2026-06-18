---
id: technique-pr-vllm-ascend-3244
title: "PR Insight: vllm-project/vllm-ascend #3244"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - aclgraph
  - speculative-decoding
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3244"
---

# PR Insight: vllm-project/vllm-ascend #3244

**Title:** [Feat]mtp aclgraph support

## Overview
Currently, MTP Model in deepseek can not be capture in ACLGraph. This PR is use to allow MTP to be captured in ACLGraph mode.

## Technical Significance
Enables ACLGraph compilation mode for Multi-Token Prediction (MTP) in DeepSeek models, allowing graph capture and optimization for speculative decoding on Ascend NPU.

## Related
- `technique-aclgraph`
- `technique-speculative-decoding`
