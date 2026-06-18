---
id: technique-pr-vllm-ascend-1694
title: "PR Insight: vllm-project/vllm-ascend #1694"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mtp
  - disaggregated-prefill
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1694"
---

# PR Insight: vllm-project/vllm-ascend #1694

**Title:** [BUGFIX] [v0.9.1] Fix mtp with disaggregated-prefill

## Overview
This PR fixes MTP (Multi-Token Prediction) compatibility with disaggregated prefill deployment.

## Technical Significance
Enables MTP to work correctly in disaggregated prefill scenarios where prefill and decode run on separate devices. The fix updates MLA attention, model runner, and MTP proposer to handle cross-device state synchronization correctly.

## Related
- `technique-mtp`
- `technique-disaggregated-prefill`
- `technique-mla`