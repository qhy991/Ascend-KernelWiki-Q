---
id: technique-pr-vllm-ascend-3849
title: "PR Insight: vllm-project/vllm-ascend #3849"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - p-d
  - mooncake
  - layerwise-connector
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3849"
---

# PR Insight: vllm-project/vllm-ascend #3849

**Title:** [P/D] fix mooncake layerwise connector

## Overview
This PR fixes a typo in the Mooncake layerwise connector where `request` (singular) should be `requests` (plural) in `connector_metadata`. The 2-line addition and 1-line deletion to `vllm_ascend/distributed/mooncake_layerwise_connector.py` corrects this naming inconsistency.

## Technical Significance
Correct field names are critical for data structures in distributed systems. This typo fix prevents failures in disaggregated inference when accessing request metadata, ensuring Mooncake's layerwise connector functions correctly in production P/D deployments.

## Related
- `technique-disaggregated-inference`
- `technique-mooncake`
- `technique-layerwise-connector`