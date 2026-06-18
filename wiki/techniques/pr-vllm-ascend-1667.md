---
id: technique-pr-vllm-ascend-1667
title: "PR Insight: vllm-project/vllm-ascend #1667"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - load-balancing
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1667"
---

# PR Insight: vllm-project/vllm-ascend #1667

**Title:** [cherry-pick] static EPLB fix bug, add unit test to v0.9.1-dev

## Overview
This PR cherry-picks static Expert Per-Level Load Balancing (EPLB) bug fixes and unit tests to v0.9.1-dev.

## Technical Significance
Backports EPLB correctness fixes to the development branch, ensuring stable load balancing behavior across release lines. The addition of unit tests prevents regressions in expert load balancing logic.

## Related
- `kernel-moe`
- `technique-load-balancing`