---
id: technique-pr-samples-80
title: "PR Insight: Ascend/samples #80"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - aicpu
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/80"
---

# PR Insight: Ascend/samples #80

**Title:** add custom aicpu op

## Overview
This PR adds custom operator examples specifically for AICPU, which handles CPU-side preprocessing and post-processing operations in the Ascend computing pipeline. It demonstrates the development pattern for AICPU operators that complement NPU kernel operators.

## Technical Significance
Extends the custom operator repertoire to include AICPU-based implementations, enabling developers to implement flexible data preprocessing, control flow, and hybrid CPU-NPU operations in Ascend workloads.

## Related
- `technique-operator-fusion`
- `technique-pipeline-scheduling`