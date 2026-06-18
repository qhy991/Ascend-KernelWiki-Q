---
id: technique-pr-vllm-ascend-8038
title: "PR Insight: vllm-project/vllm-ascend #8038"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - prefill-context-parallel
  - multimodal
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8038"
---

# PR Insight: vllm-project/vllm-ascend #8038

**Title:** [Feature][PCP][MM] Support multimodel reasoning when prefill context parallel feature is on

## Overview
This PR fixes a precision issue in multimodel reasoning when prefill context parallel (PCP) feature is enabled on NPU. The implementation updates `vllm_ascend/worker/model_runner_v1.py` and `vllm_ascend/worker/pcp_utils.py` to properly handle multimodal inputs with PCP. The fix ensures correctness for both text-only and multimodal (text+image) reasoning cases when PCP is active.

## Technical Significance
Multimodal reasoning with context parallelism is critical for scaling large vision-language models on Ascend clusters. The bug likely arose from incorrect tensor partitioning or synchronization of multimodal feature tensors across the PCP group. The fix enables accurate multimodel inference at scale by properly coordinating the multimodal processing pipeline with the distributed context parallel computation, ensuring that vision features are correctly distributed and processed across devices.

## Related
- `kernel-attention` (Attention with PCP)
- `pattern-multimodal` (Vision-language processing)
- `technique-context-parallel` (Prefill context parallelism)