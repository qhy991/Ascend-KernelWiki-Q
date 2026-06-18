---
id: technique-pr-vllm-ascend-6624
title: "PR Insight: vllm-project/vllm-ascend #6624"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - lora
  - testing
  - e2e-test
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6624"
---

# PR Insight: vllm-project/vllm-ascend #6624

**Title:** [Test][LoRA] Add e2e test for base model inference

## Overview
This PR adds an end-to-end test case to verify base model inference correctness when LoRA is enabled. The test calls do_sample with lora_id=0 to target the base model and validates outputs against expected results, ensuring no regression after fixing previous LoRA base model issues.

## Technical Significance
Adds test coverage for LoRA+base model mixed inference scenarios, preventing future regressions. The test ensures correct behavior when switching between LoRA and base model requests in the same deployment.

## Related
- `technique-lora`