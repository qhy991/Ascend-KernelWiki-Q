---
id: technique-pr-sgl-kernel-npu-391
title: "PR Insight: sgl-project/sgl-kernel-npu #391"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - deepep
  - combine-kernel
  - validation
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/391"
---

# PR Insight: sgl-project/sgl-kernel-npu #391

**Title:** The test is added to test only the combine function.

## Overview
This PR adds a dedicated test suite for the DeepEP combine function, enabling isolated testing and validation of the combine kernel independently from the full dispatch-combine pipeline. The test updates CI workflow configuration to include this focused testing capability.

## Technical Significance
Isolated testing of the combine kernel improves debuggability by allowing targeted validation without the complexity of the full dispatch-combine interaction. This focused testing approach helps identify issues specific to the combine operation more efficiently during development and CI processes.

## Related
- `kernel-deepep-combine`, `technique-testing`, `technique-validation`