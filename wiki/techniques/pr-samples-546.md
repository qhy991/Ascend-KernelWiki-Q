---
id: technique-pr-samples-546
title: "PR Insight: Ascend/samples #546"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - conv2d
  - matmul
  - custom-op
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/546"
---

# PR Insight: Ascend/samples #546

**Title:** add conv2d and matmul op_info_cfg

## Overview
This PR adds operator information configuration files for conv2d and matmul operators, defining metadata such as input/output specifications, supported data types, and hardware-specific constraints.

## Technical Significance
Standardizes operator registration patterns by providing proper configuration templates, ensuring that custom operators integrate correctly with the CANN operator registry and can be discovered by framework frontends.

## Related
- `kernel-matmul-ascendc`
- `technique-operator-fusion`