---
id: technique-pr-sgl-kernel-npu-118
title: "PR Insight: sgl-project/sgl-kernel-npu #118"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - eplb
  - random
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/118"
---

# PR Insight: sgl-project/sgl-kernel-npu #118

**Title:** [FusedDeepMoe] Support EPLB

## Overview
This PR adds comprehensive EPLB (Expert Per-Load Balancing) support to FusedDeepMoe, including receive count tracking, random routing, updated interfaces, and test cases. It integrates with the sglang framework for end-to-end validation.

## Technical Significance
EPLB with random routing improves load balancing across experts, reducing straggler effects in distributed MoE inference. The receive count tracking enables adaptive routing decisions and performance monitoring. Random routing prevents deterministic hotspots and improves overall system utilization.

## Related
- `technique-moe`, `technique-hccl-optimization`