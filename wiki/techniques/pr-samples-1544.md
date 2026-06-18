---
id: technique-pr-samples-1544
title: "PR Insight: Ascend/samples #1544"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - memcpy
  - host-device
  - async
  - memory-management
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1544"
---

# PR Insight: Ascend/samples #1544

**Title:** memcpy_host_device_async_cpp添加

## Overview
This PR adds a C++ sample demonstrating asynchronous memory copy between host and device, a critical operation for overlapping data transfer with computation.

## Technical Significance
Asynchronous host-device memory transfers are essential for achieving high throughput in inference pipelines. By overlapping data transfer with kernel execution using streams and events, developers can hide memory bandwidth latency. This sample demonstrates proper stream management, async memcpy API usage, and synchronization patterns.

## Related
- `technique-async-execution`
- `technique-double-buffering`
- `technique-event-sync`
- `technique-memory-management`
- `hw-hccs`