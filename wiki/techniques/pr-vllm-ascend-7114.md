---
id: technique-pr-vllm-ascend-7114
title: "PR Insight: vllm-project/vllm-ascend #7114"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gmm
  - compilation
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7114"
---

# PR Insight: vllm-project/vllm-ascend #7114

**Title:** [BugFix] Fix compilation errors for operators dispatch_gmm_combine_decode/moe_combine_normal/moe_dispatch_normal

## Overview
Fixes compilation errors encountered when building versions later than b020 for MoE operators: `dispatch_gmm_combine_decode`, `moe_combine_normal`, and `moe_dispatch_normal`. The root cause was updates to `moe_distribute_base.h` that changed definitions, causing compilation failures. The solution adds a dedicated copy of `moe_distribute_base.h` into each operator's implementation.

## Technical Significance
Ensures stable compilation independent of framework version updates by providing dedicated copies of dependent header files. This prevents compilation breakage from upstream changes while maintaining operator functionality.

## Related
- `technique-gmm`, `technique-moe`, `technique-compilation`, `technique-version-compatibility`