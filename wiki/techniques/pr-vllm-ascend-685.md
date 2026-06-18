---
id: technique-pr-vllm-ascend-685
title: "PR Insight: vllm-project/vllm-ascend #685"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/685"
---

# PR Insight: vllm-project/vllm-ascend #685

**Title:** [ModelRunnerV1] Adapt kv_cache quant in v1.

## Overview
This PR sets self.kv_cache_dtype to kv_cache_spec in model_runner_v1 to support KV cache quantization in the V1 engine. The change is minimal (1 addition, 1 deletion).

## Technical Significance
V1 is vLLM's new execution engine. KV cache quantization support in V1 enables memory-efficient inference with quantized attention on the latest engine, consistent with V0 capabilities.

## Related
- technique-quantization
- technique-kv-cache-paging