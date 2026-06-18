---
id: technique-pr-samples-2137
title: "PR Insight: Ascend/samples #2137"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - add
  - unaligned
  - memory-alignment
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2137"
---

# PR Insight: Ascend/samples #2137

**Title:** 修改非对齐Add样例

## Overview
This PR modifies the unaligned Add sample, updating the implementation or demonstration of how to handle addition operations with non-aligned memory access.

## Technical Significance
Unaligned operations are common in real-world workloads where tensor dimensions don't naturally align to hardware boundaries. Proper handling of these cases is essential for robust operator implementations.

## Related
- `kernel-elementwise`
- `technique-bank-conflict-avoidance`