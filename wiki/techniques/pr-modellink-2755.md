---
id: technique-pr-modellink-2755
title: "PR Insight: Ascend/ModelLink #2755"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2755"
---

# PR Insight: Ascend/ModelLink #2755

**Title:** [Qwen3]add 4b scripts

## Overview
This PR adds training scripts for the Qwen3 4B model, supporting pretraining, fine-tuning, inference, and evaluation workflows. The scripts are configured to run efficiently on Ascend NPUs.

## Technical Significance
Qwen3 4B is a compact model suitable for efficient inference and fine-tuning. The scripts leverage Ascend's capabilities to enable training on fewer devices while maintaining good throughput and memory efficiency.

## Related
- technique-operator-fusion