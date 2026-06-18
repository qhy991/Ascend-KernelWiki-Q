---
id: technique-pr-catlass-89
title: "PR Insight: Ascend/catlass #89"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - catlass
  - documentation
  - block-dispatch
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/89"
---

# PR Insight: Ascend/catlass #89

**Title:** 新增文档Block Dispatch Policies说明

## Overview
This PR adds documentation explaining Block Dispatch Policies in catlass. It clarifies how block-level work distribution is handled across Ascend NPU compute units.

## Technical Significance
Block dispatch policies are critical for optimizing work distribution across cube units and vector units. Understanding these policies enables users to tune performance for different workload shapes and memory access patterns on Ascend hardware.

## Related
- `technique-pipeline-scheduling`
- `hw-cube-unit`