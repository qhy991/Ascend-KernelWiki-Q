---
id: technique-pr-sgl-kernel-npu-10
title: "PR Insight: sgl-project/sgl-kernel-npu #10"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - testing
  - inference
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/10"
---

# PR Insight: sgl-project/sgl-kernel-npu #10

**Title:** add deepep test example

## Overview
This PR adds Python test infrastructure for deep_ep (Deep EP), introducing test scripts and a run_test.sh script. The test_low_latency.py file contains 84 lines of test code for validating Deep EP functionality on Ascend NPU.

## Technical Significance
Adds foundational testing infrastructure for Deep EP inference, enabling validation of inference latency performance. Deep EP is a specialized inference optimization technique, and having proper test harness is critical for verifying kernel correctness and performance characteristics on Ascend hardware.

## Related
- technique-inference-optimization
- technique-performance-testing