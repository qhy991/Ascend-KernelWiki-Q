---
id: technique-pr-vllm-ascend-1016
title: "PR Insight: vllm-project/vllm-ascend #1016"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - patch
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1016"
---

# PR Insight: vllm-project/vllm-ascend #1016

**Title:** [Patch] Remove `spec_decode.metrics` patch

## Overview
This PR removes the `spec_decode.metrics` patch that was resolved in upstream vLLM v0.9.0. The patch modified event recording to return device events (NPU Event for vllm-ascend) instead of CUDA events.

## Technical Significance
Removing upstream-resolved patches reduces maintenance burden. The fix indicates that vLLM v0.9.0 properly handles device-agnostic event recording, eliminating the need for Ascend-specific workarounds in the metrics patching layer.

## Related
- `technique-spec-decode`
- `technique-patching`
- `kernel-metrics`