---
id: technique-pr-vllm-ascend-465
title: "PR Insight: vllm-project/vllm-ascend #465"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - deepseek
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/465"
---

# PR Insight: vllm-project/vllm-ascend #465

**Title:** fix: fix deepseek quant bug

## Overview
This PR fixes a DeepSeek quantization bug by moving scale/offset tensor flattening from model-specific load_weight to the generic quant_method::process_weights_after_loading. The change removes 108 lines from deepseek_v2.py and adds 4 lines to quant config.

## Technical Significance
msmodelslim-generated quantized models require flattened scale/offset tensors. Moving this processing to the quantization framework makes it general instead of model-specific, improving code reuse and correctness.

## Related
- technique-quantization
- technique-deepseek