---
id: technique-pr-vllm-ascend-2647
title: "PR Insight: vllm-project/vllm-ascend #2647"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - qwen3-moe
  - tensor-parallel
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2647"
---

# PR Insight: vllm-project/vllm-ascend #2647

**Title:** [0.9.1][Bugfix][Aclgraph] Fix qwen3-moe + aclgraph + tp

## Overview
This PR fixes Qwen3 MoE + ACL Graph + tensor parallel (TP) compatibility issues. Previously, Qwen3 MoE with ACL Graph only supported pure TP scenarios due to ACL Graph limitations supporting only allgather in v0.9.1-dev.

## Technical Significance
The fix enables ACL Graph to work with Qwen3 MoE in pure TP scenarios by switching to `AscendSparseMoeBlock`. This resolves compatibility issues between Qwen3 MoE implementation and ACL Graph's communication pattern limitations, allowing users to run Qwen3 MoE with ACL Graph enabled in pure TP configurations.

## Related
- `technique-aclgraph`
- `technique-qwen3-moe`
- `technique-tensor-parallel`