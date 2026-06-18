---
id: technique-pr-modellink-2216
title: "PR Insight: Ascend/ModelLink #2216"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - training
  - qwen
  - rlhf
  - grpo
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2216"
---

# PR Insight: Ascend/ModelLink #2216

**Title:** 【R1-Zero-qwen复现 Part1】GRPO+多reward

## Overview
Implements GRPO (Group Relative Policy Optimization) with multiple reward models for R1-Zero-qwen reproduction Part 1. This adds the RLHF training infrastructure needed for group-based policy optimization.

## Technical Significance
Enables advanced RLHF training for Qwen models using GRPO with multiple reward signals. This approach can improve training efficiency and model quality by leveraging diverse reward sources during reinforcement learning.

## Related
- technique-hccl-optimization