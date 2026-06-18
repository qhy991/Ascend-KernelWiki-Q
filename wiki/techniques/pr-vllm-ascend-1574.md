---
id: technique-pr-vllm-ascend-1574
title: "PR Insight: vllm-project/vllm-ascend #1574"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - testing
  - accuracy
  - moe
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1574"
---

# PR Insight: vllm-project/vllm-ascend #1574

**Title:** [Test] Remove V0 accuracy test and enable MoE and VL test on V1

## Overview
This PR removes V0 accuracy tests and enables MoE and Vision-Language (VL) accuracy tests on V1 infrastructure.

## Technical Significance
Modernizes test infrastructure by deprecating V0 tests and focusing test coverage on V1. Enabling MoE and VL tests on V1 ensures comprehensive accuracy validation for these important model categories in the current architecture.

## Related
- `kernel-moe`
- `kernel-vision-language`