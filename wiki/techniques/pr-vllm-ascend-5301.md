---
id: technique-pr-vllm-ascend-5301
title: "PR Insight: vllm-project/vllm-ascend #5301"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - multi-modal
  - qwen
  - disaggregated-encoder
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5301"
---

# PR Insight: vllm-project/vllm-ascend #5301

**Title:** [Test] Add initial multi modal cases of Qwen2.5-VL-7B-Instruct for disaggregated encoder

## Overview
This PR adds end-to-end test cases for Qwen2.5-VL-7B-Instruct with disaggregated encoder deployments on Ascend NPUs. The tests validate that vision-language models work correctly with encoder-decoder separation architecture.

## Technical Significance
Disaggregated encoder deployments separate encoder and decoder computation across different device groups for better resource utilization. Adding comprehensive test cases ensures robustness of multi-modal model inference with this architecture on Ascend hardware.

## Related
- technique-disaggregated-inference
- technique-multi-modal
- technique-encoder-decoder