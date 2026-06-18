---
id: technique-pr-samples-1341
title: "PR Insight: Ascend/samples #1341"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - structured-sparsity
  - four-select-two
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1341"
---

# PR Insight: Ascend/samples #1341

**Title:** amct_pytorch四选二结构化稀疏sample

## Overview
This PR adds an AMCT PyTorch sample demonstrating "four-select-two" structured sparsity. The sample shows how to apply structured pruning where four groups are considered and two are selected, achieving compression while maintaining model structure.

## Technical Significance
Structured sparsity preserves hardware-friendly patterns unlike unstructured pruning. The "four-select-two" pattern is a specific sparsity scheme that can map well to Ascend hardware acceleration for sparse operations.

## Related
- technique-sparsity
- technique-structured-sparsity
- technique-model-compression