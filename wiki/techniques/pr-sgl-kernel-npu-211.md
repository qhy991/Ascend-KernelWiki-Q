---
id: technique-pr-sgl-kernel-npu-211
title: "PR Insight: sgl-project/sgl-kernel-npu #211"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - internode
  - hostbound
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/211"
---

# PR Insight: sgl-project/sgl-kernel-npu #211

**Title:** optimizer internode_dispatch hostbound

## Overview
Optimizes internode dispatch hostbound operations by calculating dispatch normal input parameters using NPU instead of CPU. Benchmarks show 4.6% HCCS bandwidth improvement and 4.4% latency reduction for single server, and 1.5% bandwidth improvement with 1.9% latency reduction for two-server setups.

## Technical Significance
The hostbound optimization reduces CPU-NPU data transfer and computation overhead for internode dispatch operations. The performance improvements, while modest, are consistent across single and multi-server deployments, demonstrating the effectiveness of moving parameter calculations to NPU for better resource utilization.

## Related
- `wiki-kernel-moe`
- `wiki-technique-npu-computation`
- `wiki-technique-internode`
- `wiki-technique-hostbound`