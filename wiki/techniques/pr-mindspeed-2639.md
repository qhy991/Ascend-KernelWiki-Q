---
id: technique-pr-mindspeed-2639
title: "PR Insight: Ascend/MindSpeed #2639"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - attention
  - ring-attention
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2639"
---

# PR Insight: Ascend/MindSpeed #2639

**Title:** fix double-ring-attention inter-intra p2p comm conflict

## Overview
This PR fixes a communication conflict in double ring attention between inter-device and intra-device peer-to-peer communication operations. The bug caused race conditions or deadlocks when using ring attention with complex communication patterns.

## Technical Significance
Ring attention is a memory-efficient technique for processing long sequences by splitting attention computation across devices. Double ring attention extends this with additional communication layers. Fixing inter-intra communication conflicts is essential for correctness and preventing deadlocks in distributed attention computations.

## Related
- `kernel-attention`
- `technique-hccl-optimization`
- `technique-ring-attention`