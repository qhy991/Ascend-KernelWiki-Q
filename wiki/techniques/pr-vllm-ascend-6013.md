---
id: technique-pr-vllm-ascend-6013
title: "PR Insight: vllm-project/vllm-ascend #6013"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - mla
  - fia
  - cann85
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6013"
---

# PR Insight: vllm-project/vllm-ascend #6013

**Title:** [Feat] Remove CP Redundant Variables after FIA operator enables for CANN 8.5

## Overview
This PR removes redundant operations in CP (Context Parallel) after integrating the FIA (Fused In-place Attention) operator in mla_cp._forward_decode with CANN 8.5.0. Previously, extra operations were needed to avoid precision issues when some cards stored no KV cache due to the cp-kv-cache-interleave-size parameter.

## Technical Significance
PCP/DCP splits KV cache across cards with the cp-kv-cache-interleave-size parameter. With too few tokens, some cards get no KV pairs, leading to zeros or corrupted values. CANN 8.5.0's FIA operator handles this correctly, allowing removal of the redundant precision workaround operations. This reduces computational overhead and simplifies the CP implementation. All CI tests pass with CANN 8.5.0, confirming correctness.

## Related
- `technique-context-parallel`, `technique-mla`, `technique-fia`, `technique-cann`