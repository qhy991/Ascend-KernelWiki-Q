---
id: technique-pr-samples-2734
title: "PR Insight: Ascend/samples #2734"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tiling
  - operator-fusion
  - ascendc
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2734"
---

# PR Insight: Ascend/samples #2734

**Title:** 解除tiling下沉样例，算子包不支持通过--install-path安装的限制

## Overview
This PR removes a restriction in the tiling sink sample where the operator package did not support installation via the --install-path flag. This change likely makes the sample more flexible and easier to use in different deployment scenarios.

## Technical Significance
Removing installation restrictions improves the usability of samples and makes it easier for developers to test and integrate tiling sink techniques into their workflows. Tiling sink is an important optimization for reducing memory overhead and improving performance.

## Related
- technique-nz-tiling
- technique-operator-fusion
- pr-samples-2721