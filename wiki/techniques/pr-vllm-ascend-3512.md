---
id: technique-pr-vllm-ascend-3512
title: "PR Insight: vllm-project/vllm-ascend #3512"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - hccl-optimization
  - aclgraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3512"
---

# PR Insight: vllm-project/vllm-ascend #3512

**Title:** Reapply "[MoE] [Refactor] Remove manual memory cleanup (#3365)" (#3483)

## Overview
1. Replace manual memory cleanup with passing parameter.

## Technical Significance
Re-applies MoE manual memory cleanup removal with improvements to balance memory management.

## Related
- `technique-moe-routing`
- `technique-aclgraph`
