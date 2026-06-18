---
id: technique-pr-vllm-ascend-5786
title: "PR Insight: vllm-project/vllm-ascend #5786"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - pd-disaggregation
  - mtp
  - full-graph
  - eagle3
  - moe-dispatch
  - async-scheduling
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5786"
---

# PR Insight: vllm-project/vllm-ascend #5786

**Title:** [v0.13.0][Bugfix] Support ALL D-Nodes in fullgraph when running MTP in PD

## Overview
This PR fixes a bug where prefill-decode disaggregation with MTP (Multi-Token Prediction) and full graph mode combined with asynchronous scheduling caused decode nodes to not properly enqueue into the full graph. The problem occurred because KV cache from prefill nodes didn't include spec tokens, causing the `total_num_scheduled_tokens` calculation to be incorrect. This led to mixed full graph and eagle mode instances in decode, causing MoeDispatch synchronization waits to slow down full graph instances.

## Technical Significance
This bugfix ensures uniform decode behavior in PD+MTP+FullGraph+async scheduling scenarios by padding spec tokens for requests with KV cache from prefill nodes. The padded spec tokens are then rejected during sampling, which satisfies the `uniform_decode` condition for full graph enqueueing. The fix prevents the performance degradation caused by mixing full graph and eagle mode instances, which was introducing synchronization waits through MoeDispatch. By ensuring all decode instances are in the full graph, the optimization maintains high throughput and prevents synchronization bottlenecks.

## Related
- `technique-pd-disaggregation`, `technique-mtp`, `technique-full-graph`, `technique-eagle3`, `technique-async-scheduling`, `technique-moe-dispatch`