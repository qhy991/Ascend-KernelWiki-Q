---
id: technique-pr-sgl-kernel-npu-202
title: "PR Insight: sgl-project/sgl-kernel-npu #202"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - notify-dispatch
  - uint64
  - optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/202"
---

# PR Insight: sgl-project/sgl-kernel-npu #202

**Title:** notify_dispatch kernel change magic from int32_t to uint64_t

## Overview
Changes the magic value type in notify_dispatch kernel from int32_t to uint64_t to solve integer reversal problems. Performance testing shows minimal impact on A3 architecture and slightly improved notify times on A2 two-server setups.

## Technical Significance
The type change from int32_t to uint64_t prevents integer overflow and reversal issues in the magic value handling, which is critical for correct dispatch notification across large-scale deployments. Performance impact is minimal, with A3 showing no significant change and A2 showing slight notify time improvements while maintaining stable overall performance.

## Related
- `wiki-kernel-moe`
- `wiki-technique-data-type-optimization`
- `wiki-technique-bugfix`
- `wiki-technique-precision`