---
id: technique-pr-vllm-ascend-9382
title: "PR Insight: vllm-project/vllm-ascend #9382"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascend950
  - gdn
  - custom-op
  - ascendc
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9382"
---

# PR Insight: vllm-project/vllm-ascend #9382

**Title:** [Ascend950] [Feature] Support custom op for GDN on Ascend 950

## Overview
This PR adds custom operator support for GDN (Gated Delta Network) operations on Ascend 950 hardware. The implementation includes updates to the recurrent GDN operator, causal conv1d operator, chunk operations, device operator bindings, and layer norm implementations to support Ascend 950.

## Technical Significance
Custom operators provide hardware-optimized implementations that significantly outperform generic implementations. Supporting GDN on Ascend 950 enables efficient inference for models using gated delta networks, which are important for certain sequence modeling and time-series tasks.

## Related
- `hw-cube-unit`
- `hw-vector-unit`
- `technique-operator-fusion`