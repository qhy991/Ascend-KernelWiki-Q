---
id: technique-pr-catlass-269
title: "PR Insight: catlass #269"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - build
  - mstuner
confidence: inferred
sources:
  - "https://gitee.com/ascend/catlass/pulls/269"
---

# PR Insight: 【mstuner_catlass】x86 compile fix

**Source:** [Catlass PR #269](https://gitee.com/ascend/catlass/pulls/269)

## Overview

This pull request resolves a compilation issue affecting the `mstuner_catlass` utility when built on x86 host architectures. `mstuner_catlass` is the MindStudio Tuner for CATLASS, a tool that automates the generation, compilation, and profiling of Tiling shapes to find the mathematical optimum for matrix multiplication kernels.

## Technical Details

While the Ascend kernels target the NPU, the tooling orchestrating the search space and compilation (such as MSTuner) runs on the host CPU. Ascend development environments can use either ARM or x86 hosts. 

This PR specifically fixes an issue where the `mstuner_catlass` host code encountered build failures on x86 environments. Such compilation issues typically arise from:
- Differences in standard library implementations or missing `#include` directives.
- Strictness differences between x86 and ARM compiler flags.
- Type definitions or architecture-specific macros that fail when compiling host-side C++ code on x86.

### Architectural Impact

This is a **build and tooling bugfix**. It does not alter the underlying Ascend kernel architecture, Tiling algorithms, or performance of Catlass itself. However, it is essential for the developer experience, as many developer workstations, continuous integration (CI) pipelines, and Dockerized build systems run on x86 platforms. By fixing the x86 build, developers can successfully generate and evaluate automated Tiling search spaces across a broader range of host systems.
