---
id: technique-pr-samples-2550
title: "PR Insight: Ascend/samples #2550"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dumptensor
  - mmad
  - add
  - tensor-dump
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2550"
---

# PR Insight: Ascend/samples #2550

**Title:** 修改DumpTensor样例，改为在Mmad样例和Add样例的基础上添加DumpTensor

## Overview
This PR modifies the DumpTensor sample to be built on top of existing Mmad and Add samples. The change refactors the sample to demonstrate DumpTensor functionality within the context of actual operator implementations.

## Technical Significance
DumpTensor is an essential debugging tool for inspecting tensor values during kernel execution. Building on existing operator samples provides realistic context for how to use tensor dumping in actual applications.

## Related
- `kernel-matmul-ascendc`
- `kernel-elementwise-ascendc`
- `hw-unified-buffer`