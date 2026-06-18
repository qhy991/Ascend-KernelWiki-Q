---
id: technique-pr-samples-2762
title: "PR Insight: Ascend/samples #2762"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2762"
---

# PR Insight: Ascend/samples #2762

**Title:** uniquecust modify infershape

## Overview
This PR modifies the infer shape logic for a unique custom operator sample. The change improves shape inference accuracy for the custom operator.

## Technical Significance
Accurate shape inference is critical for framework integration and proper memory allocation. Correct infer shape logic ensures custom operators work correctly within framework graphs and optimization passes.

## Related
- Shape inference patterns, custom operator integration