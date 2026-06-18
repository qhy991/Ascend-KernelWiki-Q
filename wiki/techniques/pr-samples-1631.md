---
id: technique-pr-samples-1631
title: "PR Insight: Ascend/samples #1631"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - scatter-nd-add
  - custom-operator
  - bugfix
  - version-compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1631"
---

# PR Insight: Ascend/samples #1631

**Title:** 【修改问题单】 【DTS2023031710407】scatter_nd_add自定义算子在C84部署升级至C29后，自定义算子运行失败

## Overview
This PR fixes a bug where the scatter_nd_add custom operator failed to run after upgrading from C84 to C29, addressing issue DTS2023031710407.

## Technical Significance
Version compatibility issues can break custom operators when the Ascend software stack is upgraded. scatter_nd_add is a tensor manipulation operator used in sparse updates and attention mechanisms. This fix ensures custom operators remain compatible across Ascend CANN version upgrades.

## Related
- technique-custom-operator
- kernel-scatter-nd