---
id: technique-pr-vllm-ascend-10469
title: "PR Insight: vllm-ascend #10469"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - bugfix
  - deepseek
  - test
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10469"
---

# PR Insight: vllm-ascend #10469

## Overview

This PR addresses a testing failure in the DeepSeek nightly CI pipeline caused by the slow loading speed of large model weights.

## Issue Addressed

During nightly tests for DeepSeek models (specifically `dsv3.1-bf16` and `dsr1-0528-w8a8`), the initialization phase often exceeds default timeouts due to the massive size of the model weights. The slow weight loading process triggers a test case failure before the engine is fully ready to process inference requests.

## Solution

A new environment variable timeout setting `VLLM_ENGINE_READY_TIMEOUT_S: "3000"` (3000 seconds) is introduced in the nightly test configuration for the affected test cases. This gives the vLLM engine ample time (up to 50 minutes) to load the large parameter set into the Ascend NPU's memory before the test framework marks the initialization as failed. 

This fix makes the CI robust against expected delays when testing models with very large numbers of parameters.
