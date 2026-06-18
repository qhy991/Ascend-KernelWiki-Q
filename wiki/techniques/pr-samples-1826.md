---
id: technique-pr-samples-1826
title: "PR Insight: Ascend/samples #1826"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - memory
  - dvpp
  - samples
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1826"
---

# PR Insight: Ascend/samples #1826

**Title:** 修改多路通道共用一份输入码流内存，减少内存申请

## Overview
This PR modifies a sample to share input stream memory across multiple channels, reducing the number of memory allocations. This optimization applies to multi-channel processing scenarios.

## Technical Significance
Memory optimization is critical for high-throughput inference, especially when processing multiple input streams simultaneously. Sharing memory buffers reduces memory bandwidth pressure and allocation overhead, improving overall system efficiency on memory-bound workloads.

## Related
- `wiki-technique-data-reuse`
- `wiki-technique-memory-optimization`