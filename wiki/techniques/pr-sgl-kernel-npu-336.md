---
id: technique-pr-sgl-kernel-npu-336
title: "PR Insight: sgl-project/sgl-kernel-npu #336"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - documentation
  - deepep
  - api
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/336"
---

# PR Insight: sgl-project/sgl-kernel-npu #336

**Title:** add deepep normal api doc

## Overview
This PR adds documentation for the DeepEP normal dispatch and combine APIs, covering function definitions, input parameters, return values, and usage examples. The documentation provides guidance on integrating these operators into inference pipelines for efficient MoE execution.

## Technical Significance
Documenting the normal dispatch and combine APIs enables developers to properly utilize DeepEP's MoE routing mechanisms in their applications. The API reference clarifies parameter requirements, memory considerations, and expected behavior for the normal execution mode of DeepEP operators.

## Related
- `kernel-deepep-dispatch`, `kernel-deepep-combine`, `technique-api-design`