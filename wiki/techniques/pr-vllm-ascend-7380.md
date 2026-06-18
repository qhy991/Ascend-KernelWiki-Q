---
id: technique-pr-vllm-ascend-7380
title: "PR Insight: vllm-project/vllm-ascend #7380"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseekocr2
  - relpos-attention
  - mask-optimization
  - conv2d-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7380"
---

# PR Insight: vllm-project/vllm-ascend #7380

**Title:** Optimize DeepSeekOCR2 RelPosAttention and CustomQwen2Decoder and add doc for DeepSeekOCR2.md

## Overview
This PR optimizes DeepSeekOCR2's RelPosAttention and CustomQwen2Decoder by replacing conv2d with matmul operations, optimizing 4D mask creation (141ms -> 1ms), and switching to prompt_flash_attention. It also adds documentation for DeepSeekOCR2 model support.

## Technical Significance
These optimizations matter for OCR model inference on Ascend. Replacing conv2d with matmul leverages the Cube unit better than conv operations. The mask optimization eliminates unnecessary CPU operations. Switching to flash attention improves memory efficiency. Combined, these significantly reduce latency for vision-language OCR models.

## Related
- technique-attention
- technique-conv2d-optimization
- technique-mask-optimization