---
id: technique-pr-vllm-ascend-890
title: "PR Insight: vllm-project/vllm-ascend #890"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - v1-engine
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/890"
---

# PR Insight: vllm-project/vllm-ascend #890

**Title:** [1/N][UT][v1 MTP] add basic v1 mtp features

## Overview
This PR adds basic Multi-Token Propose (MTP) features for the V1 engine, currently supporting TP-only, eager mode, and k=1 configuration. This is the first in a series of PRs to expand MTP capabilities.

## Technical Significance
MTP is an advanced speculative decoding technique that generates multiple tokens per step. The initial implementation provides a foundation for future expansions, enabling basic MTP functionality on the V1 engine while more complex scenarios (DP, graph mode) are planned for subsequent updates.

## Related
- `technique-mtp`
- `technique-spec-decode`
- `kernel-inference`