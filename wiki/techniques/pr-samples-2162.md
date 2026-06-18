---
id: technique-pr-samples-2162
title: "PR Insight: Ascend/samples #2162"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - venc
  - data-processing
  - bugfix
  - memory-leak
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2162"
---

# PR Insight: Ascend/samples #2162

**Title:** cplusplus/level2_simple_inference/0_data_process/venc样例内存重复释放修复

## Overview
This PR fixes a double-free memory issue in the VENC (Video Encoder) sample within the data processing section of the simple inference examples.

## Technical Significance
Memory management bugs like double-frees can cause crashes and undefined behavior. The VENC sample demonstrates video encoding using Ascend's hardware acceleration, and proper memory handling is critical for stability.

## Related
- `wiki-hardware-unified-buffer`