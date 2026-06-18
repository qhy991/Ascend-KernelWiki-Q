---
id: technique-pr-vllm-ascend-4102
title: "PR Insight: vllm-project/vllm-ascend #4102"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - moe
  - quantization
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4102"
---

# PR Insight: vllm-project/vllm-ascend #4102

**Title:** [Bugfix] fix mtp profile run error where main model and mtp model use different quantization

## Overview
This PR fixes a bug where MTP profile run errors occurred when the main model and MTP model used different quantization approaches (e.g., MTP using floating-point while main model uses quantized computation). The fix moves quantization type from MoECommMethod singleton to AscendFusedMoe class and passes it as a parameter, allowing different quantization approaches for different layers.

## Technical Significance
MTP models often use different computation modes than main models (floating-point vs quantized). The singleton pattern limitation prevented handling mixed quantization scenarios within a single model. The fix enables proper quantization configuration per layer, which is essential for correctness when combining MTP with quantized main models like DeepSeek-R1 w8a8.

## Related
- `technique-mtp`, `technique-quantization`, `technique-moe`, `pattern-config-management`