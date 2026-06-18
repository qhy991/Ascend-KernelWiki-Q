---
id: technique-pr-cann-ops-adv-200
title: "PR Insight: cann-ops-adv #200"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - distributed
  - communication
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/200"
---

# PR Insight: cann-ops-adv #200 - add moe_distribute_combine

## Overview
This PR adds the moe_distribute_combine operator, which handles distributed MoE expert output combination across multiple NPUs for large-scale MoE inference.

## Technical Significance
Distributed MoE requires combining expert outputs from multiple devices. This operator enables efficient aggregation of MoE results across NPUs, supporting ultra-large MoE models that don't fit on a single Ascend device.

## Related
- `kernel-moe`
- `kernel-reduce`
- `technique-hccl-optimization`
- `hw-hccs`