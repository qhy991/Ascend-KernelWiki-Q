---
id: technique-pr-sgl-kernel-npu-516
title: "PR Insight: sgl-kernel-npu #516"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - build
  - refactor
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/516"
---

# PR Insight: sgl-kernel-npu #516 - Refactor: Separate Submodule Init and Build, Remove CUDA Deps from CI

## Overview
This Pull Request (#516) in the `sgl-project/sgl-kernel-npu` repository addresses Continuous Integration (CI) and build process optimizations. It achieves this by separating the git submodule initialization from the main build phase and removing unnecessary CUDA dependencies from the CI environment.

## Context & Changes
- **Submodule Management Separation**: The initialization and updating of Git submodules have been decoupled from the primary build execution. This separation enables more granular control over environment setup, improving caching efficiency and modularity in CI pipelines.
- **CUDA Dependency Removal**: As `sgl-kernel-npu` is specifically designed for Huawei Ascend NPU architectures, pulling in CUDA dependencies during CI jobs is redundant and bloats the environment. Eliminating these dependencies streamlines the CI pipeline, shrinking runner environment sizes and accelerating job execution times.

## Architectural & Process Impact
- **Performance**: Significant reduction in CI setup time due to lighter container/runner requirements (no NVIDIA/CUDA overhead).
- **Maintainability**: Cleaner build orchestration by explicitly managing submodules before the compilation process begins.
- **Accuracy**: Ensures that the NPU kernel builds strictly rely on Ascend/CANN dependencies without accidental reliance on CUDA-specific libraries or headers.
