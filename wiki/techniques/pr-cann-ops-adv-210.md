---
id: technique-pr-cann-ops-adv-210
title: "PR Insight: cann-ops-adv #210"
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
  - "https://gitee.com/ascend/cann-ops-adv/pulls/210"
---

# PR Insight: cann-ops-adv #210 - add moedistributedispatch op

## Overview
This PR adds the moe_distributedispatch operator, which handles distributed MoE token dispatch across multiple NPUs for large-scale MoE inference.

## Technical Significance
Distributed MoE requires dispatching tokens to experts located on different devices. This operator enables efficient token distribution across NPUs, supporting ultra-large MoE models that span multiple Ascend devices for inference.

## Related
- `kernel-moe`
- `technique-hccl-optimization`
- `technique-data-reuse`
- `hw-hccs`