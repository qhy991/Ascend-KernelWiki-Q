---
id: technique-pr-samples-1941
title: "PR Insight: Ascend/samples #1941"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - op-plugin
  - inference
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1941"
---

# PR Insight: Ascend/samples #1941

**Title:** 添加op-plugin适配方式样例

## Overview
This PR adds a sample demonstrating how to adapt and use op-plugin (operator plugin) functionality within Ascend inference frameworks. The op-plugin mechanism allows custom operators to be integrated into the Ascend computing graph, enabling developers to add domain-specific or optimized kernels alongside standard operators.

## Technical Significance
Op-plugin adaptation is a key technique for extending Ascend's inference capabilities beyond the built-in operator library. This sample provides reference code for integrating custom AscendC kernels or third-party operators into the inference pipeline, demonstrating the proper API calls and registration patterns for Ascend910/910B.

## Related
- `technique-operator-fusion`
- `pattern-custom-operator`