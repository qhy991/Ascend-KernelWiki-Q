---
id: technique-pr-samples-2773
title: "PR Insight: Ascend/samples #2773"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tiling
  - namespace
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2773"
---

# PR Insight: Ascend/samples #2773

**Title:** add namespace AscendC::tiling for sample

## Overview
This PR updates samples to use the AscendC::tiling namespace. This change organizes tiling-related code under a dedicated namespace, improving code structure and preventing naming conflicts.

## Technical Significance
Proper namespace organization is important for code maintainability and preventing naming collisions in complex projects. Using the AscendC::tiling namespace follows C++ best practices and makes it clear which functionality relates to tiling operations.

## Related
- technique-nz-tiling