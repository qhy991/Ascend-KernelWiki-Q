---
id: technique-pr-cann-ops-adv-190
title: "PR Insight: cann-ops-adv #190"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - ring-attention
  - long-context
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/190"
---

# PR Insight: cann-ops-adv #190 - 新增RingAttentionUpdate算子

## Overview
This PR adds the RingAttentionUpdate operator, which implements the attention state update for Ring Attention, enabling efficient long-context transformer inference on Ascend NPUs.

## Technical Significance
Ring Attention enables processing arbitrarily long contexts by distributing sequence segments across devices and passing attention states in a ring pattern. This operator is critical for long-context LLM inference on multi-NPU Ascend systems, overcoming sequence length limitations.

## Related
- `kernel-attention`
- `technique-hccl-optimization`
- `technique-kv-cache-paging`
- `hw-hccs`