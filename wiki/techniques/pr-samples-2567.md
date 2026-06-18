---
id: technique-pr-samples-2567
title: "PR Insight: Ascend/samples #2567"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - python
  - dataflow
  - pydflow
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2567"
---

# PR Insight: Ascend/samples #2567

**Title:** add python dataflow

## Overview
This PR adds a Python dataflow sample. The new sample demonstrates how to use dataflow programming patterns with Python interfaces for Ascend NPU operations.

## Technical Significance
Dataflow programming is a key paradigm for efficient kernel execution on Ascend NPUs. Python interfaces make dataflow programming more accessible to developers who prefer Python over C++.

## Related
- `technique-pipeline-scheduling`
- `hw-event-sync`
- `technique-cube-vector-overlap`