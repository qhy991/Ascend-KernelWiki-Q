---
id: technique-pr-mindspeed-1195
title: "PR Insight: Ascend/MindSpeed #1195"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - flash-attention
  - bugfix
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1195"
---

# PR Insight: Ascend/MindSpeed #1195

**Title:** fix: FA_v2 开关生效需要同时打开FA开关问题

## Overview
This PR fixes an issue where the Flash Attention v2 (FA_v2) feature flag required the general Flash Attention (FA) flag to also be enabled. This simplifies the configuration by making FA_v2 independently configurable.

## Technical Significance
Flash Attention is a critical optimization for transformer models on Ascend NPUs. This fix improves usability by allowing users to enable FA_v2 directly without managing interdependent flags, making it easier to adopt this performance optimization for transformer training and inference.

## Related
- kernel-flash-attention
- kernel-attention