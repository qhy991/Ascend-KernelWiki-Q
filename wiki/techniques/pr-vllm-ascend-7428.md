---
id: technique-pr-vllm-ascend-7428
title: "PR Insight: vllm-project/vllm-ascend #7428"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - speculative-decoding
  - lora
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7428"
---

# PR Insight: vllm-project/vllm-ascend #7428

**Title:** [Test] Add a testcase of speculative_decoding + LoRA

## Overview
This PR adds an end-to-end test case combining speculative decoding with LoRA adapters. The test verifies correctness when both techniques are enabled together, ensuring LoRA weights are properly applied in the speculative decoding path.

## Technical Significance
This test matters for validating combined optimization techniques on Ascend. Speculative decoding improves inference speed while LoRA enables efficient model customization. Testing them together ensures the LoRA adapter weights are correctly applied in both target and draft model paths, preventing accuracy regressions when users combine these features.

## Related
- technique-speculative-decoding
- technique-lora