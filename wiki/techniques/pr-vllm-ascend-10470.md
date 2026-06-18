---
id: technique-pr-vllm-ascend-10470
title: "PR Insight: vllm-ascend #10470"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - misc
  - doc
  - telemetry
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm/pull/10470"
---

# PR Insight: vllm-ascend #10470

**Title:** [Misc] modify gitignore & remove out of date doc & add report_usage_stats in init_device

This PR introduces three minor maintenance updates to the `vllm-ascend` codebase to improve development workflow, documentation accuracy, and worker initialization consistency.

## 1. Gitignore Update for Custom Ops
Added the `build_out` directory to `.gitignore`. This is typically used to prevent temporary build artifacts generated during the compilation of custom Ascend operators from being accidentally committed to the repository.

## 2. Documentation Cleanup
Removed outdated content from `optimization_and_tuning.md`. Keeping documentation synchronized with the current state of the codebase ensures that users have accurate guidance when tuning performance on Ascend hardware.

## 3. Worker Initialization Consistency
Added `report_usage_stats` to the `worker.init_device` function. This change aligns the Ascend NPU worker initialization behavior with the standard `gpu_worker` in vLLM. Usage statistics reporting helps track framework and hardware utilization, ensuring consistent metrics collection across different accelerator backends.
