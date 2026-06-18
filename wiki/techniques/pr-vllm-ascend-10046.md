---
id: technique-pr-vllm-ascend-10046
title: "PR Insight: vllm-project/vllm-ascend #10046"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - data-parallel
  - metadata
  - all-reduce
  - communication
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10046"
---

# PR Insight: vllm-project/vllm-ascend #10046

**Title:** [BugFix] Add env var to control DP metadata all_reduce communication

## Overview
This PR adds an environment variable to control data parallel metadata all_reduce communication. It provides flexibility in managing when and how metadata is synchronized across data parallel ranks.

## Technical Significance
Adds configurability to data parallel metadata synchronization via environment variable. Allows fine-tuning of all_reduce behavior for DP metadata, enabling optimization for different deployment scenarios and communication patterns.

## Related
- `technique-data-parallel`, `technique-hccl-optimization`, `pattern-configuration`