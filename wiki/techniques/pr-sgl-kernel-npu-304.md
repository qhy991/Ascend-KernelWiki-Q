---
id: technique-pr-sgl-kernel-npu-304
title: "PR Insight: sgl-project/sgl-kernel-npu #304"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - ant-migration
  - combine
  - environment-variable
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/304"
---

# PR Insight: sgl-project/sgl-kernel-npu #304

**Title:** Added an environment variable to control whether to enable the Combine Ant Migration feature.

## Overview
Adds environment variable control for the Combine Ant Migration feature, enabled by setting DEEPEP_NORMAL_COMBINE_ENABLE_LONG_SEQ=1. The feature is disabled by default and requires dispatch ant migration service activation.

## Technical Significance
Environment variable control provides operational flexibility for enabling long-sequence support only when needed. This allows users to optimize for their specific use cases without incurring overhead for shorter sequences, while maintaining the ability to enable long-sequence processing when required.

## Related
- `wiki-kernel-moe`
- `wiki-technique-long-sequence`
- `wiki-technique-ant-migration`
- `wiki-technique-configuration`