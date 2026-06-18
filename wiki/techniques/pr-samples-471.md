---
id: technique-pr-samples-471
title: "PR Insight: Ascend/samples #471"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deblur-gan
  - common-library
  - refactoring
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/471"
---

# PR Insight: Ascend/samples #471

**Title:** DeblurGAN_GOPRO_Blur2Sharp改用公共库代码

## Overview
This PR refactors the DeblurGAN GOPRO Blur2Sharp sample to use common library code instead of custom implementations, improving code maintainability and consistency.

## Technical Significance
Demonstrates the benefits of using shared libraries for common operations like image processing and model inference, reducing code duplication and making samples easier to maintain.

## Related
- `pattern-refactoring`
- `pattern-library-maintenance`