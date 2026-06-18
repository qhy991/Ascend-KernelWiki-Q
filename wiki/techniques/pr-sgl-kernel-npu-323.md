---
id: technique-pr-sgl-kernel-npu-323
title: "PR Insight: sgl-project/sgl-kernel-npu #323"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - topk
  - internode
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/323"
---

# PR Insight: sgl-project/sgl-kernel-npu #323

**Title:** remove the limit that A2 internode only support topk 8

## Overview
This PR removes a restrictive limit that forced A2 internode MoE operations to only support topk=8. The modification updates the dispatch and combine tiling validation logic to support topk values in the range [2, 10], enabling more flexible expert selection configurations for internode MoE inference on Ascend A2 hardware.

## Technical Significance
This expansion of topk support allows models to utilize broader expert selection configurations on A2 hardware, particularly useful for scenarios requiring different numbers of experts per token. The change removes artificial constraints that were limiting model architecture flexibility on internode MoE deployments.

## Related
- `kernel-moe-dispatch`, `kernel-moe-combine`, `technique-internode-optimization`