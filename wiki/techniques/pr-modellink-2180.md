---
id: technique-pr-modellink-2180
title: "PR Insight: Ascend/ModelLink #2180"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mmlu
  - evaluation
  - perplexity
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2180"
---

# PR Insight: Ascend/ModelLink #2180

**Title:** mmlu支持ppl评估

## Overview
This PR adds perplexity (PPL) evaluation support for the MMLU (Massive Multitask Language Understanding) benchmark. MMLU evaluates model knowledge across multiple domains, and PPL provides an additional metric.

## Technical Significance
Adding PPL evaluation to MMLU provides more comprehensive model assessment on Ascend hardware. Perplexity measures how well the model predicts text, complementing accuracy-based metrics.

## Related
- MMLU evaluation
- perplexity metrics