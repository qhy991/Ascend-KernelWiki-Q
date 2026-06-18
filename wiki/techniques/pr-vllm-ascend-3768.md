---
id: technique-pr-vllm-ascend-3768
title: "PR Insight: vllm-project/vllm-ascend #3768"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - p-d
  - kv-producer
  - allreduce
  - prefill
  - disaggregated
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3768"
---

# PR Insight: vllm-project/vllm-ascend #3768

**Title:** [P/D] force with_prefill true after allreduce in kv producer

## Overview
This PR forces `with_prefill` to be true after allreduce operations in the KV producer for disaggregated (P/D) inference. The fix modifies `vllm_ascend/distributed/mooncake_layerwise_connector.py` and `vllm_ascend/worker/model_runner_v1.py`, ensuring correct state management after allreduce synchronization.

## Technical Significance
In disaggregated inference with prefill (P) and decode (D) nodes, KV producers perform allreduce for tensor parallel synchronization. Forcing `with_prefill` true after allreduce ensures the producer correctly handles prefill-phase KV data, preventing synchronization bugs or incorrect tensor shapes in downstream decode operations.

## Related
- `technique-disaggregated-inference`
- `technique-allreduce`
- `technique-prefill`