---
id: technique-pr-samples-342
title: "PR Insight: Ascend/samples #342"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - matmul
  - conv2d
  - custom-op
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/342"
---

# PR Insight: Ascend/samples #342

**Title:** add matmul and conv2d scripts

## Overview
This PR adds build and execution scripts for matmul and conv2d operator samples, simplifying the workflow for developers who want to compile, run, and test these fundamental operators on Ascend hardware.

## Technical Significance
Reduces development friction by providing ready-to-use scripts for common operator patterns, enabling faster iteration and testing of custom matmul and conv2d implementations.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`