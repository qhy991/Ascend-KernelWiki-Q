---
id: technique-pr-vllm-ascend-8736
title: "PR Insight: vllm-project/vllm-ascend #8736"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - specdecode
  - eagle
  - quarot
  - bugfix
  - cpu-offload
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8736"
---

# PR Insight: vllm-project/vllm-ascend #8736

**Title:** [SpecDecode][BugFix] Fix draft quarot model loading timeout due to float16 matmul bug on CPU

## Overview
This PR fixes a model loading timeout issue when loading EAGLE draft models for QUAROT models on CPU. The root cause is a bug in PyTorch's float16 matmul operation on CPU that causes indefinite hangs. The fix temporarily casts tensors to float32 before matmul operations and casts back to the original dtype afterward.

## Technical Significance
This fix prevents model loading failures when using QUAROT (Quantization-Aware Rotation of Transformed Tensors) with EAGLE speculative decoding. QUAROT is a quantization technique that enables efficient storage of rotated KV caches. The CPU-side float16 matmul bug is a PyTorch issue that affects model initialization when draft models are loaded on CPU before being transferred to NPU. The workaround ensures reliable model loading for speculative decoding workflows.

## Related
- `pattern-specdecode`
- `technique-kv-cache-paging`
- `technique-format-conversion`