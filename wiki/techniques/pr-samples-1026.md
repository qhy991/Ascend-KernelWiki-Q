---
id: technique-pr-samples-1026
title: "PR Insight: Ascend/samples #1026"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - acllite
  - dvpp
  - preprocessing
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1026"
---

# PR Insight: Ascend/samples #1026

**Title:** 完善acllite crop&paste api 及相关样例修改

## Overview
Improves the acllite crop and paste APIs and updates related sample code. Acllite is a lightweight C++ API wrapper around ACL (Ascend Computing Language) for easier model deployment.

## Technical Significance
Enhances the preprocessing capabilities in acllite, specifically for crop and paste operations which are common in computer vision pipelines. These operations are likely implemented using DVPP (Digital Vision Pre-Processing) hardware acceleration.

## Related
- `technique-dvpp-optimization` / `technique-preprocessing`
