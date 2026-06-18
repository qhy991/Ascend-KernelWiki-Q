---
id: technique-pr-vllm-ascend-6099
title: "PR Insight: vllm-project/vllm-ascend #6099"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - memory-optimization
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6099"
---

# PR Insight: vllm-project/vllm-ascend #6099

**Title:** [EPLB][Bugfix][v0.13.0] Incorporate the warm up of the EPLB into the profile run.

## Overview
This is a cherry-pick of PR #6020 for the v0.13.0 release branch. It reduces unnecessary video memory usage in EPLB by incorporating warm-up into the profile run and reusing the same gather buffer.

## Technical Significance
This fix ensures the v0.13.0 branch benefits from the EPLB memory optimization. The cherry-pick applies the same changes: integrating EPLB warm-up into the profile run and reusing gather buffers to reduce memory footprint. This prevents OOM errors in large-scale deployments on the release branch.

## Related
- `technique-pr-vllm-ascend-6020`, `technique-eplb`, `technique-memory-optimization`