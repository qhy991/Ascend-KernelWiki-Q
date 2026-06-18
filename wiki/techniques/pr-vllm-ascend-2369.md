---
id: technique-pr-vllm-ascend-2369
title: "PR Insight: vllm-project/vllm-ascend #2369"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - allgather
  - mc2
  - refactor
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2369"
---

# PR Insight: vllm-project/vllm-ascend #2369

**Title:** refactor allgather/mc2-related fused_experts

## Overview
This PR refactors the allgather/MC2-related fused_experts implementation by creating a new `TokenDispatcher` class. The implementation adds 510 lines to `vllm_ascend/ops/moe_dispatcher/token_dispatcher.py` and comprehensive tests (292 lines) in `tests/ut/ops/test_token_dispatcher.py`.

## Technical Significance
This refactoring improves code organization and maintainability by encapsulating token dispatching logic for different communication patterns (allgather, MC2) into a dedicated class. The better abstraction makes it easier to add new communication strategies and reduces code duplication across different MoE execution paths.

## Related
- `kernel-fused-moe-ascendc`, `technique-moe-communication`, `technique-code-refactor`, `kernel-token-dispatcher`