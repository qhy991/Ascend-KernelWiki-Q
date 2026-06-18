---
id: technique-pr-cann-ops-adv-238
title: "PR Insight: cann-ops-adv #238"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - rope
  - attention
  - ascendc
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/238"
---

# PR Insight: cann-ops-adv #238 - rotary_pos_emb_infer

## Overview
This PR adds rotary position embedding inference operations, providing optimized position encoding for transformer attention during LLM inference on Ascend NPUs.

## Technical Significance
Rotary position encoding is essential for modern transformer models like LLaMA. This operator provides efficient inference-time position encoding with optimized memory access patterns, reducing overhead during LLM generation.

## Related
- `kernel-rope`
- `kernel-attention`
- `hw-vector-unit`
- `technique-format-conversion`