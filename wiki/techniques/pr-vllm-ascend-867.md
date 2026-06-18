---
id: technique-pr-vllm-ascend-867
title: "PR Insight: vllm-project/vllm-ascend #867"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - mla
  - bugfix
  - v1-engine
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/867"
---

# PR Insight: vllm-project/vllm-ascend #867

**Title:** [Bugfix][Model] Fix fusedmoe and make modelrunner_v1 compatible with latest vllm

## Overview
This PR fixes CI failures caused by vLLM updates by adding moe_config for fused_moe and adjusting KV cache group changes from upstream. The changes ensure backward compatibility with vllm-ascend, which doesn't support multiple KV cache groups.

## Technical Significance
Maintaining compatibility with upstream vLLM changes is critical for vllm-ascend. This PR provides quick fixes for MoE configuration and KV cache handling, ensuring the V1 engine continues to work with the latest vLLM versions while acknowledging that multiple KV cache groups are not yet supported.

## Related
- `kernel-moe`
- `kernel-mla`
- `kv-cache`