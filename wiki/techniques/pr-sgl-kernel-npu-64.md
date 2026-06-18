---
id: technique-pr-sgl-kernel-npu-64
title: "PR Insight: sgl-project/sgl-kernel-npu #64"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - tree-ops
  - speculative-decoding
  - refactoring
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/64"
---

# PR Insight: sgl-project/sgl-kernel-npu #64

**Title:** Update speculative tree ops

## Overview
This PR updates speculative tree operations in speculative.py, modifying tree construction and management logic for MTP speculative decoding. Changes focus on tree operator implementations and data flow.

## Technical Significance
Improves speculative decoding correctness and performance by refining tree operation logic. Tree-based speculative decoding requires precise tree management to ensure correct token prediction and verification, essential for achieving inference throughput improvements.

## Related
- technique-speculative-decoding
- technique-tree-based-decoding
- technique-mtp