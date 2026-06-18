---
id: technique-pr-cann-ops-adv-84
title: "PR Insight: cann-ops-adv #84"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - flash-attention
  - attention
  - data-reuse
  - l1-buffer
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/84"
---

# PR Insight: cann-ops-adv #84 - PFA L1 reuse

## Overview
This PR implements L1 buffer data reuse optimizations for PFA (PromptFlashAttention), reducing global memory accesses by keeping frequently accessed data in the L1 cache.

## Technical Significance
L1 buffer reuse reduces memory bandwidth pressure, which is often the bottleneck for attention operators. By maximizing data reuse in the L1 cache, this optimization improves PFA performance during prompt processing, enabling faster LLM inference on Ascend NPUs.

## Related
- `kernel-flash-attention`
- `technique-data-reuse`
- `hw-l1-buffer`
- `hw-unified-buffer`