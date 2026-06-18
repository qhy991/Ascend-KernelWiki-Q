---
id: technique-pr-samples-2391
title: "PR Insight: Ascend/samples #2391"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - cube-group
  - barrier
  - synchronization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2391"
---

# PR Insight: Ascend/samples #2391

**Title:** add cube_group_barrier

## Overview
This PR adds a cube_group_barrier sample, demonstrating how to use barrier synchronization across cube unit groups in AscendC. This is essential for coordinating parallel execution when multiple cube units work together on a single kernel.

## Technical Significance
Barrier synchronization is a critical primitive for parallel kernel programming on Ascend. Understanding how to synchronize cube groups enables developers to implement more complex parallel algorithms and avoid race conditions in multi-unit computations.

## Related
- `hw-cube-unit`, `technique-event-sync`