---
id: technique-pr-vllm-ascend-7367
title: "PR Insight: vllm-project/vllm-ascend #7367"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - fia
  - installation
  - file-handling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7367"
---

# PR Insight: vllm-project/vllm-ascend #7367

**Title:** [bugfix] fix unzip file path for fia operator

## Overview
This PR fixes incorrect decompression path for the FIA (Flash Infer Attention) operator package, which was creating unnecessary folders during modification. The fix ensures proper file path handling in the installation scripts for FIA operators on A2 and A3.

## Technical Significance
This fix matters for FIA operator installation reliability on Ascend. Incorrect decompression paths could cause operator registration failures or runtime errors when using flash attention. The fix ensures operators are extracted to the correct locations, enabling reliable deployment of high-performance attention kernels.

## Related
- technique-flash-infer-attention