---
id: technique-pr-samples-2706
title: "PR Insight: Ascend/samples #2706"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - gm
  - bank-conflict-avoidance
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2706"
---

# PR Insight: Ascend/samples #2706

**Title:** add gm conflict case

## Overview
This PR adds a sample demonstrating GM (Global Memory) conflict cases. The example shows scenarios where GM access patterns can lead to conflicts, helping developers understand how to identify and avoid memory contention issues in their kernel implementations.

## Technical Significance
GM conflict cases are critical for performance optimization on Ascend hardware. Understanding how memory access patterns affect bandwidth and avoiding conflicts is essential for achieving high throughput in memory-bound kernels.

## Related
- `technique-bank-conflict-avoidance`
- `hw-global-memory`
- `technique-data-reuse`