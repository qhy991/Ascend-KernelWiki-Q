---
id: technique-pr-vllm-ascend-2016
title: "PR Insight: vllm-project/vllm-ascend #2016"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - communication
  - fused-moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2016"
---

# PR Insight: vllm-project/vllm-ascend #2016

**Title:** [0.9.1][bugfix] Remove unnecessary reduce_results access in shared_experts.down_proj

## Overview
This PR removes redundant all-reduce logic in the shared_experts.down_proj operation that was introduced in PR #1802. The unnecessary reduce_results access was causing communication overhead without providing benefit.

## Technical Significance
This fix reduces unnecessary communication in MoE inference, improving performance by eliminating redundant all-reduce operations. The cleanup improves code maintainability and ensures that shared experts processing is efficient on Ascend NPUs.

## Related
- `technique-fused-moe`
- `technique-moe`
- `technique-communication`