---
id: technique-pr-vllm-ascend-5458
title: "PR Insight: vllm-project/vllm-ascend #5458"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build
  - cann
  - aclnn
  - cmake
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5458"
---

# PR Insight: vllm-project/vllm-ascend #5458

**Title:** [Kernel]update csrc cmakelist for open-source cann

## Overview
This PR updates the CMakeLists.txt in the csrc directory to include additional header file paths for open-source CANN compatibility. Specifically, it adds the base/dlog_pub.h header path for aclnn to resolve installation errors caused by CANN directory structure changes.

## Technical Significance
The build system update ensures vllm-ascend can compile successfully with open-source CANN distributions, which may have different directory structures compared to proprietary releases. This improves portability and compatibility across different CANN versions and installation methods.

## Related
- `technique-build-optimization` (Build system compatibility)
- `technique-cann-integration` (CANN framework integration)