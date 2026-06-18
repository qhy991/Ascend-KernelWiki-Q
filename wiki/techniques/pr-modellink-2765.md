---
id: technique-pr-modellink-2765
title: "PR Insight: Ascend/ModelLink #2765"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - qwen3
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2765"
---

# PR Insight: Ascend/ModelLink #2765

**Title:** add qwen3 14b

## Overview
This PR adds training and evaluation scripts for the Qwen3 14B model. The scripts include configurations for pretraining, fine-tuning, inference, and evaluation, optimized for Ascend hardware.

## Technical Significance
Qwen3 14B represents a balance between model capability and resource requirements. The scripts leverage Ascend's computational efficiency to enable distributed training with appropriate parallelism strategies for this mid-sized model.

## Related
- technique-operator-fusion