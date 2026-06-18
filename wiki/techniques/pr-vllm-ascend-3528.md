---
id: technique-pr-vllm-ascend-3528
title: "PR Insight: vllm-project/vllm-ascend #3528"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - hccl-optimization
  - aclgraph
  - speculative-decoding
  - decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3528"
---

# PR Insight: vllm-project/vllm-ascend #3528

**Title:** [FEAT] Refactor spec decode to support efficient padded speculation

## Overview
1. Refactor the file `mtp_proposer.py`, splits torchair related codes into `torchair_mtp_proposer.py`

## Technical Significance
Refactors speculative decoding to support efficient padded speculation for improved throughput.

## Related
- `technique-aclgraph`
- `technique-speculative-decoding`
