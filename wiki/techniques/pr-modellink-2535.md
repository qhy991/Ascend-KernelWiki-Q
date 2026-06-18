---
id: technique-pr-modellink-2535
title: "PR Insight: Ascend/ModelLink #2535"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mla
  - communication-hiding
  - recompute
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2535"
---

# PR Insight: Ascend/ModelLink #2535

**Title:** 【feature】【master】支持MLA TP 通信隐藏 + MLA up proj 重计算

## Overview
This PR adds support for Multi-Head Latent Attention (MLA) with tensor parallelism communication hiding and up-projection recomputation. MLA is a memory-efficient attention mechanism used in some modern LLM architectures.

## Technical Significance
Communication hiding in TP reduces synchronization overhead, improving training throughput on Ascend hardware. Recomputing the up-projection saves memory at the cost of additional computation, which is beneficial for memory-constrained training scenarios.

## Related
- MLA (Multi-Head Latent Attention)
- tensor parallelism optimization
- activation recomputation