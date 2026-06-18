---
id: technique-pr-vllm-ascend-10587
title: "PR Insight: vllm-ascend #10587"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10587"
---

# PR Insight: vllm-ascend #10587

## Overview

**Title:** [CI] Modify weekly failed test case: Qwen3.5-122B-A10B-W8A8-A3.yaml
**Repository:** vllm-project/vllm-ascend
**PR Number:** 10587
**URL:** [vllm-ascend#10587](https://github.com/vllm-project/vllm-ascend/pull/10587)

## Description

This PR is a routine CI (Continuous Integration) maintenance update addressing a failing weekly test case. Specifically, it modifies the end-to-end (e2e) configuration for testing the **Qwen3.5-122B-A10B-W8A8-A3** model under Ascend's continuous testing environment.

### Key Changes
- Modifies the weekly e2e test configuration: `tests/e2e/weekly/single_node/configs/Qwen3.5-122B-A10B-W8A8-A3.yaml`
- Corrects parameters or thresholds within the test case to ensure the periodic testing for this specific Qwen 3.5 122B configuration (W8A8 quantized for Ascend) passes reliably.

### Impact
This PR does not introduce any user-facing code changes. Its primary goal is to improve the stability and reliability of the `vllm-ascend` automated testing pipeline for large quantized models on Huawei Ascend NPU environments.
