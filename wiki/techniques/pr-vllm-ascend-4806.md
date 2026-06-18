---
id: technique-pr-vllm-ascend-4806
title: "PR Insight: vllm-project/vllm-ascend #4806"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - prefill
  - revert
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4806"
---

# PR Insight: vllm-project/vllm-ascend #4806

**Title:** Revert "[Kernel] add custom MoE ops for prefill"

## Overview
This PR reverts the changes from PR #4194 which added custom MoE operations for prefill, as it broke CI tests. The revert removes the dispatch_layout, moe_combine_normal, moe_dispatch_normal, and notify_dispatch operators that were previously added.

## Technical Significance
Rollback of custom MoE prefill operators due to CI failures. Indicates that the AscendC MoE operations for prefill stage had issues that need to be resolved before re-introduction.

## Related
- `kernel-moe-combine-normal`
- `kernel-moe-dispatch-normal`
- `kernel-dispatch-layout`
- `kernel-moe-prefill`