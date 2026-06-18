---
id: technique-pr-samples-2804
title: "PR Insight: Ascend/samples #2804"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build-system
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2804"
---

# PR Insight: Ascend/samples #2804

**Title:** update sample with arch path * update sample with arch path

## Overview
This PR updates samples to use architecture-specific paths. The change ensures samples correctly locate architecture-dependent resources and headers for different Ascend NPU variants.

## Technical Significance
Architecture-specific paths are important for samples to work across different Ascend hardware variants (Ascend 910, 910B, etc.). Proper path management ensures samples build and run correctly on target hardware.

## Related
- Architecture-specific build patterns