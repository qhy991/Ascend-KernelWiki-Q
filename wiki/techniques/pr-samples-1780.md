---
id: technique-pr-samples-1780
title: "PR Insight: Ascend/samples #1780"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tensorflow
  - ascendc
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1780"
---

# PR Insight: Ascend/samples #1780

**Title:** 新增ascendc tensorflow 整网推理样例工程

## Overview
This PR adds a complete end-to-end inference example using AscendC with TensorFlow, demonstrating how to build a full inference pipeline that leverages AscendC operators within a TensorFlow graph.

## Technical Significance
Provides a comprehensive reference for integrating AscendC operators into TensorFlow inference workflows, enabling developers to accelerate custom operations while maintaining framework compatibility.

## Related
- `technique-operator-fusion`
- `technique-pipeline-scheduling`