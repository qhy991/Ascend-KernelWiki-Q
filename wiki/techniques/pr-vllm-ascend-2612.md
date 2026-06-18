---
id: technique-pr-vllm-ascend-2612
title: "PR Insight: vllm-project/vllm-ascend #2612"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - refactor
  - token-dispatcher
  - code-cleanup
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2612"
---

# PR Insight: vllm-project/vllm-ascend #2612

**Title:** [Refactor][MoE] remove redundant code after refactoring fused_moe

## Overview
This PR removes redundant MoE code following the fused_moe refactoring. Key changes include moving apply_mlp code to a separate file, removing alltoall_buffer and alltoall_seq environment variables and related code, and retaining only the TokenDispatcher inheritance class.

## Technical Significance
The refactoring significantly cleans up MoE implementation by eliminating redundant code and improving code organization. By extracting `moe_mlp.py` (199 new lines) and removing 426 lines from token_dispatcher.py and 405 lines from fused_moe.py, the codebase becomes more maintainable. The removal of alltoall_buffer and alltoall_seq related environment variables simplifies configuration management.

## Related
- `technique-moe`
- `technique-token-dispatcher`
- `technique-refactor`