---
id: technique-pr-modellink-2811
title: "PR Insight: Ascend/ModelLink #2811"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2811"
---

# PR Insight: Ascend/ModelLink #2811

**Title:** 【refactor】high availability to features_manager

## Overview
This PR refactors high availability functionality into the features_manager module. It improves code organization and maintainability of the ModelLink framework.

## Technical Significance
Code refactoring improves maintainability and extensibility of the framework. This change makes it easier to add new features and manage high availability configurations for training on Ascend NPUs, supporting more robust production deployments.

## Related
- `technique-distributed-training`