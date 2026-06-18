---
id: technique-pr-vllm-ascend-6822
title: "PR Insight: vllm-project/vllm-ascend #6822"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - gdn-attention
  - accuracy
  - graph-mode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6822"
---

# PR Insight: vllm-project/vllm-ascend #6822

**Title:** [main][bugfix] Fixed an accuracy problem of gdn layer in graph

## Overview
This PR fixes accuracy issues in GDN (Gated Delta Net) attention when running in graph mode with padded query_start_loc. The fix introduces an unpadded version (gdn_query_start_loc) specifically for GDN attention operations.

## Technical Significance
Resolves non-deterministic output issues in graph mode with GDN attention by separating padded and unpadded query_start_loc. The padding required for FIA/TND constraints causes accuracy problems in GDN attention, necessitating separate unpadded inputs.

## Related
- `kernel-attention`