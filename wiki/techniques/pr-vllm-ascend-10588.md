---
id: technique-pr-vllm-ascend-10588
title: "PR Insight: vllm-ascend #10588"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - documentation
  - fix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10588"
---

# PR Insight: vllm-ascend #10588

## Overview
This pull request addresses documentation inaccuracies and missing context within the GLM-5/5.1 tutorial documentation. While it does not introduce code changes to the core system, it improves the developer experience by ensuring paths are correctly specified and architectural concepts are properly introduced.

## Changes Addressed

### Model Cache Path Corrections
The PR corrects typographic errors in the model cache paths used for GLM-5 quantized models:
- Changed the model directory reference from `GLM-5-w4a8` to `GLM5-w4a8`.
- Updated the base cache directory from a generic `/root/.cache/glm5-w8a8` to a standard ModelScope hub path `/root/.cache/modelscope/hub/models/vllm-ascend/GLM5-w8a8`.
This change is crucial for users trying to follow the tutorials verbatim to avoid "file not found" errors during model loading.

### Prefill-Decode Disaggregation Explanation
The PR also adds a brief, conceptual explanation of **Prefill-Decode Disaggregation**. This is a deployment architectural strategy where the computationally intense "prefill" phase (processing the input prompt) and the memory-bandwidth bound "decode" phase (generating output tokens) are separated across different instances or hardware resources. Clarifying this in the documentation helps users better understand and optimize their vLLM deployments for performance.
