---
id: technique-pr-vllm-ascend-8435
title: "PR Insight: vllm-project/vllm-ascend #8435"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decoding
  - pcp
  - eagle3
  - bugfix
  - slot-mapping
  - triton
  - compute-order
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8435"
---

# PR Insight: vllm-project/vllm-ascend #8435

**Title:** [BugFix] Fix compute_slot_mapping triton for pcp+eagle3

## Overview
This PR fixes an issue where the main model used the Triton operator to compute slot mapping, but did not account for the draft model scenario. With PCP enabled, the slot mapping could not be fully computed using the Triton operator before the main model's forward pass because the Triton operator is computed on the NPU, and the latter would overwrite the former, causing incorrect results in PCP+Eagle3 scenarios.

## Technical Significance
This fix ensures correct slot mapping computation in hybrid deployment scenarios with speculative decoding and context parallelism. The issue demonstrates complex compute ordering dependencies when combining PCP, speculative decoding, and draft models. The solution properly handles the interaction between main and draft model slot mapping computation.

## Related
- `technique-speculative-decoding`
- `technique-context-parallel`
- `technique-eagle`