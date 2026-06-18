---
id: technique-pr-vllm-ascend-10461
title: "PR Insight: vllm-project/vllm-ascend #10461"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - gqa
  - minimax
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10461"
---

# PR Insight: vllm-project/vllm-ascend #10461

**Title:** [Feature] Support MiniMax M2 C8 cache scale in GQA load_weights

## Overview
This PR adds support for MiniMax M2 C8 cache scaling in the GQA (Grouped Query Attention) weight loading path. The implementation adds C8 cache scale support to the GQA weight loading patch, enabling proper handling of MiniMax M2 models that use C8 quantization. Validation shows AIME2025 accuracy of 93.33% and performance improvements: output token throughput increased from 3996.55 tok/s (W8A8) to 4632.68 tok/s (W8A8C8) with TPOT decreasing from 56.5ms to 52.7ms.

## Technical Significance
This feature enables support for MiniMax M2 models with C8 quantization, expanding the range of supported quantization schemes on Ascend. C8 quantization provides better compression than standard W8A8 while maintaining accuracy, as demonstrated by the AIME2025 results. The performance improvements show that C8 can deliver better throughput and latency than standard W8A8, making it an attractive option for production deployments. This support is essential for users deploying MiniMax M2 models on Ascend hardware.

## Related
- `technique-quantization`
- `technique-gqa`
- `technique-minimax`