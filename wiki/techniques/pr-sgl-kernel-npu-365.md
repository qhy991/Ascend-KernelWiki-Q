---
id: technique-pr-sgl-kernel-npu-365
title: "PR Insight: sgl-project/sgl-kernel-npu #365"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - ci
  - moe
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/365"
---

# PR Insight: sgl-project/sgl-kernel-npu #365

**Title:** reset ci -- run test mixed running for experts on a2.

## Overview
This PR removes the mixed expert running test configuration for A2 hardware from the CI workflow. The deletion simplifies the testing matrix by removing a specific test case that may have been redundant or causing issues in the continuous integration pipeline.

## Technical Significance
Adjusting CI test configurations helps optimize testing resources and focus on critical test cases. Removing the mixed expert running test for A2 suggests either redundancy with other tests or optimization of the testing strategy to reduce CI execution time while maintaining adequate coverage.

## Related
- `technique-testing`, `technique-ci-optimization`