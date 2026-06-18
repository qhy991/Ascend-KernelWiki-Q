---
id: technique-pr-vllm-ascend-1632
title: "PR Insight: vllm-project/vllm-ascend #1632"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1632"
---

# PR Insight: vllm-project/vllm-ascend #1632

**Title:** [BUGFIX] FIX mtp accuraccy when temperture is not 0

## Overview
This PR fixes accuracy degradation in MTP (Multi-Token Prediction) when temperature is non-zero during sampling.

## Technical Significance
Corrects MTP sampling logic to maintain accuracy across all temperature values. The bug caused incorrect token acceptance rates when temperature deviated from 0, affecting diversity and accuracy trade-offs in speculative decoding.

## Related
- `technique-mtp`
- `technique-spec-decode`
- `technique-sampling`