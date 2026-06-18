---
id: technique-pr-samples-1276
title: "PR Insight: Ascend/samples #1276"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - jpeg
  - memory-management
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1276"
---

# PR Insight: Ascend/samples #1276

**Title:** 【轻量级 PR】：JPEGE支持用户配置输出内存

## Overview
This PR adds support for user-configurable output memory in the JPEGE (JPEG Encoder) sample. This allows applications to specify their own memory buffers for encoded output.

## Technical Significance
User-configurable output memory is an important optimization for inference pipelines, enabling zero-copy or reduced-copy workflows. For Ascend inference applications, this can reduce data movement between device memory (unified buffer) and host memory, improving overall throughput and reducing latency in image processing pipelines.

## Related
- hw-unified-buffer
- technique-data-reuse