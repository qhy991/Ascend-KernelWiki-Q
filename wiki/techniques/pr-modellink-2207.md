---
id: technique-pr-modellink-2207
title: "PR Insight: Ascend/ModelLink #2207"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - agi
  - template
  - data-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2207"
---

# PR Insight: Ascend/ModelLink #2207

**Title:** 新增agi模版 & agi推理支持DP

## Overview
This PR adds AGI (Artificial General Intelligence) evaluation templates and supports data parallelism for AGI inference. Data parallelism enables efficient inference by distributing data across multiple devices.

## Technical Significance
Adding AGI evaluation templates expands benchmarking capabilities. Data parallelism support improves inference throughput on Ascend hardware by distributing work across multiple NPUs.

## Related
- AGI evaluation
- data parallelism