---
id: technique-pr-sgl-kernel-npu-169
title: "PR Insight: sgl-project/sgl-kernel-npu #169"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - internode
  - dispatch
  - combine
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/169"
---

# PR Insight: sgl-project/sgl-kernel-npu #169

**Title:** deepep support internode api

## Overview
Adds internode API support for DeepEP on A2 architecture, implementing prefill dispatch and combine operators for multi-server deployments. The implementation includes comprehensive tiling utilities and layered kernel implementations for efficient cross-node MoE operations.

## Technical Significance
This implementation enables DeepEP to scale across multiple A2 servers, providing efficient internode communication and data distribution for MoE inference. The internode API with prefill support allows for better resource utilization and load balancing across servers. The comprehensive tiling and layered kernel implementations optimize memory access and computational efficiency for cross-node MoE operations.

## Related
- `wiki-kernel-moe`
- `wiki-technique-hccl-optimization`
- `wiki-hardware-a2`
- `wiki-technique-internode`