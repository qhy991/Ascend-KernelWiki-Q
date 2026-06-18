---
id: technique-pr-sgl-kernel-npu-68
title: "PR Insight: sgl-project/sgl-kernel-npu #68"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla-preprocess
  - tiling
  - acl-graph
  - precision
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/68"
---

# PR Insight: sgl-project/sgl-kernel-npu #68

**Title:** Solve the mlapo operator's precision anomaly in acl graph

## Overview
This PR fixes precision anomalies in the MLA preprocessing operator when executed in ACL graph mode by changing tiling host-to-device implementation. Updates mla_preprocess.cpp tiling logic to ensure correct tiling data retrieval during graph replay.

## Technical Significance
Resolves precision issues that occur in ACL graph execution mode, ensuring consistent numerical results across different execution contexts. Proper tiling data handling is essential for maintaining correctness in graph-optimized inference pipelines on Ascend hardware.

## Related
- technique-mla
- technique-tiling
- technique-acl-graph
- technique-precision