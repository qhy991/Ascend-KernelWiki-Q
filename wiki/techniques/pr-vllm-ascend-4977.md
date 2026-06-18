---
id: technique-pr-vllm-ascend-4977
title: "PR Insight: vllm-project/vllm-ascend #4977"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - w4a8-dynamic
  - gather-ep
  - alltoall
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4977"
---

# PR Insight: vllm-project/vllm-ascend #4977

**Title:** [Bugfix][MoE] Remove All2All in w4a8_dynamic

## Overview
This PR removes alltoall in w4a8_dynamic scenarios since GatherEP has been fixed in PR #3279. The change is made to ascend_forward_context.py.

## Technical Significance
Optimizes W4A8 dynamic quantized MoE by using the fixed GatherEP instead of alltoall, reducing communication overhead.

## Related
- `kernel-moe`
- `kernel-gather-ep`
- `kernel-alltoall`
- `technique-w4a8-quantization`
- `technique-moe-communication`