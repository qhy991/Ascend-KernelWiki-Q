---
id: technique-pr-samples-2526
title: "PR Insight: Ascend/samples #2526"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - hccl-optimization
  - multi-card
  - llm
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2526"
---

# PR Insight: Ascend/samples #2526

**Title:** [llm-datadist] 添加单进程多卡示例

## Overview
This PR adds a single-process multi-card sample example to the llm-datadist collection, demonstrating how to distribute data processing across multiple NPU cards within a single process context for large language model workloads.

## Technical Significance
Provides a reference implementation for multi-card data distribution patterns in LLM inference/training scenarios, showing how to efficiently coordinate across multiple Ascend cards without multi-process overhead.

## Related
- `technique-hccl-optimization`