---
id: technique-pr-samples-166
title: "PR Insight: Ascend/samples #166"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/166"
---

# PR Insight: Ascend/samples #166

**Title:** Added testcase of custom operator

## Overview
This PR adds comprehensive test cases for custom operator implementations, covering various input shapes, data types, and edge cases. It provides a testing framework pattern for validating custom operator correctness on Ascend hardware.

## Technical Significance
Establishes testing best practices for custom operator development, enabling developers to verify numerical accuracy and functional correctness before deploying custom kernels in production workloads.

## Related
- `technique-operator-fusion`