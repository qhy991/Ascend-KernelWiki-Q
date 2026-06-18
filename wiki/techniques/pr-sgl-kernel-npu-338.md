---
id: technique-pr-sgl-kernel-npu-338
title: "PR Insight: sgl-project/sgl-kernel-npu #338"
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
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/338"
---

# PR Insight: sgl-project/sgl-kernel-npu #338

**Title:** Document get_dispatch_layout API

## Overview
This PR adds documentation for the get_dispatch_layout API function, including its definition, input parameters, return values, and practical usage examples. The API provides layout computation for DeepEP dispatch operations, enabling efficient token-to-expert assignment and memory layout planning.

## Technical Significance
Documenting get_dispatch_layout provides developers with the knowledge to query and understand dispatch layouts for DeepEP operators, which is essential for optimizing memory access patterns and implementing custom routing strategies in MoE inference pipelines.

## Related
- `kernel-deepep-dispatch`, `technique-api-design`, `technique-tiling`