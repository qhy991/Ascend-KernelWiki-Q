---
id: technique-pr-vllm-ascend-3731
title: "PR Insight: vllm-project/vllm-ascend #3731"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - dcp
  - pcp
  - aclgraph
  - mla
  - attention-v1
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3731"
---

# PR Insight: vllm-project/vllm-ascend #3731

**Title:** [feat]dcp pcp support aclgraph

## Overview
This PR enables DCP (Decode-Compute-Parallel) and PCP (Prefill-Compute-Parallel) support for full aclgraph execution, including MLA (Multi-Head Latent Attention) and attention_v1. The implementation adds significant logic across multiple files: 100 lines to `vllm_ascend/compilation/acl_graph.py`, 131 lines to `vllm_ascend/attention/mla_v1.py`, 74 lines to `vllm_ascend/attention/attention_v1.py`, and 64 lines to `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
Enabling full aclgraph support for DCP and PCP execution modes allows prefill and decode phases to run on different compute resources in graph mode, improving resource utilization and throughput. The support extends to MLA attention variants, ensuring the optimization benefits apply to models using KV cache compression.

## Related
- `technique-aclgraph`
- `technique-dcp`
- `technique-pcp`
- `technique-mla`