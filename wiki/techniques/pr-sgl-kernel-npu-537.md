---
id: technique-pr-sgl-kernel-npu-537
title: "PR Insight: sgl-kernel-npu #537"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build
  - ci
  - bugfix
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/537"
---

# fix: only build deepep if deepep=ON

## Overview
This PR fixes a build crash in the `sgl-kernel-npu` repository that occurs when running `bash build.sh -a kernels` on Ascend 910B (A2) hardware. The build script was unconditionally attempting to generate CMake configurations for the `deepep` module, which caused a crash if the necessary configuration file (`CMakePresets.json`) was missing.

## Changes
The build logic is updated to verify the `$BUILD_DEEPEP_MODULE` environment variable. The `create_deepep_cmake` step and subsequent build operations for `deepep` are now correctly skipped unless `$BUILD_DEEPEP_MODULE` is explicitly set to `ON`.

## Technical Details
Prior to this fix, the build script would proceed into the `create_deepep_cmake` function regardless of whether the user actually intended to build the DeepEP module. During this process, it attempted to copy a `CMakePresets.json` file. When the repository was built for pure kernel compilation (e.g., using `-a kernels`) without DeepEP submodules or dependencies initialized, this file did not exist, leading to an immediate build failure.

By introducing the conditional check, the PR ensures a more robust build process. It properly decouples the module compilation, allowing developers to compile general Ascend kernels without being blocked by DeepEP-specific CMake requirements.
