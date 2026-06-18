---
id: technique-pr-samples-1002
title: "PR Insight: Ascend/samples #1002"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - pytorch
  - pruning
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1002"
---

# PR Insight: Ascend/samples #1002

**Title:** add prune sample for amct_pytorch

## Overview
Adds a new pruning sample for AMCT PyTorch, demonstrating how to apply structured pruning techniques to PyTorch models on Ascend hardware.

## Technical Significance
Expands the AMCT PyTorch compression techniques coverage to include pruning, which is complementary to quantization. Pruning can reduce model size and computation by removing redundant connections.

## Related
- `technique-pruning` / `technique-compression`
