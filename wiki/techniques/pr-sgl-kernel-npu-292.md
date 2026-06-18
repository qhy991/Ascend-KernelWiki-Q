---
id: technique-pr-sgl-kernel-npu-292
title: "PR Insight: sgl-project/sgl-kernel-npu #292"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - moe
  - combine
  - aclnn
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/292"
---

# PR Insight: sgl-project/sgl-kernel-npu #292

**Title:** fix a2 single combine aclnn params

## Overview
Fixes kernel errors caused by inconsistent operator parameters in the A2 single combine interface. The issue was in the ACLNN parameter handling for the combine operation.

## Technical Significance
Parameter consistency is critical for kernel correctness and stability. This fix prevents runtime errors that occur due to parameter mismatches in the A2 single combine interface, ensuring reliable operation for single-server MoE inference scenarios.

## Related
- `wiki-kernel-moe`
- `wiki-technique-aclnn`
- `wiki-technique-bugfix`
- `wiki-hardware-a2`