---
id: technique-pr-sgl-kernel-npu-89
title: "PR Insight: sgl-project/sgl-kernel-npu #89"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - event-sync
  - instruction-queue
  - moe
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/89"
---

# PR Insight: sgl-project/sgl-kernel-npu #89

**Title:** Revert "Separate the buffers used by D/C and notify_dispatch to avoid conflicts"

## Overview
This PR reverts a previous change (#67) that attempted to separate buffers used by dispatch/combine and notify_dispatch operations in the MoE (Mixture of Experts) system. The reversion affects files in the MoE operator kernel including comm_args.h and CAM MoE dispatch/combine normal mode headers.

## Technical Significance
This reversion indicates that the buffer separation approach introduced earlier caused issues, likely related to HCCL communication synchronization or buffer conflicts in the MoE dispatch/combine pipeline. The fix suggests that unified buffer management is more effective for MoE inter-rank communication on Ascend NPUs.

## Related
- `technique-hccl-optimization`, `technique-moe`