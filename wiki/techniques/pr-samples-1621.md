---
id: technique-pr-samples-1621
title: "PR Insight: Ascend/samples #1621"
type: wiki-technique
architectures:
  - ascend910
  - ascend310p
  - ascend310p
tags:
  - samples
  - tbe
  - custom-operator
  - 310b
  - python3.9
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1621"
---

# PR Insight: Ascend/samples #1621

**Title:** TBE自定义算子的配置文件适配310B；兼容Python3.9

## Overview
This PR adapts TBE (Tensor Boost Engine) custom operator configuration files for the Ascend 310B platform and ensures compatibility with Python 3.9.

## Technical Significance
TBE is the DSL for writing custom Ascend operators. Adapting configuration for 310B involves adjusting for the edge device's hardware constraints and capabilities. Python 3.9 compatibility ensures samples work with modern Python versions, which is important as Python 3.7 reaches end-of-life.

## Related
- technique-tbe
- wiki-hardware-ascend310p