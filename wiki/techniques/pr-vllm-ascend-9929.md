---
id: technique-pr-vllm-ascend-9929
title: "PR Insight: vllm-project/vllm-ascend #9929"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moonvit3d
  - dtype
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9929"
---

# PR Insight: vllm-project/vllm-ascend #9929

**Title:** [Ascend950][BugFix] Fix MoonViT3dPretrainedModel.to overriding quantized ViT weight dtype

## Overview
This PR fixes an issue where MoonViT3dPretrainedModel.to() method was overriding quantized ViT weight dtypes incorrectly, potentially breaking quantization precision for vision transformer components.

## Technical Significance
Preserves quantized weight dtypes in MoonViT3dPretrainedModel when calling .to() for dtype conversion. Ensures that quantized ViT weights maintain their correct dtypes rather than being overwritten, maintaining quantization accuracy and preventing precision loss.

## Related
- `technique-quantization`, `kernel-vit`, `pattern-dtype-handling`