---
id: technique-pr-cann-ops-adv-315
title: "PR Insight: Ascend/cann-ops-adv #315"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - flash-attention
  - ascendc
  - api-compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/315"
---

# PR Insight: Ascend/cann-ops-adv #315

**Title:** fix add CCE for high-level apis softmaxflshV2 softmax

## Overview
This PR fixes and adds CCE (Compute Cube Engine) support for high-level APIs related to softmax flash attention V2 and softmax operators. The changes ensure proper integration between high-level API interfaces and low-level CCE implementations.

## Technical Significance
CCE integration is crucial for leveraging Ascend's hardware acceleration capabilities. This fix ensures that softmax and flash attention V2 operators properly utilize the Cube unit for efficient computation. High-level API fixes improve developer experience by providing stable interfaces while maintaining hardware-specific optimizations. The V2 flash attention operator likely includes improvements for memory layout, head-dimension handling, or mask processing efficiency.

## Related
- `technique-flash-attention`
- `technique-softmax-ascendc`
- `technique-cube-unit`
- `technique-high-level-api`