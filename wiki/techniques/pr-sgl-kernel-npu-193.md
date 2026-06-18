---
id: technique-pr-sgl-kernel-npu-193
title: "PR Insight: sgl-project/sgl-kernel-npu #193"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - internode
  - testing
  - hccs
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/193"
---

# PR Insight: sgl-project/sgl-kernel-npu #193

**Title:** add test internode for deepep

## Overview
Adds comprehensive testing infrastructure for DeepEP internode API, including test scripts and performance benchmarks. Tests show HCCS bandwidth of 35-38 GB/s for dispatch and 52-53 GB/s for combine, with RDMA bandwidth of 8-9 GB/s and 13 GB/s respectively.

## Technical Significance
The internode testing framework validates cross-node communication performance and correctness for DeepEP deployments. The benchmark results provide realistic performance expectations for multi-server deployments, showing efficient HCCS and RDMA bandwidth utilization. This testing infrastructure is crucial for ensuring reliable multi-server MoE inference performance.

## Related
- `wiki-kernel-moe`
- `wiki-technique-hccl-optimization`
- `wiki-technique-internode`
- `wiki-technique-testing`