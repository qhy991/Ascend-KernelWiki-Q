---
id: technique-pr-vllm-ascend-3909
title: "PR Insight: vllm-project/vllm-ascend #3909"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - bugfix
  - aclgraph
  - spec-decoding
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3909"
---

# PR Insight: vllm-project/vllm-ascend #3909

**Title:** fix bug when max_seqs=14 in mtp=2 scenario and raise error when cudagraph_capture_sizes can't be an integer multiple of uniform_decode_query_len

## Overview
This PR fixes three issues: (1) Reverts a previous MTP fullgraph bugfix pending vLLM support, (2) Raises an error when `cudagraph_capture_sizes` cannot be evenly divided by `uniform_decode_query_len`, and (3) Fixes a bug when max_num_seqs=14 in MTP=2 scenario. The changes affect MTP behavior in graph capture mode and validation of graph capture size configurations.

## Technical Significance
The MTP bug with specific sequence counts reveals edge cases in MTP data path handling. The graph capture size validation prevents silent failures when capture sizes don't align with MTP query lengths, which is critical for correct graph replay. Proper validation helps users configure graph capture correctly for MTP workloads on Ascend NPUs.

## Related
- `technique-mtp`, `technique-aclgraph`, `technique-graph-capture`, `technique-validation`