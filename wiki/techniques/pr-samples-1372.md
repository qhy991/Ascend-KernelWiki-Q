---
id: technique-pr-samples-1372
title: "PR Insight: Ascend/samples #1372"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - ctrlcpu
  - bugfix
  - samples
  - cplusplus
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1372"
---

# PR Insight: Ascend/samples #1372

**Title:** 【轻量级 PR】：问题单DTS2022080813673修改ctrlcpu 流程

## Overview
This PR fixes the ctrlcpu flow in the Ascend samples repository to address issue DTS2022080813673. The changes modify how the control CPU interactions are handled in the sample code, ensuring correct flow and execution.

## Technical Significance
Corrects the ctrlcpu flow which is critical for proper control path execution in Ascend samples. This fix likely addresses synchronization or timing issues in the CPU-NPU interaction pattern.

## Related
- `pattern-cpu-npu-sync`
- `technique-event-sync`