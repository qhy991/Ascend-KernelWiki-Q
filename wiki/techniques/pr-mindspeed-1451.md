---
id: technique-pr-mindspeed-1451
title: "PR Insight: Ascend/MindSpeed #1451"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - feature
  - variable-length
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1451"
---

# PR Insight: Ascend/MindSpeed #1451

**Title:** feat: Supports variable sequence lengths across batches/microbatches

## Overview
This PR adds support for variable sequence lengths across different batches and microbatches. This feature enables efficient processing of mixed-length sequences without padding to the maximum length.

## Technical Significance
Improves computational efficiency and memory usage for workloads with variable-length sequences by eliminating unnecessary padding. This optimization is particularly valuable for NLP tasks with natural language inputs of varying lengths.

## Related
- `pattern-dynamic-shape`
- `kernel-attention`