---
id: technique-pr-sgl-kernel-npu-33
title: "PR Insight: sgl-project/sgl-kernel-npu #33"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - dispatch
  - combine
  - moe
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/33"
---

# PR Insight: sgl-project/sgl-kernel-npu #33

**Title:** support normal dispatch and combine

## Overview
This PR adds support for normal dispatch and combine operations in Deep EP, enabling intranode expert routing and result aggregation. Significantly expands deep_ep.cpp (397 additions) and buffer.py with comprehensive dispatch/combine logic.

## Technical Significance
Enables efficient MoE inference by supporting normal (non-tree) dispatch and combine operations for expert routing. Intracode dispatch reduces communication overhead compared to cross-node dispatch. The combine operator merges expert outputs, essential for Mixture of Experts inference pipelines on Ascend NPUs.

## Related
- technique-moe-routing
- technique-dispatch-optimization
- technique-intranode-communication