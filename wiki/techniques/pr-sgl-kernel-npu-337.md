---
id: technique-pr-sgl-kernel-npu-337
title: "PR Insight: sgl-project/sgl-kernel-npu #337"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - documentation
  - deepep
  - low-latency
  - api
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/337"
---

# PR Insight: sgl-project/sgl-kernel-npu #337

**Title:** Added the low_latency operator API documentation.

## Overview
This PR adds comprehensive documentation for the DeepEP low-latency operator API, describing the optimized dispatch and combine variants designed for minimal latency inference scenarios. The documentation covers parameter specifications, performance characteristics, and usage patterns for low-latency MoE inference.

## Technical Significance
The low-latency API documentation enables developers to leverage DeepEP's latency-optimized MoE routing for time-sensitive inference applications. It provides guidance on when to use low-latency mode versus normal mode, and how to configure operators for optimal latency performance.

## Related
- `kernel-deepep-low-latency`, `technique-api-design`, `technique-latency-optimization`