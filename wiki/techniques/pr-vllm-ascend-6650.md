---
id: technique-pr-vllm-ascend-6650
title: "PR Insight: vllm-project/vllm-ascend #6650"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - tensor-parallel
  - fully-sharded-loras
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6650"
---

# PR Insight: vllm-project/vllm-ascend #6650

**Title:** [Bugfix][LoRA] Fix the issue when enable LoRA + tp + fully_sharded_loras

## Overview
This PR fixes issue #6143 by enabling server startup with --enable-lora, --fully-sharded-loras, and --tensor_parallel_size 2 simultaneously. The fix addresses compatibility issues between LoRA sharding and tensor parallelism configurations.

## Technical Significance
Enables complex distributed LoRA configurations combining tensor parallelism and fully sharded LoRA adapters. This provides flexibility for large-scale deployments requiring both parameter and data parallelism strategies.

## Related
- `technique-lora`