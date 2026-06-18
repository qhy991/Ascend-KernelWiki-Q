---
id: technique-pr-samples-2430
title: "PR Insight: Ascend/samples #2430"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - llm
  - datadist
  - layer-wise
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2430"
---

# PR Insight: Ascend/samples #2430

**Title:** [LLM-DataDist] 新增按层传输Samples

## Overview
This PR adds layer-wise transmission samples to the LLM-DataDist collection, demonstrating how to distribute data by layer in large language model workloads.

## Technical Significance
Provides reference implementations for layer-wise data distribution patterns in LLM inference/training, showing how to optimize communication granularity for different model architectures.

## Related
- `technique-hccl-optimization`