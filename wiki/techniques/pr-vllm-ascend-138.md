---
id: technique-pr-vllm-ascend-138
title: "PR Insight: vllm-project/vllm-ascend #138"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
  - framework-overhead
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/138"
---

# PR Insight: vllm-project/vllm-ascend #138

**Title:** [Model Runner][Performance] Cache the jugement result of is_encoder_decoder to decrease framework overhead

## Overview
This PR caches the is_encoder_decoder status in ModelInputForNPUBuilder.__init__ to avoid repeated deep call stack traversals. The change reduces CPU framework overhead during model execution.

## Technical Significance
Framework overhead reduction is critical for inference throughput. By caching the encoder-decoder model flag, the PR eliminates redundant attribute lookups through the model_config hierarchy, saving CPU cycles in the hot model runner path.

## Related
- technique-framework-overhead