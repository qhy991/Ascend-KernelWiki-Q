---
id: technique-pr-vllm-ascend-6430
title: "PR Insight: vllm-project/vllm-ascend #6430"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - operator-fusion
  - allreduce
  - layernorm
  - npugraph
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6430"
---

# PR Insight: vllm-project/vllm-ascend #6430

**Title:** [bugfix][npugraph_ex]add the extra check for allreduce rmsnorm fusion pass

## Overview
This PR adds a missing check condition to the allreduce RMSNorm fusion pass in the npugraph_ex compilation pipeline. The fusion should only occur when the start of compile_range is greater than 512, which was previously overlooked.

## Technical Significance
Fixes a bug in operator fusion logic for npugraph where the allreduce-rmsnorm fusion was being applied incorrectly. The fix ensures that fusion is only performed when the compilation range meets the required size threshold, preventing incorrect fusion that could cause performance or correctness issues.

## Related
- `technique-operator-fusion`
- `pattern-allreduce-fusion`