---
id: technique-pr-vllm-ascend-6320
title: "PR Insight: vllm-project/vllm-ascend #6320"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - e2e-test
  - npugraph-ex
  - static-kernel
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6320"
---

# PR Insight: vllm-project/vllm-ascend #6320

**Title:** [e2e Test][npugraph_ex]add static kernel e2e test case

## Overview
This PR adds an end-to-end test case for the npugraph_ex static kernel scenario, monitoring the compilation and unloading process. The test was added in `tests/e2e/singlecard/test_aclgraph_accuracy.py` with minor fixes to `vllm_ascend/compilation/compiler_interface.py`.

## Technical Significance
The test ensures proper lifecycle management of static kernels in npugraph_ex mode, validating that kernels compile correctly and unload when no longer needed. This improves confidence in the static kernel optimization path.

## Related
- `technique-static-kernel`
- `technique-npugraph`
- `technique-e2e-testing`