---
id: technique-pr-vllm-ascend-2962
title: "PR Insight: vllm-project/vllm-ascend #2962"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - long-sequence
  - operator-optimization
  - memory-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2962"
---

# PR Insight: vllm-project/vllm-ascend #2962

**Title:** [Perf] Add new npu_fused_infer_attention_score op to improve perfomance in splitfuse cases and resolve long-seq mask problems

## Overview
This PR adds a new npu_fused_infer_attention_score operator to improve performance in splitfuse scenarios and resolve memory issues with ultra-long sequences (128k). The new operator supports fixed-size compressed masks, avoiding excessive CPU memory consumption from large attention mask allocations.

## Technical Significance
The new operator addresses two critical issues: performance optimization for splitfuse cases and memory management for long sequences. By supporting compressed masks, it prevents CPU OOM when max_model_len reaches 128k. The implementation uses version checks to ensure backward compatibility until future CANN versions are available.

## Related
- `kernel-attention-ascendc`, `technique-chunked-prefill`, `technique-memory-optimization`