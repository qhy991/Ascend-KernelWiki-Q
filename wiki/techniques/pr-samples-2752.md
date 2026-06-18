---
id: technique-pr-samples-2752
title: "PR Insight: Ascend/samples #2752"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - llm
  - data-distribution
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2752"
---

# PR Insight: Ascend/samples #2752

**Title:** 添加llm_datadist sample

## Overview
This PR adds an LLM data distribution sample. The sample demonstrates how to distribute data across multiple devices for Large Language Model inference or training.

## Technical Significance
Efficient data distribution is crucial for multi-device LLM workloads. This sample helps developers understand data parallelism strategies and how to balance workload across Ascend NPUs.

## Related
- `pattern-data-parallelism`, `pattern-multi-device-inference`