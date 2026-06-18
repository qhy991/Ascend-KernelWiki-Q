---
id: technique-pr-modellink-2726
title: "PR Insight: Ascend/ModelLink #2726"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mamba
  - performance
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2726"
---

# PR Insight: Ascend/ModelLink #2726

**Title:** [mamba]Eliminate the einsum operation for next states

## Overview
This PR optimizes the Mamba model by eliminating the einsum operation used for computing next states. The optimization replaces the einsum with more efficient operations better suited for Ascend hardware.

## Technical Significance
Einsum operations can be inefficient on hardware accelerators. Replacing them with specialized operations reduces computational overhead and improves the performance of Mamba models on Ascend NPUs by leveraging hardware-friendly operations.

## Related
- kernel-matmul
- technique-operator-fusion