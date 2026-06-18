---
id: technique-pr-sgl-kernel-npu-176
title: "PR Insight: sgl-project/sgl-kernel-npu #176"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - low-latency
  - single-server
  - dispatch
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/176"
---

# PR Insight: sgl-project/sgl-kernel-npu #176

**Title:** deepep low_latency d&c support a2 single server

## Overview
Adds low-latency dispatch and combine operator support for A2 single-server deployments in DeepEP. The implementation achieves ~42 GB/s combined bandwidth with average latency around 1ms, significantly improving single-server MoE inference performance.

## Technical Significance
This optimization enables efficient low-latency MoE inference on single A2 servers, which is critical for cost-effective deployments. The implementation includes comprehensive tiling utilities and specialized kernels for single-server scenarios, achieving excellent bandwidth utilization (~42 GB/s) and latency performance. This makes DeepEP viable for single-server deployments without sacrificing performance.

## Related
- `wiki-kernel-moe`
- `wiki-technique-low-latency`
- `wiki-hardware-a2`
- `wiki-technique-single-server`