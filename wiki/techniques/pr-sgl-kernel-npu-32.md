---
id: technique-pr-sgl-kernel-npu-32
title: "PR Insight: sgl-project/sgl-kernel-npu #32"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - build
  - ci
  - infrastructure
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/32"
---

# PR Insight: sgl-project/sgl-kernel-npu #32

**Title:** Add build deepep step

## Overview
This PR adds Deep EP build steps to the CI workflow and container preparation script, ensuring automated compilation and testing of Deep EP components in the development pipeline.

## Technical Significance
Improves CI/CD infrastructure for Deep EP development by adding automated build verification. Container build scripts enable reproducible build environments for Ascend kernel development, essential for consistent testing across different development stages.

## Related
- technique-ci-cd
- technique-build-automation