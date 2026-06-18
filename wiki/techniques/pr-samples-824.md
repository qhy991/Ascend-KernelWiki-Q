---
id: technique-pr-samples-824
title: "PR Insight: Ascend/samples #824"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - cmake
  - build
  - aicpu
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/824"
---

# PR Insight: Ascend/samples #824

**Title:** fix aicpu cmake

## Overview
This PR fixes CMake configuration issues related to AICPU samples. AICPU is Ascend's CPU-side operator framework, and this fix addresses build problems in AICPU-related sample code.

## Technical Significance
AICPU allows custom operators to run on the CPU side of Ascend systems, complementing NPU-side operators. Fixing CMake configuration for AICPU samples ensures that developers can compile and run custom CPU operator examples. This is important for understanding the full range of operator deployment options on Ascend, including hybrid NPU/CPU execution.

## Related
- AICPU operator development
- CMake configuration for custom operators
- Hybrid NPU/CPU execution
- Custom operator deployment patterns