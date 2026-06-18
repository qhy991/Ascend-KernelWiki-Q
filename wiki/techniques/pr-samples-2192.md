---
id: technique-pr-samples-2192
title: "PR Insight: Ascend/samples #2192"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - custom-op
  - torchair
  - graph-mode
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2192"
---

# PR Insight: Ascend/samples #2192

**Title:** 新增自定算子入torchair图模式样例

## Overview
This PR adds a sample demonstrating how to integrate custom operators into TorchAir graph mode. TorchAir is the PyTorch frontend for Ascend, and graph mode provides optimization opportunities.

## Technical Significance
Shows the integration pattern for custom Ascend operators in PyTorch workflows using TorchAir's graph mode. This is essential for extending PyTorch with Ascend-optimized operators while leveraging graph optimizations.

## Related
- `technique-operator-fusion`
- `wiki-language-ascendc`