---
id: technique-pr-vllm-ascend-4913
title: "PR Insight: vllm-project/vllm-ascend #4913"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sfa
  - cp
  - communication-domain
  - mtp
  - pp
  - weight-load
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4913"
---

# PR Insight: vllm-project/vllm-ascend #4913

**Title:** [Bugfix] Fix the bug in initializing the shared_weight communication domain in sfa-cp, and fix the mtp weight load in pp>1 situation

## Overview
This PR fixes two bugs: (1) a bug in PR #4188 where sfa-cp couldn't find the global_pp_size parameter during initialization of the shared_weight communication domain, and (2) MTP weight loading issues when pipeline parallelism > 1.

## Technical Significance
Fixes SFA-CP initialization for shared weight communication and ensures MTP weights load correctly in multi-stage pipelines. This enables proper weight synchronization in SFA context parallelism and MTP speculative decoding with pipeline parallelism.

## Related
- `kernel-sfa`
- `technique-context-parallelism`
- `technique-pipeline-parallelism`
- `technique-mtp`
- `technique-weight-loading`