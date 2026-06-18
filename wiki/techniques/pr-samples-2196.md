---
id: technique-pr-samples-2196
title: "PR Insight: Ascend/samples #2196"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - namespace
  - coding-style
  - ascendc
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2196"
---

# PR Insight: Ascend/samples #2196

**Title:** 删除hello_world样例中的显式using namespace AscendC

## Overview
This PR removes the explicit `using namespace AscendC;` declaration from the hello_world sample, likely to avoid namespace pollution and demonstrate explicit qualification patterns.

## Technical Significance
Demonstrates best practices for namespace usage in AscendC development, showing that explicit qualification (`AscendC::Type`) is preferred over `using namespace` to avoid naming conflicts and improve code clarity.

## Related
- `technique-operator-fusion`