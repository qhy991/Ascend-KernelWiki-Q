---
id: technique-pr-vllm-ascend-9089
title: "PR Insight: vllm-project/vllm-ascend #9089"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - testing
  - sfa
  - mla
  - precision-validation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9089"
---

# PR Insight: vllm-project/vllm-ascend #9089

**Title:** [Test] add attention ut for sfa_v1 and mla_cp

## Overview
This PR adds comprehensive precision unit tests for Ascend attention implementations, specifically covering `AscendSFAImpl` (SFA v1) and `AscendMlaCPImpl` (MLA with Context Parallel). The tests compare NPU kernel outputs against fp32 reference implementations across multiple scenarios: pure decode, pure prefill, mixed decode/prefill, and MTP speculative decoding with both bf16/fp16 dtypes and tensor parallel sizes 1, 2, and 4.

## Technical Significance
The addition of precision testing ensures numerical correctness of attention kernels across different execution modes. By testing both SFA and MLA implementations with context parallelism, the test suite validates that attention computations maintain accuracy across different architectural optimizations and workload patterns. The tests also support DeepSeek-V3.2-Exp model configurations with proper handling of `hf_overrides` and `hf_config_override`.

## Related
- `kernel-attention-ascendc`, `technique-flash-attention`, `technique-context-parallel`, `kernel-mla-ascendc`