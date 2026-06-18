---
id: technique-pr-vllm-ascend-6902
title: "PR Insight: vllm-project/vllm-ascend #6902"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - dynamic-dimensions
  - glm5
  - tiling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6902"
---

# PR Insight: vllm-project/vllm-ascend #6902

**Title:** [feat] parameterize hardcoded MLA dimensions to support GLM5-W8A8

## Overview
Parameterizes MLA (Multi-Layer Attention) dimension constants by deriving them from tensor shapes at runtime instead of hardcoding DeepSeek V3 values. The implementation adds 9 dimension fields to MlaTilingData, adds OpParam fields, dynamizes host-side tiling functions, and derives dimensions from wuk, gamma1, and kv_cache_rope tensor shapes.

## Technical Significance
Enables MLA preprocessing operators to work with both DeepSeek V3 and GLM5 models without Python API changes. The runtime dimension derivation replaces 310+ hardcoded constants across 4 kernel files, improving maintainability and model compatibility.

## Related
- `technique-mla`, `technique-tiling`, `technique-dynamic-kernels`, `technique-model-agnostic`