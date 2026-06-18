---
id: technique-pr-modellink-2768
title: "PR Insight: Ascend/ModelLink #2768"
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
  - "https://gitee.com/ascend/ModelLink/pulls/2768"
---

# PR Insight: Ascend/ModelLink #2768

**Title:** add qwen3 moe dir& rename scripts

## Overview
This PR adds support directory structure and scripts for Qwen3 Mixture-of-Experts (MoE) models. It includes renaming existing scripts to accommodate the new MoE variant and organizes the configuration files.

## Technical Significance
Qwen3 MoE represents a state-of-the-art model architecture that benefits significantly from Ascend's computational capabilities. This addition enables training and inference of sparse MoE models on Ascend hardware, leveraging the NPU's efficiency for conditional computation.

## Related
- kernel-attention
- technique-operator-fusion