---
id: technique-pr-samples-2271
title: "PR Insight: Ascend/samples #2271"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tensorflow
  - ascendc
  - custom-op
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2271"
---

# PR Insight: Ascend/samples #2271

**Title:** add tensorflow use ascendc custom op sample

## Overview
This PR adds a sample demonstrating how to integrate AscendC custom operators into TensorFlow graphs, showing the complete workflow from kernel implementation to TensorFlow operator registration.

## Technical Significance
Provides a comprehensive reference for extending TensorFlow with Ascend-accelerated custom operators, enabling developers to leverage Ascend hardware capabilities within TensorFlow training and inference pipelines.

## Related
- `technique-operator-fusion`
- `technique-pipeline-scheduling`