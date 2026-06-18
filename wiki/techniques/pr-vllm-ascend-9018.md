---
id: technique-pr-vllm-ascend-9018
title: "PR Insight: vllm-project/vllm-ascend #9018"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - ascendc
  - moe
  - gdn
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9018"
---

# PR Insight: vllm-project/vllm-ascend #9018

**Title:** [Performance] add op `chunk_fwd_o` and `chunk_gated_delta_rule_fwd_h`

## Overview
This PR adds two custom AscendC operators for performance improvement: `chunk_fwd_o` and `chunk_gated_delta_rule_fwd_h`. The implementations in `csrc/moe/chunk_fwd_o/` and `csrc/moe/chunk_gated_delta_rule_fwd_h/` include comprehensive tiling infrastructure, GDN forward O epilogue with QK mask, and gated delta rule forward H update. Testing with Qwen3.6-27B-W8A8 on GPQA dataset confirms accuracy with consistent results across 5 runs (82-87%).

## Technical Significance
The new custom operators provide optimized implementations for GDN (Gated Delta Network) forward pass operations on Ascend NPUs. The `chunk_fwd_o` operator handles output computation with QK masking, while `chunk_gated_delta_rule_fwd_h` handles hidden state updates. The comprehensive tiling infrastructure ensures efficient memory access and hardware utilization (Cube/Vector units). These operators enable high-performance quantized GDN inference with accuracy maintained through rigorous GPQA benchmarking.

## Related
- `kernel-attention` (GDN attention)
- `technique-ascendc` (Custom operator development)
- `pattern-quantization` (W8A8 quantization integration)