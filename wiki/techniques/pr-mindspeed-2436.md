---
id: technique-pr-mindspeed-2436
title: "PR Insight: Ascend/MindSpeed #2436"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - revert
  - alibi
  - fav2
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2436"
---

# PR Insight: Ascend/MindSpeed #2436

**Title:** Revert "!2418 【问题单】【master分支】alibi重构问题单fav2算子报错解决"

## Overview
This PR reverts a previous change (PR #2418) that attempted to fix ALiBi refactoring issues with the fav2 operator. The revert indicates the original fix introduced new problems.

## Technical Significance
Rolls back a problematic change to maintain stability while a proper fix is developed. This highlights the complexity of ALiBi refactoring and the need for careful testing when modifying attention mechanisms.

## Related
- `kernel-attention-ascendc`
- `technique-alibi`