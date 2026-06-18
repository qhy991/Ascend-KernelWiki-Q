---
id: technique-pr-vllm-ascend-9933
title: "PR Insight: vllm-project/vllm-ascend #9933"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moonvit3d
  - dtype
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9933"
---

# PR Insight: vllm-project/vllm-ascend #9933

**Title:** [Ascend950][BugFix] Fix MoonViT3dPretrainedModel.to overriding quantized ViT weight dtype

## Overview
This PR is identical to #9929, fixing the same issue of MoonViT3dPretrainedModel.to() overriding quantized ViT weight dtypes incorrectly. It may be a backport or duplicate fix for different maintenance branches.

## Technical Significance
Ensures consistency of quantized ViT weight dtype handling across branches by backporting the same fix. Prevents quantization precision issues in production deployments using different maintenance branches.

## Related
- `technique-quantization`, `kernel-vit`, `pattern-dtype-handling`