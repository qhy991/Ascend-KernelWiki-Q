---
id: technique-pr-samples-1838
title: "PR Insight: Ascend/samples #1838"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - unique
  - custom-op
  - dtype-support
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1838"
---

# PR Insight: Ascend/samples #1838

**Title:** support uniquecust op int8 int16 uint16 uint8 float32 float64 dtype

## Overview
This PR extends the custom Unique operator to support multiple data types including int8, int16, uint16, uint8, float32, and float64, improving the operator's flexibility across different precision requirements.

## Technical Significance
Enables Unique operator functionality across various data types, supporting diverse use cases from quantized inference (int8) to high-precision computation (float64). This demonstrates type-generic programming patterns in AscendC.

## Related
- `technique-operator-fusion`
- `technique-format-conversion`