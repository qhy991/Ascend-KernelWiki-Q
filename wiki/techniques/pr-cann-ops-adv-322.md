---
id: technique-pr-cann-ops-adv-322
title: "PR Insight: Ascend/cann-ops-adv #322"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - cmake
  - build
  - infrastructure
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/322"
---

# PR Insight: Ascend/cann-ops-adv #322

**Title:** moe_compute_expert_token算子CMakeList修改

## Overview
This PR modifies the CMakeLists.txt configuration for the moe_compute_expert_token operator. The changes update the build configuration to improve compilation, linking, or integration of this MoE operator into the CANN ops library.

## Technical Significance
The moe_compute_expert_token operator computes expert-specific outputs for assigned tokens in MoE models. Proper CMake configuration ensures the operator is correctly compiled, linked, and made available to high-level APIs. This modification may improve build parallelism, fix dependency issues, or enable better integration with other MoE operators. Clean build configuration is essential for maintaining a scalable and maintainable operator library.

## Related
- `technique-moe-ascendc`
- `technique-cmake-configuration`
- `technique-build-optimization`
- `technique-operator-integration`