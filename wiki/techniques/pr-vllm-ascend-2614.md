---
id: technique-pr-vllm-ascend-2614
title: "PR Insight: vllm-project/vllm-ascend #2614"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - moe
  - quantization
  - all-to-all
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2614"
---

# PR Insight: vllm-project/vllm-ascend #2614

**Title:** [3/N][Feat][Graph] Support `all-to-all` and quantized models with ACL Graph

## Overview
This PR adds support for all-to-all communication and quantized models with ACL Graph for MoE operations. It unifies execution paths, adds W8A8 dynamic quantization support, implements weight pre-processing, and enables dynamic communication method selection based on token count and SoC version.

## Technical Significance
The feature significantly improves MoE performance by enabling all-to-all communication for large token counts, which is more efficient than all-gather on modern hardware. The unified execution path reduces code duplication while W8A8 dynamic quantization support enables efficient quantized MoE inference. Dynamic communication selection optimizes performance by choosing between mc2, allgather, or alltoall based on runtime conditions.

## Related
- `technique-moe`
- `technique-aclgraph`
- `technique-quantization`
- `technique-all-to-all`