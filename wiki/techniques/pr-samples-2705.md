---
id: technique-pr-samples-2705
title: "PR Insight: Ascend/samples #2705"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bank-conflict-avoidance
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2705"
---

# PR Insight: Ascend/samples #2705

**Title:** add bank conflict cases

## Overview
This PR adds sample cases demonstrating bank conflicts in memory access patterns. The samples show different scenarios where bank conflicts occur and how to identify them in kernel code, providing practical examples for developers to understand memory access optimization.

## Technical Significance
Bank conflicts are a critical performance bottleneck on NPU architectures. Understanding and avoiding bank conflicts through proper memory access patterns and tiling is essential for achieving optimal kernel performance, especially for memory-bound operations like matrix operations and data transformations.

## Related
- `technique-bank-conflict-avoidance`
- `hw-unified-buffer`
- `technique-data-reuse`