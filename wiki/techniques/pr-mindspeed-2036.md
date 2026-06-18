---
id: technique-pr-mindspeed-2036
title: "PR Insight: Ascend/MindSpeed #2036"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - megatron
  - compatibility
  - refactor
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2036"
---

# PR Insight: Ascend/MindSpeed #2036

**Title:** Megatron-LM-core0.10.0适配

## Overview
This PR adapts MindSpeed to work with Megatron-LM core0.10.0 release. The change updates integration points to support the new Megatron-LM version on Ascend NPUs.

## Technical Significance
Megatron-LM core0.10.0 brings important updates and optimizations for large-scale training. Adapting to this version ensures MindSpeed can leverage the latest features and performance improvements from upstream Megatron-LM. The adaptation likely includes updates to parallel training strategies, attention implementations, and memory optimizations. Keeping up with Megatron-LM updates is critical for maintaining compatibility with state-of-the-art training techniques and models on Ascend hardware.

## Related
- `technique-hccl-optimization`
- `technique-attention`