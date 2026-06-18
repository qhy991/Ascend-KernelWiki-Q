---
id: technique-pr-cann-ops-adv-318
title: "PR Insight: Ascend/cann-ops-adv #318"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build
  - cmake
  - compilation
  - infrastructure
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/318"
---

# PR Insight: Ascend/cann-ops-adv #318

**Title:** Fix single operator build without aclnn src error

## Overview
This PR fixes a build error that occurs when building single operators without ACLNN source code. The changes ensure the build system correctly handles cases where only specific operators are compiled without the full ACLNN library source.

## Technical Significance
Single operator builds are important for development, testing, and custom deployments where only a subset of operators is needed. This fix improves the build system's flexibility and robustness, allowing developers to build and test individual operators without requiring the entire ACLNN source tree. Proper build system configuration is essential for efficient development workflows and custom operator integration.

## Related
- `technique-build-optimization`
- `technique-cmake-configuration`
- `technique-modular-build`
- `technique-infrastructure`