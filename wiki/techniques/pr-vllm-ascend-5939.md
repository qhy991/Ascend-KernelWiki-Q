---
id: technique-pr-vllm-ascend-5939
title: "PR Insight: vllm-project/vllm-ascend #5939"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - mtp
  - pcp
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5939"
---

# PR Insight: vllm-project/vllm-ascend #5939

**Title:** [bugfix](CP) Fix and unify the PD request discrimination logic.

## Overview
This PR fixes and unifies the logic for discriminating Prefill vs Decode requests in PCPManager. The update syncs with vLLM community changes from PR #32118, which modified the criteria for judging request types.

## Technical Significance
PCPManager involves multiple calculations of PD request counts. The PR consolidates the related logic and updates the PD request count once per batch, reducing redundant calculations and ensuring consistency. The fix addresses the updated criteria from the vLLM community, ensuring PCPManager correctly categorizes requests. This is critical for proper context parallel behavior with MTP and async scheduling.

## Related
- `technique-context-parallel`, `technique-mtp`, `technique-pd-disaggregation`