---
id: technique-pr-samples-2094
title: "PR Insight: Ascend/samples #2094"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - macro-replacement
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2094"
---

# PR Insight: Ascend/samples #2094

**Title:** 将__CCE_KT_TEST__函数宏替换为ASCENDC_CPU_DEBUG

## Overview
This PR replaces the `__CCE_KT_TEST__` function macro with `ASCENDC_CPU_DEBUG`, updating the debugging and testing interface to match the latest AscendC conventions.

## Technical Significance
Modernizes the testing infrastructure by adopting current debug macros, ensuring compatibility with latest toolchains and simplifying CPU-based debugging workflows for kernel development.

## Related
- `technique-operator-fusion`