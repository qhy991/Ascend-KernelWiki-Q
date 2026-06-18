---
id: technique-pr-sgl-kernel-npu-201
title: "PR Insight: sgl-project/sgl-kernel-npu #201"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - deepep
  - single-server
  - normal-mode
  - dispatch
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/201"
---

# PR Insight: sgl-project/sgl-kernel-npu #201

**Title:** Support run normal mode deepep on a single A2 machine

## Overview
Enables DeepEP normal mode operation on single A2 machines by implementing comprehensive dispatch, combine, and notify operators with full tiling support. The implementation includes both host-side tiling calculations and kernel-side operations.

## Technical Significance
This feature makes DeepEP viable for single-server deployments, which is critical for cost-effective inference setups. The normal mode implementation provides an alternative to low-latency mode, offering different performance characteristics. The comprehensive tiling support ensures efficient memory utilization and computational performance on single A2 servers.

## Related
- `wiki-kernel-moe`
- `wiki-technique-single-server`
- `wiki-hardware-a2`
- `wiki-technique-tiling`