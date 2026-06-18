---
id: technique-pr-vllm-ascend-1872
title: "PR Insight: vllm-project/vllm-ascend #1872"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mla
  - nz-format
  - format-conversion
  - performance
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1872"
---

# PR Insight: vllm-project/vllm-ascend #1872

**Title:** [0.9.1][Perf]Remove NZ of kv_b_proj in Deepseek MLA.

## Overview
This PR removes NZ format transformation for the kv_b_proj weights in DeepSeek MLA. The weights are not quantized and fall back to ND calculation in runtime (torchair graph doesn't support float bmm with NZ), causing two redundant transData operations. Removing them saves ~40us per layer.

## Technical Significance
Format optimization for MLA. Eliminating unnecessary NZ->ND conversions for non-quantized weights reduces data movement overhead, which is significant for attention kernels that are memory-bandwidth bound.

## Related
- `kernel-mla-ascendc`
- `technique-nz-format`
- `technique-format-conversion`
- `technique-deepseek`