---
id: technique-pr-modellink-2663
title: "PR Insight: Ascend/ModelLink #2663"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - qwen
  - feature
  - training
  - poc
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2663"
---

# PR Insight: Ascend/ModelLink #2663

**Title:** add qwen3-235b and qwen3-32b poc scripts

## Overview
This PR adds proof-of-concept (PoC) training scripts for Qwen3 models with 235B and 32B parameters. These scripts demonstrate how to train large-scale Qwen3 models using ModelLink on Ascend hardware.

## Technical Significance
Qwen3 is an important LLM architecture, and PoC scripts for both medium (32B) and very large (235B) parameter scales help users understand training workflows at different model sizes. This support enables exploration of Qwen3 training on Ascend NPUs across a range of model scales.

## Related