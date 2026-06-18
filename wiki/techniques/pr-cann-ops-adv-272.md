---
id: technique-pr-cann-ops-adv-272
title: "PR Insight: Ascend/cann-ops-adv #272"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - quantization
  - transformer
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/272"
---

# PR Insight: Ascend/cann-ops-adv #272

**Title:** combine k support 2-16

## Overview
This PR extends the combine-k operator to support a range of 2 to 16 combined operations. The combine-k functionality is used in MoE and other transformer architectures where multiple experts or operations need to be combined efficiently.

## Technical Significance
Supporting variable combine-k values (2-16) provides flexibility for different MoE configurations and expert parallelism strategies. The combine operation likely aggregates outputs from multiple experts or combines multiple computational paths. This extension enables models to dynamically adjust the number of experts combined per token or batch, optimizing for different hardware capabilities and model sizes. The implementation likely uses efficient vector operations and may leverage Cube units for parallel combination of expert outputs.

## Related
- `technique-moe-ascendc`
- `technique-expert-parallelism`
- `technique-vector-unit`
- `technique-operator-fusion`