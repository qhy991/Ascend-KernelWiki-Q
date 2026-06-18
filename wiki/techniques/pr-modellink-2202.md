---
id: technique-pr-modellink-2202
title: "PR Insight: Ascend/ModelLink #2202"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bbh
  - chain-of-thought
  - evaluation
  - data-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2202"
---

# PR Insight: Ascend/ModelLink #2202

**Title:** 新增bbh cot评估模版 & bbh评估支持DP

## Overview
This PR adds BBH (Big-Bench Hard) Chain-of-Thought (CoT) evaluation templates and supports data parallelism for BBH evaluation. BBH is a challenging benchmark requiring multi-step reasoning.

## Technical Significance
Adding BBH CoT evaluation expands benchmarking for complex reasoning tasks. Data parallelism enables efficient evaluation across multiple Ascend NPUs for faster benchmarking results.

## Related
- BBH evaluation
- chain-of-thought reasoning