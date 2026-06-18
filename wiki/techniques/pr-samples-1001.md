---
id: technique-pr-samples-1001
title: "PR Insight: Ascend/samples #1001"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - dvpp
  - jpegd
  - optimization
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1001"
---

# PR Insight: Ascend/samples #1001

**Title:** remove align up of jpegd

## Overview
Removes alignment padding in the JPEG decoder (JPEGD) DVPP operation, likely to reduce memory overhead or improve efficiency for certain input sizes.

## Technical Significance
DVPP operations require specific memory alignment, but unnecessary alignment increases memory usage. This optimization reduces memory footprint for JPEG decoding in inference pipelines.

## Related
- `technique-dvpp-optimization` / `hw-unified-buffer`
