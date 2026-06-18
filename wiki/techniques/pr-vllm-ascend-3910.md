---
id: technique-pr-vllm-ascend-3910
title: "PR Insight: vllm-project/vllm-ascend #3910"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/3910"
---

# PR Insight: vllm-project/vllm-ascend #3910

**Title:** Main mfix bug when max_seqs=14 in mtp=2 scenario and raise error when cudagraph_capture_sizes can't be an integer multiple of uniform_decode_query_lentp

## Overview
This is the main branch version of PR #3909, fixing the same three issues: reverting MTP fullgraph bugfix, raising error for invalid graph capture sizes, and fixing max_seqs=14 bug in MTP=2 scenario. The changes ensure MTP operates correctly across different sequence count configurations and validates graph capture parameters.

## Technical Significance
Consistent fixes across branches ensure MTP stability across vLLM versions. The edge case with specific sequence counts (max_seqs=14, MTP=2) reveals complex interactions between MTP data paths and sequence management. The graph capture size validation prevents misconfiguration that could cause incorrect graph replay or performance issues.

## Related
- `technique-mtp`, `technique-aclgraph`, `technique-graph-capture`, `technique-validation`