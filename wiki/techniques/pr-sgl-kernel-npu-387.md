---
id: technique-pr-sgl-kernel-npu-387
title: "PR Insight: sgl-project/sgl-kernel-npu #387"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl
  - interface-update
  - compile-warnings
  - moe
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/387"
---

# PR Insight: sgl-project/sgl-kernel-npu #387

**Title:** Change hccl Init and SetCcTiling interface to V2 version to avoid compile warnings

## Overview
This PR updates HCCL interface calls from Init to InitV2 and SetCcTiling to SetCcTilingV2 across DeepEP operators to eliminate compilation warnings. The changes apply to combine, dispatch, and notify kernels in both A2 and general implementations, maintaining functional compatibility with newer HCCL API versions.

## Technical Significance
Updating to V2 HCCL interfaces ensures compatibility with current CANN versions and removes deprecated API warnings that could indicate future breaking changes. The interface update maintains backward compatibility while preparing for future HCCL API evolution.

## Related
- `technique-hccl-optimization`, `kernel-deepep-combine`, `kernel-deepep-dispatch`