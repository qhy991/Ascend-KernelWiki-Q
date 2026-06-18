---
id: technique-pr-modellink-2713
title: "PR Insight: Ascend/ModelLink #2713"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - feature
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2713"
---

# PR Insight: Ascend/ModelLink #2713

**Title:** add a3 configuration file

## Overview
This PR adds configuration files for A3 (Ascend Autonomous Architecture) training. The configurations provide settings for distributed training scenarios using A3's communication and parallelism strategies.

## Technical Significance
A3 is Huawei's distributed training framework designed for Ascend hardware. Adding configuration files enables efficient distributed training of large models using A3's optimized communication patterns on Ascend NPUs.

## Related
- technique-hccl-optimization