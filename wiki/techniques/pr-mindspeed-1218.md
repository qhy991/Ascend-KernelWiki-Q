---
id: technique-pr-mindspeed-1218
title: "PR Insight: Ascend/MindSpeed #1218"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - moe
  - zero-memory
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1218"
---

# PR Insight: Ascend/MindSpeed #1218

**Title:** 迁移moe-zero-memory & tp-extend-ep文档

## Overview
This PR migrates documentation for MoE zero-memory and tp-extend-ep features. MoE zero-memory reduces memory usage in Mixture of Experts models, while tp-extend-ep likely extends tensor parallelism with expert parallelism.

## Technical Significance
Documentation migration ensures users have access to accurate information about advanced MindSpeed features. MoE zero-memory and tensor+expert parallelism are important for scaling large MoE models on Ascend clusters, and proper documentation helps users adopt these optimizations effectively.

## Related
- kernel-moe
- technique-communication-optimization