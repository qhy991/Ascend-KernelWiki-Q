---
id: technique-pr-mindspeed-1807
title: "PR Insight: Ascend/MindSpeed #1807"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - compatibility
  - atb
  - build
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1807"
---

# PR Insight: Ascend/MindSpeed #1807

**Title:** 兼容不支持ag-mm-rs的ATB版本，避免编译报错

## Overview
This PR adds compatibility for ATB (Ascend Tensor Boost) versions that don't support ag-mm-rs (likely an advanced matrix multiplication reduction-strain feature). The change prevents compilation errors when using older ATB versions.

## Technical Significance
ATB version compatibility is important for working across different Ascend software stacks. Adding compatibility checks prevents build failures and enables MindSpeed to work with a wider range of ATB installations on Ascend NPUs.

## Related
- build-system patterns
- atb-integration
- matrix multiplication