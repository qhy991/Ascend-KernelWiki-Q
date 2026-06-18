---
id: technique-pr-vllm-ascend-8304
title: "PR Insight: vllm-project/vllm-ascend #8304"
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
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8304"
---

# PR Insight: vllm-project/vllm-ascend #8304

**Title:** [BugFix][0.18.0] Fix quant_bias missing in w8a8_static when flashcomm1 is enabled for GLM-5

## Overview
This PR backports the quant_bias fix from #8220 to the v0.18.0 release branch. The bug was identified in the w8a8_static quantization method where quant_bias was not added if tp_rank > 0. In the flashcomm1 scenario, all ranks require quant_bias addition, meaning tp_rank=0 should be passed to ensure correct bias application for GLM-5 models.

## Technical Significance
This cherry-pick ensures consistency between main and release branches for quantization precision fixes. The bug fix is critical for GLM-5 quantized model inference accuracy when using flashcomm1 communication optimization. Maintaining the fix across release branches ensures users benefit from the precision improvements regardless of vLLM version.

## Related
- `technique-quantization`
- `technique-flashcomm1`
- `technique-tensor-parallel`