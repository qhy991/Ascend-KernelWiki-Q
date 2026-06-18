---
id: technique-pr-samples-1197
title: "PR Insight: Ascend/samples #1197"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - object-detection
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1197"
---

# PR Insight: Ascend/samples #1197

**Title:** 通用目标识别样例的READM修改

## Overview
This PR updates the README documentation for the general object recognition sample application.

## Technical Significance
Documentation improvements help developers understand best practices for object recognition on Ascend. Object recognition workloads benefit from operator fusion to reduce memory movement between detection stages, and efficient use of Ascend's unified buffer for intermediate feature maps.

## Related
- technique-operator-fusion
- hw-unified-buffer