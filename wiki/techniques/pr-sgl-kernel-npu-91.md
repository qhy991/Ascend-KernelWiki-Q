---
id: technique-pr-sgl-kernel-npu-91
title: "PR Insight: sgl-project/sgl-kernel-npu #91"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - unified-buffer
  - moe
  - event-sync
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/91"
---

# PR Insight: sgl-project/sgl-kernel-npu #91

**Title:** Reapply fix for hccl buffer use and verify

## Overview
This PR reapplies and verifies a fix for HCCL buffer usage in the MoE (Mixture of Experts) dispatch and combine operations. It updates tiling code, kernel headers, and communication arguments to ensure proper buffer management for inter-rank communication.

## Technical Significance
The fix addresses HCCL buffer management issues in MoE operations, likely resolving conflicts between dispatch and combine phases. This is critical for performance in multi-rank MoE inference where HCCS communication bottlenecks directly impact throughput. The reapplication after the reversion in PR #89 suggests a refined approach to buffer sharing.

## Related
- `technique-hccl-optimization`, `technique-moe`, `hw-hccs`