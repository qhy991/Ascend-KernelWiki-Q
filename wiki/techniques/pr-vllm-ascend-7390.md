---
id: technique-pr-vllm-ascend-7390
title: "PR Insight: vllm-project/vllm-ascend #7390"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-comm
  - vl-models
  - mla
  - tensor-parallelism
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7390"
---

# PR Insight: vllm-project/vllm-ascend #7390

**Title:** [Feature] Support Flash Comm V1 for VL models (with MLA)

## Overview
This PR enables Flash Comm V1 for vision-language models with MLA attention. The fix detects VL first layer at init time, sets need_gather_q_kv=False when flashcomm1+TP>1+is_vl_first_layer, and pre-allocates output as [N//tp_size, H]. It also improves VL model detection and removes unnecessary CPU/fp32 round-trips in position embedding.

## Technical Significance
This fix matters for VL model efficiency on Ascend with tensor parallelism. Previously, flash comm was blocked for VL models because inputs_embeds from vision encoder weren't reduce-scattered, causing wrong output shapes. The fix enables the optimized flash comm path for VL models while maintaining correctness, significantly improving attention performance for multimodal inference.

## Related
- technique-flash-comm
- technique-mla
- technique-vl-inference