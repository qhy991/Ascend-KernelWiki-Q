---
id: technique-pr-mindspeed-1759
title: "PR Insight: Ascend/MindSpeed #1759"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - long-sequence
  - ring-attention
  - operator-fusion
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1759"
---

# PR Insight: Ascend/MindSpeed #1759

**Title:** 长序列RingAttention适配TND+融合算子适配

## Overview
This PR adapts RingAttention for long sequences and adds support for TND (likely Tensor-Sequence-Head-Dim) format with fused operators. The changes improve performance for long-context attention workloads.

## Technical Significance
RingAttention is important for handling extremely long sequences beyond device memory limits. Adapting it with TND format and operator fusion enables more efficient execution of long-context attention on Ascend NPUs by reducing memory access and communication overhead.

## Related
- ring-attention
- technique-operator-fusion
- long-sequence training