---
id: technique-pr-modellink-2766
title: "PR Insight: Ascend/ModelLink #2766"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - moe
  - qwen3
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2766"
---

# PR Insight: Ascend/ModelLink #2766

**Title:** add qwen3-moe-30b

## Overview
This PR adds training, fine-tuning, and evaluation scripts for the Qwen3-MoE 30B model. It includes configuration files and pipelines to support this large-scale Mixture-of-Experts model on Ascend hardware.

## Technical Significance
Qwen3-MoE 30B is a large MoE model that benefits from Ascend's computational efficiency. The MoE architecture enables high performance with sparse activation, making it well-suited for Ascend NPUs which excel at conditional computation.

## Related
- kernel-attention
- technique-operator-fusion