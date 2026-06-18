---
id: technique-pr-modellink-2806
title: "PR Insight: Ascend/ModelLink #2806"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - performance
  - pipeline-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2806"
---

# PR Insight: Ascend/ModelLink #2806

**Title:** add time info to the pipeline baseline for llm-0.12.1

## Overview
This PR adds time information tracking to pipeline parallelism baseline for LLM version 0.12.1 in the PyTorch backend. It enables performance monitoring for pipeline training.

## Technical Significance
Pipeline parallelism time tracking helps identify pipeline bubbles and communication overhead. This addition enables users to optimize pipeline efficiency on Ascend NPUs, improving overall training throughput.

## Related
- `technique-pipeline-scheduling`
- `technique-distributed-training`