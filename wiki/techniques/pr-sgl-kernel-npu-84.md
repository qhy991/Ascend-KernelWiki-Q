---
id: technique-pr-sgl-kernel-npu-84
title: "PR Insight: sgl-project/sgl-kernel-npu #84"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - deepep
  - testing
  - infrastructure
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/84"
---

# PR Insight: sgl-project/sgl-kernel-npu #84

**Title:** Add CI to test args -a deepep

## Overview
This PR adds CI support for the `-a deepep` build argument, merges two test workflows to eliminate redundant builds, and sets HCCL_BUFFSIZE to minimum constraint values for correctness verification. Updates CI workflows and build scripts.

## Technical Significance
Improves CI efficiency by consolidating test workflows and validating Deep EP-specific build configurations. Minimum buffer size testing ensures code constraints are correct, preventing runtime errors from misconfigured HCCL parameters. This CI infrastructure is essential for maintaining code quality across build variants.

## Related
- technique-ci-cd
- technique-build-testing
- technique-hccl-configuration