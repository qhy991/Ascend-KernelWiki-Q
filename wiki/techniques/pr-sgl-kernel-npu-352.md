---
id: technique-pr-sgl-kernel-npu-352
title: "PR Insight: sgl-project/sgl-kernel-npu #352"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - long-sequences
  - notify-dispatch
  - loop-unrolling
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/352"
---

# PR Insight: sgl-project/sgl-kernel-npu #352

**Title:** Modify notifydispatch to support DEEPEP_NORMAL_LONG_SEQ_ROUND up to 128.

## Overview
This PR modifies the notify_dispatch kernel to support up to 128 rounds of long sequence processing in DeepEP normal mode. The implementation updates the kernel loop structure to handle larger round counts, verified with DEEPEP_NORMAL_LONG_SEQ_ROUND=128 and DEEPEP_NORMAL_LONG_SEQ_PER_ROUND_TOKENS=512 configurations.

## Technical Significance
Supporting up to 128 rounds enables DeepEP to handle very long sequences in multi-round processing mode, which is essential for models with extensive context requirements. This extension allows more granular token distribution across rounds while maintaining efficient memory usage and communication patterns.

## Related
- `kernel-notify-dispatch`, `kernel-deepep-normal`, `technique-long-sequence-optimization`