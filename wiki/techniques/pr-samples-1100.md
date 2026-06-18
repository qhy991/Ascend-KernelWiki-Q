---
id: technique-pr-samples-1100
title: "PR Insight: Ascend/samples #1100"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build-system
  - cross-architecture
  - makefile
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1100"
---

# PR Insight: Ascend/samples #1100

**Title:** 完善acllite makefile 通过架构选择编译器的逻辑

## Overview
This PR improves the ACLLite Makefile by enhancing the logic for selecting compilers based on architecture. The modification ensures the correct compiler is chosen based on the target Ascend architecture.

## Technical Significance
Different Ascend architectures (910, 910B, etc.) may require different compiler flags, libraries, or toolchains. Implementing architecture-aware compiler selection in the Makefile ensures proper compilation across different Ascend NPU generations, improving cross-platform compatibility and build reliability.

## Related
- Build system configuration
- Cross-architecture compilation
- Makefile optimization
- ACLLite build process