---
id: technique-pr-modellink-2256
title: "PR Insight: Ascend/ModelLink #2256"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - qwen
  - rlhf
  - format-control
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2256"
---

# PR Insight: Ascend/ModelLink #2256

**Title:** 【R1-Zero-qwen复现 Part3】strict format

## Overview
Implements strict format control for R1-Zero-qwen reproduction Part 3. This ensures consistent output formatting and adherence to specific format requirements during RLHF training.

## Technical Significance
Improves output quality and consistency for RLHF-trained Qwen models by enforcing strict format constraints. This is important for applications that require predictable and structured model outputs.

## Related
- technique-hccl-optimization