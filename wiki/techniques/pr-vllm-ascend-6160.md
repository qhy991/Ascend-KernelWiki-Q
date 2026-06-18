---
id: technique-pr-vllm-ascend-6160
title: "PR Insight: vllm-project/vllm-ascend #6160"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - configuration
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6160"
---

# PR Insight: vllm-project/vllm-ascend #6160

**Title:** [EPLB][Bugfix] Do not refresh parameters when eplb_config is not passed

## Overview
This PR fixes an EPLB configuration bug where parameters were refreshed even when eplb_config was not provided. The fix ensures other configurations take effect without the eplb_config dict, and only refreshes when eplb_config is explicitly passed. Additionally fixes MTP Processor CI tests.

## Technical Significance
EPLB (Expert Parallel Load Balancing) configuration management needs to handle optional configuration gracefully. The previous behavior of refreshing parameters even without explicit configuration could cause unintended side effects. This fix ensures configuration changes only apply when explicitly requested, improving configuration robustness for MoE workloads.

## Related
- `technique-moe`, `technique-eplb`, `technique-spec-decode`