---
id: technique-pr-sgl-kernel-npu-95
title: "PR Insight: sgl-project/sgl-kernel-npu #95"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - moe
  - event-sync
  - hccs
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/95"
---

# PR Insight: sgl-project/sgl-kernel-npu #95

**Title:** [Feature] Add diagnostic modules to dispatch and combine

## Overview
This PR adds diagnostic modules to detect slow anomalies in dispatch and combine communication within supernodes. It maintains statistical matrices of average receive/send wait times between ranks and provides analysis utilities to identify abnormal communication patterns.

## Technical Significance
The diagnostic capability is critical for production debugging of MoE systems where communication imbalances cause severe performance degradation. By tracking per-rank wait times and applying threshold-based anomaly detection, operators can identify slow nodes or network issues. The implementation shows minimal performance impact (<1% overhead) while providing valuable debugging insights.

## Related
- `technique-hccl-optimization`, `hw-hccs`, `technique-moe`