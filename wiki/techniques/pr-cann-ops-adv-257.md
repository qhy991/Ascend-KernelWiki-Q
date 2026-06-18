---
id: technique-pr-cann-ops-adv-257
title: "PR Insight: Ascend/cann-ops-adv #257"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - transformer
  - ascendc
  - instruction-queue
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/257"
---

# PR Insight: Ascend/cann-ops-adv #257

**Title:** modify scaled_masked_softmax_grad_v2 instruction

## Overview
This PR modifies instruction scheduling and optimization in the scaled masked softmax gradient V2 operator implementation. The changes target the AscendC kernel implementation to improve instruction pipeline efficiency and address potential performance bottlenecks in the backward pass of attention mechanisms.

## Technical Significance
Instruction-level modifications in softmax gradient operators are critical for achieving optimal performance on Ascend hardware. This change likely addresses instruction queue scheduling, pipeline bubbles, or data movement patterns between Vector and Scalar units. The scaled masked softmax operator is a key component in transformer attention computation, and its gradient performance directly impacts training throughput. The V2 version suggests improvements over the original implementation, potentially focusing on head-dimension optimizations or mask handling efficiency.

## Related
- `technique-softmax-ascendc`
- `technique-pipeline-scheduling`
- `technique-transformer-attention`
- `technique-cube-vector-overlap`