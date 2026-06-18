---
id: technique-pr-vllm-ascend-2565
title: "PR Insight: vllm-project/vllm-ascend #2565"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - long-sequence
  - context-parallel
  - sequence-parallel
  - mla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2565"
---

# PR Insight: vllm-project/vllm-ascend #2565

**Title:** [Feat] long_seq_optim support cp&&sp

## Overview
This PR adds support for context parallel (CP) and sequence parallel (SP) in long sequence optimization. It implements changes across multiple components including MLA attention, scheduler, DeepSeek V2 model, fused MoE ops, and worker implementations to enable parallel processing of long sequences.

## Technical Significance
The feature enables efficient handling of long sequences (128k tokens) by implementing both context parallel and sequence parallel strategies. Key changes include MLA v1 attention optimization, DeepSeek V2 model adaptations, and scheduler enhancements. This allows the framework to distribute long sequence processing across multiple NPU devices, improving throughput and enabling support for larger context windows.

## Related
- `technique-context-parallel`
- `technique-sequence-parallel`
- `technique-mla`