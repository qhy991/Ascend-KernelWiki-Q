---
id: technique-pr-modellink-2356
title: "PR Insight: Ascend/ModelLink #2356"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - swap
  - bugfix
  - memory-optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2356"
---

# PR Insight: Ascend/ModelLink #2356

**Title:** 开启swap特性报错

## Overview
This PR fixes an error that occurs when the swap feature is enabled. The swap feature likely refers to memory swapping between NPU memory and host memory for handling large models that exceed device memory capacity.

## Technical Significance
Memory swapping enables training of models larger than NPU device memory by offloading less frequently accessed tensors to host memory. This is critical for very large models or limited hardware configurations. The bug fix ensures that the swap mechanism correctly handles tensor transfers, memory address mapping, and synchronization between NPU and host memory, preventing crashes or data corruption during training.

## Related
- `technique-memory-optimization`
- `technique-offloading`
- `hw-unified-buffer`