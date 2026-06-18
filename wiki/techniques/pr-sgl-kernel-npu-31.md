---
id: technique-pr-sgl-kernel-npu-31
title: "PR Insight: sgl-project/sgl-kernel-npu #31"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cache-assign
  - ascendc
  - mtp
  - cache-optimization
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/31"
---

# PR Insight: sgl-project/sgl-kernel-npu #31

**Title:** Add cache_assign op and packaing functionality for sgl_kernel_npu

## Overview
This PR adds a cache_location_assign AscendC operation to reduce assign_req_to_token_pool_native time cost from >=5ms to <=0.5ms for MTP scenarios. Updates build.sh, CMakeLists.txt, and adds comprehensive packaging functionality for the sgl_kernel_npu library.

## Technical Significance
Achieves 10x performance improvement for cache location assignment operations critical to MTP (multi-token prediction) scenarios. The packaging functionality enables proper distribution of the AscendC operator library for integration with SGLang inference framework.

## Related
- technique-cache-optimization
- technique-operator-fusion
- technique-packaging