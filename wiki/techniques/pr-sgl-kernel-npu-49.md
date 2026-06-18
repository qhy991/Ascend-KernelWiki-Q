---
id: technique-pr-sgl-kernel-npu-49
title: "PR Insight: sgl-project/sgl-kernel-npu #49"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - dispatch
  - bugfix
  - correctness
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/49"
---

# PR Insight: sgl-project/sgl-kernel-npu #49

**Title:** fix dispatch return param recv_count mismatch

## Overview
This PR fixes a parameter mismatch bug where dispatch and low_latency_dispatch return recv_count parameters incorrectly. Updates deep_ep.cpp and deep_ep.hpp to ensure consistent return value handling.

## Technical Significance
Resolves correctness issues in dispatch operations that could cause incorrect routing behavior in MoE inference. The recv_count parameter is critical for tracking token distribution across experts, and mismatches lead to routing failures or incorrect results.

## Related
- technique-moe-routing
- technique-dispatch-correctness
- technique-bug-fix