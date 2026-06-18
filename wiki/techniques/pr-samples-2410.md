---
id: technique-pr-samples-2410
title: "PR Insight: Ascend/samples #2410"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - mmad
  - api
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2410"
---

# PR Insight: Ascend/samples #2410

**Title:** add AscendC Mmad Api invocation sample

## Overview
This PR adds a sample demonstrating how to invoke the AscendC Mmad (Matrix Multiply-Add) API. Mmad is a high-level matrix operation API in AscendC that abstracts lower-level cube unit details for common matrix operations.

## Technical Significance
The Mmad API provides a convenient interface for matrix operations without needing to manually configure cube units and data movements. This sample helps developers understand when and how to use the API versus custom cube kernel development.

## Related
- `kernel-matmul-ascendc`, `hw-cube-unit`