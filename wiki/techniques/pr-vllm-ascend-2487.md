---
id: technique-pr-vllm-ascend-2487
title: "PR Insight: vllm-project/vllm-ascend #2487"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - alltoallv
  - refactor
  - token-dispatcher
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2487"
---

# PR Insight: vllm-project/vllm-ascend #2487

**Title:** [main] refactor alltoallv in fused_moe

## Overview
This PR refactors all2all-related fused_experts (both quantized and unquantized) into `TokenDispatcherWithAll2AllV`, including dispatch and combine calculation. The implementation adds 298 lines and removes 50 lines from `vllm_ascend/ops/moe_dispatcher/token_dispatcher.py` with comprehensive tests.

## Technical Significance
This refactoring improves code organization by encapsulating alltoall communication patterns into a dedicated token dispatcher class. The better abstraction makes it easier to maintain and extend alltoall-based MoE execution, reducing code duplication across quantized and non-quantized paths.

## Related
- `kernel-fused-moe-ascendc`, `technique-moe-communication`, `technique-code-refactor`, `kernel-token-dispatcher`