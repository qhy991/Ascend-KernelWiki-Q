---
id: technique-pr-vllm-ascend-5410
title: "PR Insight: vllm-project/vllm-ascend #5410"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mla
  - revert
  - prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5410"
---

# PR Insight: vllm-project/vllm-ascend #5410

**Title:** Revert "MLA prefill preformance optimization (#5275)"

## Overview
This PR reverts the MLA prefill performance optimization from PR #5275 due to the upcoming 0.13.0 release. The optimization will be redone after the release to ensure stability.

## Technical Significance
Reverting changes before a release prevents introducing potential regressions. The prefill optimization will be revisited and properly tested for a future release to ensure it provides benefits without breaking existing functionality.

## Related
- technique-mla
- technique-prefill-optimization
- technique-release-stability