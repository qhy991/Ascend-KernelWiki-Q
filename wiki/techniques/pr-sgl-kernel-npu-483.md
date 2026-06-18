---
id: technique-pr-sgl-kernel-npu-483
title: "PR Insight: sgl-kernel-npu #483"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/483"
---

# PR Insight: sgl-kernel-npu #483 - CI: Restore Build Cache for PR CI, with A2 Wheel Fix

## Overview
This PR addresses Continuous Integration (CI) workflows for the `sgl-kernel-npu` repository, specifically targeting improvements in the build cache mechanism for Pull Request checks. In addition to CI performance optimizations, it includes a crucial fix for the "A2 wheel" build process.

## Architectural & Technical Details

### 1. Build Cache Restoration for PR CI
Compiling kernels for the Ascend NPU (both Ascend 910 and 910B) can be a time-consuming process. CI pipelines often suffer from long execution times if they have to compile kernels from scratch on every commit. 
- By **restoring build caches**, the PR significantly reduces the turnaround time for CI checks on Pull Requests.
- This involves preserving intermediate compiled objects or using caching tools (like `ccache` or GitHub Actions cache) so that unchanged files are not recompiled.

### 2. A2 Wheel Fix
The term "A2" generally refers to the Ascend 910B series (or specific Atlas variations).
- Creating Python wheels for hardware accelerators requires careful handling of architecture-specific compiler flags and linked libraries.
- A bug or misconfiguration previously caused issues when packaging the wheel for the A2 architecture.
- This fix ensures that the wheel generation script correctly packages the Ascend A2 kernel binaries, likely by correcting paths, linkage, or adjusting the cache keys to avoid conflicts between different target architectures.

## Impact
- **Developer Productivity:** Faster CI feedback loops for contributors due to cache restoration.
- **Reliability:** Correctly built and packaged wheels for Ascend 910B (A2), ensuring that end users can install the kernels without facing binary incompatibility or missing dependencies.
