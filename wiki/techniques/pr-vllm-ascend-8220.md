---
id: technique-pr-vllm-ascend-8220
title: "PR Insight: vllm-project/vllm-ascend #8220"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - w8a8
  - bugfix
  - flashcomm1
  - glm-5
  - precision
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8220"
---

# PR Insight: vllm-project/vllm-ascend #8220

**Title:** [BugFix] Fix quant_bias missing in w8a8_static when flashcomm1 is enabled for GLM-5

## Overview
This PR fixes a precision bug in GLM-5 quantized matrix multiplication when flashcomm1 is enabled. The bug was identified in the w8a8_static quantization method where quant_bias was not added if tp_rank > 0. In the flashcomm1 scenario, all ranks require quant_bias addition, meaning tp_rank=0 should be passed to ensure correct bias application. The fix addresses the root cause of precision issues observed in the o_proj layer.

## Technical Significance
This precision fix is critical for quantized model inference accuracy. The bug caused incorrect results in GLM-5 models using W8A8 quantization with flashcomm1 communication optimization. The fix ensures consistent bias application across all tensor parallel ranks, maintaining quantization accuracy. This PR resolves a fundamental issue in the quantization implementation that affected model output quality.

## Related
- `technique-quantization`
- `technique-flashcomm1`
- `technique-tensor-parallel`