---
id: technique-pr-vllm-ascend-2003
title: "PR Insight: vllm-project/vllm-ascend #2003"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - bugfix
  - packaging
  - installation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2003"
---

# PR Insight: vllm-project/vllm-ascend #2003

**Title:** [0.9.1]fix bugs that cannot find eplb submodule

## Overview
This PR fixes a packaging bug where EPLB submodules (adaptor and core) were not being installed properly. The issue occurred because `__init__.py` files were missing from `vllm_ascend/eplb/adaptor` and `vllm_ascend/eplb/core` directories, causing module import failures after pip installation.

## Technical Significance
This fix ensures proper package installation and module discovery for EPLB functionality, preventing runtime errors in production environments. Proper package structure is essential for reliable deployment, especially for features like EPLB that are critical for MoE load balancing.

## Related
- `technique-eplb`
- `technique-packaging`