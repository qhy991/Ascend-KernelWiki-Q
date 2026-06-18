---
id: technique-pr-cann-ops-adv-198
title: "PR Insight: cann-ops-adv #198"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - grouped-gemm
  - configuration
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/198"
---

# PR Insight: cann-ops-adv #198 - add_MoeFinalizeRoutingV2 && GroupedMatmulAdd config_910_93

## Overview
This PR adds the MoeFinalizeRoutingV2 and GroupedMatmulAdd operators along with configuration for Ascend 910_93, expanding MoE inference capabilities on specific Ascend hardware variants.

## Technical Significance
MoeFinalizeRoutingV2 completes the routing process with improved implementation. GroupedMatmulAdd adds support for fused GEMM with addition, reducing kernel launches. Configuration support for 910_93 ensures proper hardware-specific optimization, improving MoE inference performance.

## Related
- `kernel-moe`
- `kernel-grouped-gemm`
- `technique-operator-fusion`
- `hw-cube-unit`