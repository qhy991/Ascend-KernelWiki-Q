---
id: technique-pr-vllm-ascend-10275
title: "PR Insight: vllm-project/vllm-ascend #10275"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - scheduler
  - recompute
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10275"
---

# PR Insight: vllm-project/vllm-ascend #10275

**Title:** [Misc]Fix AttributeError in RecomputeScheduler due to missing routed experts extraction logic

## Overview
This PR fixes a crash in RecomputeScheduler and AsyncRecomputeScheduler when requests finish, caused by a missing `_get_routed_experts()` method. The crash occurs when async scheduling is enabled, a request stops in the current step, and the scheduler attempts to access routed experts information that cannot be extracted. The fix adds the missing routed experts extraction logic to the RecomputeScheduler, ensuring that when `enable_return_routed_experts=True`, routed experts are correctly returned via EngineCoreOutput.

## Technical Significance
This is a critical scheduler correctness fix for MoE workloads using recomputation with async scheduling. The missing method caused crashes when requests completed, making the scheduler unusable in production scenarios. The fix ensures that routed expert information is properly extracted and returned when enabled, supporting downstream operations that depend on expert routing information. This is particularly important for MoE models where understanding which experts were activated is essential for monitoring and optimization.

## Related
- `technique-moe`
- `technique-scheduler`
- `technique-recomputation`