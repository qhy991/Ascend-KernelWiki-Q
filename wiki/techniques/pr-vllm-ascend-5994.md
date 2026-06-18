---
id: technique-pr-vllm-ascend-5994
title: "PR Insight: vllm-project/vllm-ascend #5994"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - mtp
  - async-scheduling
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5994"
---

# PR Insight: vllm-project/vllm-ascend #5994

**Title:** [Bugfix] fix bug of pcp+mtp+async scheduler

## Overview
This PR fixes a service suspension issue when PCP (Prefill-Context Parallel), MTP (Multi-Token Prediction), and async scheduling are enabled together. After sending a curl request, the service would hang due to shape mismatches.

## Technical Significance
The combination of PCP, MTP, and async scheduling creates complex scheduling scenarios. The shape mismatch occurred in metadata calculations when these features interacted. The fix resolves the issue by ensuring proper tensor shape handling across the PCP and MTP workflows with async scheduling. Testing confirms the service can now handle requests without hanging when all three features are enabled.

## Related
- `technique-pcp`, `technique-mtp`, `technique-async-scheduling`