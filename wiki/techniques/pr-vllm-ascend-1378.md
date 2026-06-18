---
id: technique-pr-vllm-ascend-1378
title: "PR Insight: vllm-project/vllm-ascend #1378"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - chunked-prefill
  - torchair
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1378"
---

# PR Insight: vllm-project/vllm-ascend #1378

**Title:** [BugFix] Fix a bug of running chunked-prefill with torchair

## Overview
This PR fixes a bug when running chunked-prefill with TorchAir, ensuring correct behavior in MLA V1 attention computation.

## Technical Significance
Resolves incorrect attention computation when TorchAir graph mode is combined with chunked-prefill. The fix ensures that chunked prefill operations correctly pass context to the attention operator, which is critical for maintaining accuracy in TorchAir-accelerated inference pipelines.

## Related
- `technique-chunked-prefill`
- `technique-torchair`
- `kernel-attention`