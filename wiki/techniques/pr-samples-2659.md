---
id: technique-pr-samples-2659
title: "PR Insight: Ascend/samples #2659"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - torchair
  - tiling-sink
  - custom-operator
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2659"
---

# PR Insight: Ascend/samples #2659

**Title:** [feature]torchair support tiling custom op

## Overview
This PR adds support for tiling sink custom operators in TorchAir, which is the PyTorch integration for Ascend. This allows TorchAir workflows to benefit from tiling sink optimizations.

## Technical Significance
TorchAir integration makes advanced optimizations accessible to PyTorch developers. The feature bridges custom operator optimizations with the framework-level API.

## Related
- `pattern-tiling`, `technique-custom-operators`