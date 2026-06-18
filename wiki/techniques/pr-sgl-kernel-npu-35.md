---
id: technique-pr-sgl-kernel-npu-35
title: "PR Insight: sgl-project/sgl-kernel-npu #35"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - tree-building
  - verification
  - speculative-decoding
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/35"
---

# PR Insight: sgl-project/sgl-kernel-npu #35

**Title:** MTP build tree op and verify tree op

## Overview
This PR adds MTP (multi-token prediction) build tree and verify tree operations with comprehensive test coverage. Includes speculative.py (212 lines) for tree building logic and test suites for build_tree (429 lines) and verify_tree (87 lines) operations.

## Technical Significance
Enables tree-based speculative decoding for MTP inference by providing tree construction and verification operations. Tree-based approaches improve inference throughput by predicting multiple tokens in parallel. The verify operation ensures correctness of speculative predictions.

## Related
- technique-speculative-decoding
- technique-tree-based-decoding
- technique-mtp