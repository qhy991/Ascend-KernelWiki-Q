---
id: technique-pr-vllm-ascend-7344
title: "PR Insight: vllm-project/vllm-ascend #7344"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - memory-optimization
  - distributed
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7344"
---

# PR Insight: vllm-project/vllm-ascend #7344

**Title:** [EPLB] Reduce the memory used for batch_isend_irecv

## Overview
This PR reduces memory usage in the EPLB (Expert Load Balancer) communication path by addressing buffer allocation that was moved from dist.all_gather_into_tensor to dist.batch_isend_irecv. The fix genuinely reduces overall NPU memory usage in this communication pattern.

## Technical Significance
This optimization matters for Ascend EPLB memory efficiency. A previous optimization (#6729) appeared to reduce memory but actually shifted buffer allocation without reducing overall usage. This fix properly reduces memory by optimizing the batch_isend_irecv buffer handling, estimated savings of ~0.35GB for a 48-layer model, enabling larger batch sizes or models on the same hardware.

## Related
- technique-eplb
- technique-hccl-optimization
- technique-memory-optimization