---
id: technique-pr-vllm-ascend-9389
title: "PR Insight: vllm-project/vllm-ascend #9389"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - a2
  - deepseek-v4
  - moe
  - all-reduce
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9389"
---

# PR Insight: vllm-project/vllm-ascend #9389

**Title:** [BugFix][A2]Avoid duplicate MoE all-reduce for DeepSeek V4 tensor outputs

## Overview
This PR fixes an issue where duplicate MoE all-reduce operations were being performed for DeepSeek V4 tensor outputs on A2 hardware. The fix is implemented in the DeepSeek V4 model implementation to eliminate redundant collective communication operations.

## Technical Significance
Duplicate all-reduce operations waste network bandwidth and increase latency, particularly problematic in multi-device deployments. Eliminating redundant communication improves overall inference throughput and reduces resource contention on the interconnect.

## Related
- `technique-hccl-optimization`
- `kernel-moe`