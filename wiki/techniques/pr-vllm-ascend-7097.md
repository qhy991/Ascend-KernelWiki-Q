---
id: technique-pr-vllm-ascend-7097
title: "PR Insight: vllm-project/vllm-ascend #7097"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - gmm
  - eplb
  - test-stability
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7097"
---

# PR Insight: vllm-project/vllm-ascend #7097

**Title:** [Test][BugFix] Fix dispatch_gmm_combine_decode test stability

## Overview
Fixes nightly test failures for `dispatch_gmm_combine_decode` by ensuring each test case uses a copy of global kwargs instead of a reference to prevent parameter pollution between test cases. Also adds weight initialization for EPLB + W8A8 dynamic quantization scenarios.

## Technical Significance
Improves test stability and isolation by preventing cross-test parameter contamination. The weight initialization addition ensures proper test coverage for combined EPLB and quantization scenarios.

## Related
- `technique-gmm`, `technique-moe`, `technique-eplb`, `technique-test-isolation`