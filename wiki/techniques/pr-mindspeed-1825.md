---
id: technique-pr-mindspeed-1825
title: "PR Insight: Ascend/MindSpeed #1825"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - long-sequence
  - bnsd
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1825"
---

# PR Insight: Ascend/MindSpeed #1825

**Title:** 长序列支持BNSD和arguments整改

## Overview
This PR adds support for BNSD (Batch-Sequence-N-Head-Dim) format for long sequences and refactors argument handling. The changes improve long-context training support and clean up command-line argument interfaces.

## Technical Significance
BNSD format is important for efficient long-sequence processing on Ascend NPUs. Supporting this format enables better memory layout for attention operations and improves performance for long-context workloads.

## Related
- format-conversion
- attention-optimization
- long-sequence training