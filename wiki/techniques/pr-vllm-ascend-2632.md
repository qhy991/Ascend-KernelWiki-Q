---
id: technique-pr-vllm-ascend-2632
title: "PR Insight: vllm-project/vllm-ascend #2632"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - torchair
  - bugfix
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2632"
---

# PR Insight: vllm-project/vllm-ascend #2632

**Title:** [V1][BUGFIX][0.10.1] FIX mtp on main branch

## Overview
This PR fixes MTP (Multi-Token Prediction) torchair bugs caused by torchair and MoE refactoring. The fix addresses issues in MTP proposer, torchair fused MoE operations, and adds comprehensive correctness testing for MTP torchair functionality.

## Technical Significance
The bug fix resolves MTP functionality issues introduced by previous refactoring work. Changes include updates to MTP proposer logic, torchair fused MoE operations, and new test coverage (90 lines) for MTP torchair correctness. The fix depends on related PRs for fused MoE fixes and torchair multi-DP support, ensuring proper integration of MTP with refactored components.

## Related
- `technique-mtp`
- `technique-torchair`
- `technique-moe`