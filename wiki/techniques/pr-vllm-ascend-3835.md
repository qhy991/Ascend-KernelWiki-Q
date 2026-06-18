---
id: technique-pr-vllm-ascend-3835
title: "PR Insight: vllm-project/vllm-ascend #3835"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - p-d
  - kv-producer
  - allreduce
  - prefill
  - disaggregated
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3835"
---

# PR Insight: vllm-project/vllm-ascend #3835

**Title:** [v0.11.0] [P/D] force with_prefill true after allreduce in kv producer

## Overview
This is a cherry-pick of PR #3768 to the v0.11.0 branch, ensuring correct state management in disaggregated inference. It forces `with_prefill` to be true after allreduce operations in the KV producer by modifying the mooncake layerwise connector and model runner.

## Technical Significance
Backporting this P/D synchronization fix ensures v0.11.0 users have correct allreduce-prefill state management, preventing synchronization bugs in production disaggregated inference deployments.

## Related
- `technique-disaggregated-inference`
- `technique-allreduce`
- `technique-prefill`