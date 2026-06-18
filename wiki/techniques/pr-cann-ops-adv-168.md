---
id: technique-pr-cann-ops-adv-168
title: "PR Insight: cann-ops-adv #168"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - routing
  - quantization
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/168"
---

# PR Insight: cann-ops-adv #168 - delete large case for MoeInitRoutingQuantV2

## Overview
This PR removes large test cases for the MoeInitRoutingQuantV2 operator, likely to reduce testing time or address memory constraints in the test environment.

## Technical Significance
Removing overly large test cases improves CI/CD efficiency while maintaining test coverage. The modification ensures faster validation of quantized MoE routing functionality on Ascend NPUs without sacrificing quality assurance for typical usage patterns.

## Related
- `kernel-moe`
- `kernel-quant-matmul`
- `kernel-topk`
- `technique-testing`