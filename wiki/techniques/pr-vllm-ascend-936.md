---
id: technique-pr-vllm-ascend-936
title: "PR Insight: vllm-project/vllm-ascend #936"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/936"
---

# PR Insight: vllm-project/vllm-ascend #936

**Title:** [V1][0.7.3] Revert the default value of enable_chunked_prefill in add…

## Overview
This PR reverts the default value of `enable_chunked_prefill` to False in additional_scheduler_config for the v0.7.3 version, preventing V0 scheduler failures when V1 scheduling logic is incorrectly activated.

## Technical Significance
Version-specific scheduler configuration ensures backward compatibility. This fix for v0.7.3 prevents the same scheduling logic issue as PR #935, maintaining proper chunked prefill behavior for the v0.7.3 release.

## Related
- `technique-chunked-prefill`
- `kernel-scheduler`
- `v1-engine`