---
id: technique-pr-vllm-ascend-2559
title: "PR Insight: vllm-project/vllm-ascend #2559"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - rotary-embedding
  - refactor
  - torchair
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2559"
---

# PR Insight: vllm-project/vllm-ascend #2559

**Title:** [5/N][refactor]add torchair rotary ops

## Overview
This PR refactors torchair-related rotary embedding operations by moving them into a dedicated `torchair/ops/` directory structure. It adds `torchair_rotary_embedding.py` with associated unit tests and updates the torchair model runner and utilities to integrate the new organization.

## Technical Significance
This refactoring improves code organization by consolidating torchair rotary embedding operations into a dedicated module. The reorganization enables cleaner code separation and prepares for subsequent refactoring to remove torchair code outside of the rotary ops directory. This is part 5 of an N-part refactoring series to improve code maintainability in torchair integration.

## Related
- `technique-operator-fusion`
- `technique-refactor`