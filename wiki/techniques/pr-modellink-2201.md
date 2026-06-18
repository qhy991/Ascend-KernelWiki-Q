---
id: technique-pr-modellink-2201
title: "PR Insight: Ascend/ModelLink #2201"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - gsm8k
  - evaluation
  - data-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2201"
---

# PR Insight: Ascend/ModelLink #2201

**Title:** 新增gsm8k评估模板 & gsm8k支持DP

## Overview
This PR adds GSM8K (Grade School Math 8K) evaluation templates and supports data parallelism for GSM8K evaluation. GSM8K evaluates mathematical reasoning capabilities of language models.

## Technical Significance
Adding GSM8K evaluation expands benchmarking for mathematical reasoning. Data parallelism support enables efficient evaluation across multiple Ascend NPUs for faster results.

## Related
- GSM8K evaluation
- mathematical reasoning benchmarking