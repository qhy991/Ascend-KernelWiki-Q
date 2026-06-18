---
id: technique-pr-vllm-ascend-8174
title: "PR Insight: vllm-project/vllm-ascend #8174"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - c8
  - glm4.7
  - graph-mode
  - pd-separation
  - kv-cache
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8174"
---

# PR Insight: vllm-project/vllm-ascend #8174

**Title:** [Feature] Supports GLM4.7 C8 scenarios

## Overview
This PR adds C8 quantization scenario support for GLM4.7 models, introducing graph mode and layerwise branching for PD (Prefill-Decode) separation. The implementation modifies attention, KV transfer, and quantization configuration to support C8 parameters. Extending C8 support to other GQA models requires adding their specific C8 quantization parameters to `patch_gqa_c8.py`. MTP support is not currently included.

## Technical Significance
The addition of C8 quantization support for GLM4.7 enables efficient inference with reduced memory footprint while maintaining accuracy. The graph mode and layerwise branching for PD separation optimize execution for prefill and decode phases respectively. This PR provides a framework for adding C8 support to other GQA models by updating the configuration with model-specific parameters.

## Related
- `technique-quantization`
- `technique-kv-cache-optimization`
- `technique-graph-mode`