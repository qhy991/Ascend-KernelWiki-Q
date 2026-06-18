---
id: technique-pr-mindspeed-2180
title: "PR Insight: Ascend/MindSpeed #2180"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - hccl
  - communication
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2180"
---

# PR Insight: Ascend/MindSpeed #2180

**Title:** refactor：hccl buffer adaptive

## Overview
This PR refactors the HCCL (Huawei Collective Communication Library) buffer adaptive feature. The feature dynamically adjusts HCCL buffer sizes based on communication patterns and memory availability.

## Technical Significance
Adaptive HCCL buffer sizing is a critical optimization for distributed training on Ascend NPUs. By dynamically adjusting buffer sizes, this feature improves memory utilization and reduces communication overhead. Larger buffers can improve throughput for bulk transfers, while smaller buffers reduce memory pressure. The adaptive algorithm likely considers factors such as tensor size, memory availability, and communication frequency to optimize buffer allocation. This optimization is particularly important for hybrid parallel training with complex communication patterns.

## Related
- `technique-hccl-optimization`
- `technique-pipeline-scheduling`