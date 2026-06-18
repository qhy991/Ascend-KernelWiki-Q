---
id: technique-pr-vllm-ascend-7036
title: "PR Insight: vllm-project/vllm-ascend #7036"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - metadata
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7036"
---

# PR Insight: vllm-project/vllm-ascend #7036

**Title:** [P/D][Bugfix] Layerwise stacking MTP error.

## Overview
Fixes a metadata cleanup issue in MTP layerwise stacking where the community added a cleaning mechanism after the main model finishes running. The MTP layer should not clean the metadata, so a new condition is added to avoid cleaning it.

## Technical Significance
Prevents metadata cleanup errors in MTP scenarios by adding proper conditional checks. The fix ensures that metadata needed for MTP operations is preserved while allowing cleanup for non-MTP code paths.

## Related
- `technique-mtp`, `technique-metadata-management`, `technique-layerwise-stacking`