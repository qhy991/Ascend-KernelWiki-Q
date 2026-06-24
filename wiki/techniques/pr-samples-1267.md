---
id: technique-pr-samples-1267
title: "PR Insight: Ascend/samples #1267"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - platform-migration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1267"
---

# PR Insight: Ascend/samples #1267

**Title:** 算子目录下710->310P

## Overview
This PR updates operator-specific sample directories to replace references from Ascend710 to Ascend310P platform, continuing the platform migration effort.

## Technical Significance
Platform-specific operator samples require careful updates because Ascend310P may have different operator support, memory hierarchies, and performance characteristics compared to Ascend710. This migration ensures that operator development examples remain relevant for developers targeting Ascend310P hardware.

## Related
- wiki-hardware-unified-buffer
- wiki-hardware-l1-buffer
- technique-tiling