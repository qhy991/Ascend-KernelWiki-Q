---
id: technique-pr-vllm-ascend-6032
title: "PR Insight: vllm-project/vllm-ascend #6032"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - spec-decode
  - aclgraph
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6032"
---

# PR Insight: vllm-project/vllm-ascend #6032

**Title:** [Bugfix] Remove `use_aclgraph` in mtp_proposer and use `use_cuda_graph`

## Overview
This PR removes `use_aclgraph` from mtp_proposer and uses `use_cuda_graph` instead, matching the pattern in eagle_proposer. The fix addresses a scenario where `use_aclgraph=True` while `use_cuda_graph=False` (e.g., with async_scheduling=True) that caused incorrect logic but coincidentally worked.

## Technical Significance
With async_scheduling enabled and deepseek v3.2, `common_attn_metadata.num_input_tokens` must match the tokens entering the model. The old code used `use_aclgraph` which padded num_tokens to num_input_tokens, coinciding with `common_attn_metadata.num_input_tokens` but was incorrect for eager mode. The fix properly updates `common_attn_metadata.num_input_tokens = num_input_tokens` after padding, allowing safe use of `use_cuda_graph` instead.

## Related
- `technique-mtp`, `technique-spec-decode`, `technique-aclgraph`, `technique-async-scheduling`