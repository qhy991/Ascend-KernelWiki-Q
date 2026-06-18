---
id: technique-pr-vllm-ascend-3801
title: "PR Insight: vllm-project/vllm-ascend #3801"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - chunkprefill
  - pcp
  - dcp
  - long-sequence
  - feature-support
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3801"
---

# PR Insight: vllm-project/vllm-ascend #3801

**Title:** [feature] chunkprefill support pcp&dcp

## Overview
This PR extends ChunkPrefill to support PCP (Prefill-Compute-Parallel) and DCP (Decode-Compute-Parallel) features for long sequences. The implementation adds significant logic across attention and worker layers: 456 lines to `vllm_ascend/attention/attention_v1.py`, 453 lines to `vllm_ascend/attention/mla_v1.py`, and 283 lines to `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
ChunkPrefill with PCP/DCP support enables efficient processing of long input sequences by parallelizing compute and communication phases. This is critical for handling long-context models where prefill phases can become bottlenecks. The support extends to MLA attention variants, ensuring the optimization applies to models using KV cache compression.

## Related
- `technique-chunkprefill`
- `technique-pcp`
- `technique-dcp`
- `technique-long-sequence`