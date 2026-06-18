---
id: technique-pr-modellink-2688
title: "PR Insight: Ascend/ModelLink #2688"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pytorch
  - bugfix
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2688"
---

# PR Insight: Ascend/ModelLink #2688

**Title:** compatible with torch2.1

## Overview
This PR adds compatibility with PyTorch 2.1 for ModelLink. The changes ensure that ModelLink can work correctly with PyTorch 2.1 on Ascend hardware, likely addressing API changes or dependency issues in the newer PyTorch version.

## Technical Significance
PyTorch compatibility is crucial for ModelLink users. Supporting PyTorch 2.1 allows users to benefit from performance improvements and new features in the PyTorch ecosystem while training on Ascend NPUs, keeping ModelLink current with the PyTorch release cycle.

## Related