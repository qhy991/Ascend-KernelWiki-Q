---
id: technique-pr-modellink-2324
title: "PR Insight: Ascend/ModelLink #2324"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - hunyuanlargemoe
  - scripts
  - moe
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2324"
---

# PR Insight: Ascend/ModelLink #2324

**Title:** 【HunyuanLargeMoE】shell files

## Overview
This PR adds shell script files for HunyuanLargeMoE model training. The scripts provide configuration templates for running Hunyuan's large-scale Mixture-of-Experts models on Ascend hardware.

## Technical Significance
HunyuanLargeMoE represents a very large MoE model requiring sophisticated distributed training strategies. The shell scripts configure tensor parallelism, expert parallelism, and data parallelism for optimal NPU utilization across large Ascend clusters. Proper MoE training requires load balancing, expert communication optimization, and memory management strategies specific to large-scale expert models on Ascend NPUs.

## Related
- `technique-moe-training`
- `technique-expert-parallelism`
- `technique-load-balancing`