---
id: technique-pr-sgl-kernel-npu-528
title: "PR Insight: sgl-kernel-npu #528"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - test
  - gdn
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/528"
---

# PR Insight: sgl-kernel-npu #528

**Title:** feat: fix gdn test backends, skip old test, better naming

## Overview
This PR improves the testing infrastructure for the SGLang NPU kernel library. It specifically targets tests for Gated Delta Network (GDN) backends and cleans up outdated test cases to streamline the CI pipeline. 

## Key Changes
1. **Fix GDN Test Backends:** Corrects backend-specific tests for Gated Delta Network operations to ensure they properly align with the latest kernel features. 
2. **Skip Old Tests:** Explicitly skips tests covering legacy or outdated kernels (e.g., ones superseded by new integrated "megakernels") to reduce testing redundancy and accelerate continuous integration.
3. **Better Naming:** Refactors naming conventions across the test suite. This enhances developer readability, debuggability, and maintainability.

## Context
These changes are part of a broader ongoing effort to organize and stabilize the `sgl-kernel-npu` test framework (also closely associated with PR #527), ensuring that kernel coverage correctly reflects the current state of supported algorithms without wasting compute on deprecated ones.
