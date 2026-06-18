---
id: technique-pr-samples-2548
title: "PR Insight: Ascend/samples #2548"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - gmm
  - code-quality
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2548"
---

# PR Insight: Ascend/samples #2548

**Title:** gmm rm using namespace

## Overview
This PR removes "using namespace" directives from the GMM (group matrix multiplication) samples. Removing namespace prefixes improves code clarity and prevents potential name collisions.

## Technical Significance
Explicit namespace prefixes make code more readable and maintainable. They prevent accidental name conflicts, especially important in samples that serve as templates for production code.

## Related
- `kernel-matmul-ascendc`, `pattern-code-quality`