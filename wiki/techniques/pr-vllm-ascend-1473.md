---
id: technique-pr-vllm-ascend-1473
title: "PR Insight: vllm-project/vllm-ascend #1473"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - chunked-prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1473"
---

# PR Insight: vllm-project/vllm-ascend #1473

**Title:** [0.9.1][bugfix] fix chunked_prefill_mla input for MTP

## Overview
This PR fixes incorrect input handling in chunked-prefill MLA when used with MTP (Multi-Token Prediction).

## Technical Significance
Corrects MTP's interaction with chunked-prefill MLA, ensuring that the proposer receives properly formatted input. The fix updates model runner and MTP proposer to handle chunked prefill outputs correctly, maintaining spec decode accuracy.

## Related
- `technique-mtp`
- `technique-chunked-prefill`
- `technique-mla`