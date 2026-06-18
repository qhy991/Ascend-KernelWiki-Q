---
id: technique-pr-vllm-ascend-8864
title: "PR Insight: vllm-project/vllm-ascend #8864"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - eplb
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8864"
---

# PR Insight: vllm-project/vllm-ascend #8864

**Title:** [BugFix] Fix Ascend MoE routing expert count with EPLB

## Overview
This PR fixes Ascend MoE dynamic EPLB routing after upstream vLLM MoE/EPLB refactor that introduced the distinction between logical experts (router logits) and physical/global experts (logical + EPLB replicas). The bug caused `router_logits.shape[-1]` validation to fail when compared against `moe_config.num_experts` (which includes physical experts with dynamic EPLB). The fix adds a helper to resolve logical expert count from `moe_config.num_logical_experts` and applies it across all MoE quant paths.

## Technical Significance
The bug blocked quantized MoE inference with dynamic EPLB due to incorrect expert count validation. The fix ensures compatibility with upstream vLLM's logical/physical expert split by using the correct expert count for router validation, expert selection, zero expert handling, and profile routing. This resolves the "Number of global experts mismatch" assertion error in Qwen3 MoE W8A8 dynamic EPLB tests and prevents similar issues in other quantization modes.

## Related
- `technique-moe` (MoE expert routing)
- `technique-eplb` (Expert parallel load balancing)
- `pattern-quantization` (MoE quantization paths)