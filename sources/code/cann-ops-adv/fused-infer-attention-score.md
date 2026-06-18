---
id: code-cann-ops-adv-fused-infer-attention-score
title: "CANN Ops Adv \u2014 Fused Infer Attention Score"
type: source-code
repo: Ascend/cann-ops-adv
path: src/transformer/fused_infer_attention_score
url: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/fused_infer_attention_score
source_category: upstream-code
architectures:
- ascend910
- ascend910b
tags:
- attention
- fusion
- inference
- ascendc
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- unified-buffer
- global-memory
techniques:
- online-softmax
- pipeline-scheduling
- data-reuse
kernel_types:
- attention
- flash-attention
languages:
- ascendc
- cpp
---

# CANN Ops Adv — Fused Infer Attention Score

Advanced fused attention-score operator path. This is code evidence for fusing attention score computation, masking, scaling, softmax, and output staging in inference workloads.

## Code Location

- Repository: `Ascend/cann-ops-adv`
- Path: `src/transformer/fused_infer_attention_score`
- URL: https://gitee.com/ascend/cann-ops-adv/tree/master/src/transformer/fused_infer_attention_score
