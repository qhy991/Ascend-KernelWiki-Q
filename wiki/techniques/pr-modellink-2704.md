---
id: technique-pr-modellink-2704
title: "PR Insight: Ascend/ModelLink #2704"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - checkpoint
  - qkv
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2704"
---

# PR Insight: Ascend/ModelLink #2704

**Title:** fix qkv-extra in load ckpt

## Overview
This PR fixes an issue related to loading extra QKV (Query-Key-Value) parameters from checkpoints. The fix ensures that additional QKV parameters are correctly handled during checkpoint loading.

## Technical Significance
QKV projections are core components of transformer attention mechanisms. Fixing the loading of extra QKV parameters ensures that models with varying attention configurations can be correctly restored from checkpoints on Ascend NPUs.

## Related
- kernel-attention
- technique-format-conversion