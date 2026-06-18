---
id: technique-pr-sgl-kernel-npu-280
title: "PR Insight: sgl-project/sgl-kernel-npu #280"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - hccl
  - tiling
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/280"
---

# PR Insight: sgl-project/sgl-kernel-npu #280

**Title:** Fix the issue of HCCL buffer tiling verification failure during one round of testing.

## Overview
Fixes HCCL buffer tiling verification failures that occurred during single-round testing with specific configurations (bs=1800, HCCL_BUFFSIZE=1536). The issue was caused by not running the ant migration task.

## Technical Significance
Tiling verification is critical for preventing memory allocation failures and ensuring stable MoE operations. This fix prevents runtime errors that occur in specific configuration scenarios, ensuring reliable operation across different batch sizes and HCCL buffer configurations.

## Related
- `wiki-kernel-moe`
- `wiki-technique-hccl-optimization`
- `wiki-technique-tiling`
- `wiki-technique-bugfix`