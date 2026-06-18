---
id: technique-pr-vllm-ascend-2075
title: "PR Insight: vllm-project/vllm-ascend #2075"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - moe
  - quantization
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2075"
---

# PR Insight: vllm-project/vllm-ascend #2075

**Title:** [0.9.1][bugfix] fix bf16 multistream

## Overview
This PR fixes shape conflicts between shared and routed experts for DeepSeek models when tensor parallel size > 1 and multistream MoE is enabled. It also resolves interface conflicts for DeepSeek BF16 models introduced by a previous optimization.

## Technical Significance
The fix ensures correct tensor shapes for expert routing in multistream scenarios, which is critical for distributed MoE inference with BF16 precision. This resolves runtime errors and maintains performance benefits of multistream MoE execution on Ascend NPU.

## Related
- `technique-moe`
- `technique-quantization`
- `kernel-deepseek-moe`
- `technique-multistream`