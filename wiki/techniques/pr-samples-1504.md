---
id: technique-pr-samples-1504
title: "PR Insight: Ascend/samples #1504"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build-system
  - cmake
  - directory-structure
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1504"
---

# PR Insight: Ascend/samples #1504

**Title:** 修改impl目录为${vendor_name}_impl

## Overview
This PR renames the implementation directory to use a vendor-specific naming pattern (${vendor_name}_impl), improving build system organization.

## Technical Significance
Directory structure changes support multi-vendor or multi-backend code organization within the samples repository. Using templated directory names allows the same build system to support different vendor implementations (Ascend, other NPU vendors) or different implementation strategies (TBE vs AscendC vs fallback).

## Related
- `technique-build-system`
- `technique-code-organization`
- `technique-multi-vendor-support`