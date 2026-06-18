---
id: technique-pr-samples-2096
title: "PR Insight: Ascend/samples #2096"
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
  - "https://gitee.com/ascend/samples/pulls/2096"
---

# PR Insight: Ascend/samples #2096

**Title:** 将cplusplus目录的__CCE_KT_TEST__函数宏复原，并将operator目录下的替换掉

## Overview
This PR reverts the `__CCE_KT_TEST__` macro changes in the cplusplus directory while applying the macro replacement to the operator directory, maintaining different debug interfaces for different components.

## Technical Significance
Shows the proper separation of concerns between different components, where cplusplus samples may need different debug interfaces compared to operator samples. This ensures compatibility across various parts of the codebase.

## Related
- `technique-operator-fusion`