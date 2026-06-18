---
id: technique-pr-sgl-kernel-npu-306
title: "PR Insight: sgl-project/sgl-kernel-npu #306"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fla
  - gdn
  - gating
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/306"
---

# PR Insight: sgl-project/sgl-kernel-npu #306

**Title:** optimize gdn gating and fused_qkvzba_split_reshape_cat

## Overview
Optimizes GDN (Grouped Dilated Network) gating operations and fused QKVZBA split-reshape-concat operations for improved performance. The optimizations target computational efficiency in attention-related operations.

## Technical Significance
GDN gating and QKVZBA operations are critical components in modern attention mechanisms. The optimizations reduce computational overhead and improve memory access patterns, directly impacting inference throughput for models that utilize these advanced attention components.

## Related
- `wiki-kernel-attention`
- `wiki-technique-fla`
- `wiki-technique-gating`
- `wiki-technique-optimization`