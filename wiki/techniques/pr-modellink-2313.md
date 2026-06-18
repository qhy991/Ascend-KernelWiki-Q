---
id: technique-pr-modellink-2313
title: "PR Insight: Ascend/ModelLink #2313"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - weight-conversion
  - deepseek3
  - vpp
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2313"
---

# PR Insight: Ascend/ModelLink #2313

**Title:** 新增deepseekv3权重转换vpp功能

## Overview
Adds VPP (Virtual Parallel Pipeline) weight conversion functionality for DeepSeekV3. This enables weight transformation and distribution for DeepSeekV3 models using the VPP parallelism strategy.

## Technical Significance
Enables advanced training configurations for DeepSeekV3 by supporting VPP weight conversion. VPP is a sophisticated parallelism strategy that can improve training efficiency for very large models on distributed NPU clusters.

## Related
- technique-moe
- technique-hccl-optimization