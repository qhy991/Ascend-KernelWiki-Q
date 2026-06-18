---
id: technique-pr-vllm-ascend-6428
title: "PR Insight: vllm-project/vllm-ascend #6428"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - deployment
  - mooncake
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6428"
---

# PR Insight: vllm-project/vllm-ascend #6428

**Title:** [Image] Bump mooncake version to v0.3.8.post1

## Overview
This PR updates the Mooncake KV cache transfer library to version v0.3.8.post1 across the vllm-ascend Docker images, build scripts, and documentation. Changes include updating Dockerfiles, installation scripts, workflow configurations, and tutorial documentation to use the new Mooncake release.

## Technical Significance
Mooncake is used for distributed KV cache management and transfer in disaggregated inference setups. Keeping the library version synchronized ensures compatibility with the latest KV cache pooling features and fixes. The version bump affects containerized deployments and multi-node inference scenarios where KV cache is shared across instances.

## Related
- `technique-kv-cache-paging`
- `pattern-distributed-inference`
- `technique-kv-offload`