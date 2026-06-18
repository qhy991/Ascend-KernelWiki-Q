---
id: technique-pr-vllm-ascend-6941
title: "PR Insight: vllm-project/vllm-ascend #6941"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - multimodal
  - gdn
  - layer-detection
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6941"
---

# PR Insight: vllm-project/vllm-ascend #6941

**Title:** [BugFix] Improve GDN layer detection for multimodal models

## Overview
Enhances `check_gdn_layer()` function to properly detect GDN layers in multimodal models by adding support for checking `text_config.layer_types` in addition to root-level `layer_types`. Fixes potential None reference errors when `layer_types` attribute is missing by replacing `hasattr()` checks with safer `getattr()` approach and adding fallback to empty list.

## Technical Significance
Fixes GDN layer detection in multimodal models like Qwen-Omni where layer type information is nested under `text_config`. The safer attribute access prevents errors when `layer_types` is None, improving robustness across different model configurations.

## Related
- `technique-gdn`, `technique-multimodal`, `technique-model-detection`