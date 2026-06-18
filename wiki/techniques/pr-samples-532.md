---
id: technique-pr-samples-532
title: "PR Insight: Ascend/samples #532"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - custom-op
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/532"
---

# PR Insight: Ascend/samples #532

**Title:** add sample sd3403 op info cfg

## Overview
This PR adds operator information configuration files for the SD3403 platform, providing the metadata and hardware-specific settings required for custom operator registration and execution on this Ascend variant.

## Technical Significance
Enables custom operator development for the SD3403 platform by providing the necessary configuration templates, ensuring proper operator registration and hardware feature mapping across different Ascend generations.

## Related
- `technique-operator-fusion`