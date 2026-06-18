---
id: technique-pr-vllm-ascend-10199
title: "PR Insight: vllm-project/vllm-ascend #10199"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pipeline-parallel
  - speculative-decoding
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10199"
---

# PR Insight: vllm-project/vllm-ascend #10199

**Title:** [BugFix] Fix the verification when pipeline parallel + mtp in PD disaggregation scenario

## Overview
This PR backports vLLM Pipeline Parallel (PP) + Multi-Token Prediction (MTP) speculative decoding support for NPU, introducing patches to handle model runner output alignment, post-step scheduling, and model config validation. It ensures that local Eagle/MTP drafters are validated with pipeline parallel size of 1 on the last PP stage, and that speculative token IDs are correctly tracked and propagated through the scheduler and model runner. The fix addresses issues with in-place slicing of `request.spec_token_ids`, potential `KeyError` in distributed environments, and import compatibility for `MTPModelTypes`.

## Technical Significance
This is a critical distributed inference fix for PP+MTP scenarios on Ascend. The PR resolves several correctness issues in speculative decoding when combined with pipeline parallelism: preventing duplicate scheduling through proper token ID handling, avoiding crashes in distributed environments with safer dictionary access, and maintaining compatibility across vLLM versions. The patches ensure that MTP virtual tokens are properly tracked across PP stages and that the scheduler correctly handles speculative token propagation in the disaggregated PD scenario.

## Related
- `technique-speculative-decoding`
- `technique-pipeline-parallel`
- `technique-mtp`