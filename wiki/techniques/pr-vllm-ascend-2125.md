---
id: technique-pr-vllm-ascend-2125
title: "PR Insight: vllm-project/vllm-ascend #2125"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - aclgraph
  - communication-optimization
  - strategy-pattern
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2125"
---

# PR Insight: vllm-project/vllm-ascend #2125

**Title:** [1/N][Feat] Support MoE models with ACL Graph and refactor MoE communication logic

## Overview
This PR refactors MoE (Mixture of Experts) communication logic using a strategy pattern by introducing `MoECommMethod` abstract base class. The implementation creates `AllGatherImpl` and adapts ACL Graph handling to cover all scenarios. Changes include new `vllm_ascend/distributed/moe_comm_method.py` (449 lines), updates to `vllm_ascend/ops/fused_moe.py` and `vllm_ascend/worker/model_runner_v1.py`, and tests in `tests/e2e/multicard/moe/test_moe_comm.py`.

## Technical Significance
This architectural decoupling allows easy addition, replacement, or optimization of MoE communication strategies (MC2, AllToAll) without modifying core MoE implementation. The strategy pattern enables future optimizations like W8A8/Int8 models to use `unified_fused_experts`. However, it notes that data-parallel (DP) communication currently doesn't work with vLLM's dispatch/combine mechanisms, requiring alternative approaches.

## Related
- `kernel-fused-moe-ascendc`, `technique-operator-fusion`, `technique-hccl-optimization`, `technique-moe-communication`