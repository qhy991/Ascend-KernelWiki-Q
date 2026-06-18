---
id: technique-pr-vllm-ascend-935
title: "PR Insight: vllm-project/vllm-ascend #935"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunked-prefill
  - v1-engine
  - scheduler
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/935"
---

# PR Insight: vllm-project/vllm-ascend #935

**Title:** [V1] Revert the default value of enable_chunked_prefill in additional…

## Overview
This PR reverts the default value of `enable_chunked_prefill` to False in additional_scheduler_config to prevent the V0 scheduler from incorrectly using V1 scheduling logic when chunked prefill is forcibly enabled.

## Technical Significance
Proper scheduler configuration is critical for correct engine behavior. The fix ensures that V0 scheduler operates correctly without unintended V1 logic activation, preventing failures and maintaining proper chunked prefill behavior per engine version.

## Related
- `technique-chunked-prefill`
- `kernel-scheduler`
- `v1-engine`