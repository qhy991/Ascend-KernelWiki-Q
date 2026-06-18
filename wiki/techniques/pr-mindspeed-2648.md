---
id: technique-pr-mindspeed-2648
title: "PR Insight: Ascend/MindSpeed #2648"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspore
  - bugfix
  - megatron
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2648"
---

# PR Insight: Ascend/MindSpeed #2648

**Title:** [mindspore][bugfix]megatron 012 bugfix

## Overview
This PR fixes bugs in the Megatron 0.12 integration when using MindSpore backend. The changes address compatibility issues between MindSpeed, Megatron-LM 0.12, and MindSpore framework, ensuring proper behavior of training operations and utilities.

## Technical Significance
Megatron-LM is a widely used large-scale training framework. Maintaining compatibility with version 0.12 is important for users who want to leverage new Megatron features while using MindSpore on Ascend hardware. This fix ensures reliable operation of the adapter layer.

## Related