---
id: technique-pr-mindspeed-1703
title: "PR Insight: Ascend/MindSpeed #1703"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - mc2
  - moe
  - documentation
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1703"
---

# PR Insight: Ascend/MindSpeed #1703

**Title:** mc2 moe operator-shard H doc

## Overview
This PR adds documentation (H doc) for MC2 MoE operator sharding. The documentation explains how MoE operators are sharded across devices in the MC2 parallelism mode.

## Technical Significance
Documentation for operator sharding helps users understand how MoE experts are distributed across Ascend NPUs. This information is critical for configuring parallelism strategies and optimizing performance for MoE workloads.

## Related
- moe-routing techniques
- operator-sharding
- parallelism-strategies