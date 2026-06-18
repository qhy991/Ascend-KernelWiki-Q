---
id: technique-pr-cann-ops-adv-339
title: "PR Insight: Ascend/cann-ops-adv #339"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build
  - cmake
  - shell-scripting
  - infrastructure
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/339"
---

# PR Insight: Ascend/cann-ops-adv #339

**Title:** bugfix: multi op-name pass error from cmake to shell script

## Overview
This PR fixes a bug where multiple operator names were not correctly passed from CMake configuration to shell scripts. The changes ensure proper handling of operator name lists during the build process.

## Technical Significance
Proper operator name handling is essential for building multiple operators efficiently and correctly. This bug fix ensures that shell scripts receive the correct operator names from CMake, preventing build failures or incorrect operator compilation. Multi-operator builds are common for custom deployments and testing, so robust name passing is crucial for the build system's reliability.

## Related
- `technique-build-optimization`
- `technique-cmake-configuration`
- `technique-shell-scripting`
- `technique-infrastructure`