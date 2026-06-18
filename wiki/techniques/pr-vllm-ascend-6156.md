---
id: technique-pr-vllm-ascend-6156
title: "PR Insight: vllm-project/vllm-ascend #6156"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - memory-alignment
  - hbm
  - synchronization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6156"
---

# PR Insight: vllm-project/vllm-ascend #6156

**Title:** [BugFix]bug fix for dispatch_ffn_combine

## Overview
This PR fixes a synchronization bug in dispatch_ffn_combine operator for MoE routing. The issue occurs when expertPerRank doesn't result in 512B-aligned data length. The fix pads synchronization data to 512B alignment to match Ascend A3's HBM atomic write behavior.

## Technical Significance
dispatch_ffn_combine uses synchronization signals embedded in int32 data (EP * expertPerRank values). Ascend A3 writes 512B DataBlocks atomically to HBM. For DeepSeek with expertPerRank=16, this alignment works naturally, but other configurations require explicit padding. The fix ensures correct synchronization checking by padding to 512B boundaries regardless of expertPerRank value.

## Related
- `technique-moe`, `technique-memory-alignment`, `technique-hbm`, `technique-synchronization`