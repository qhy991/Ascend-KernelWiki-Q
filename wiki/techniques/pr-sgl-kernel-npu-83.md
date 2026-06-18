---
id: technique-pr-sgl-kernel-npu-83
title: "PR Insight: sgl-project/sgl-kernel-npu #83"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - dispatch
  - combine
  - memory-verification
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/83"
---

# PR Insight: sgl-project/sgl-kernel-npu #83

**Title:** Fix the memory verification issue within intranode dispatch

## Overview
This PR fixes memory verification issues in intranode dispatch by validating total memory usage across all operators sharing the same communication group. Updates tiling logic in dispatch and combine normal operations to account for shared communication domain memory constraints.

## Technical Significance
Resolves memory verification failures that could cause incorrect resource allocation in distributed MoE inference. Proper accounting of shared communication domain memory is essential for preventing memory exhaustion and ensuring correct execution of intranode dispatch/combine operations.

## Related
- technique-memory-verification
- technique-intranode-communication
- technique-communication-domain