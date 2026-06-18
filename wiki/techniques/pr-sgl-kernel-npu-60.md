---
id: technique-pr-sgl-kernel-npu-60
title: "PR Insight: sgl-project/sgl-kernel-npu #60"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cache-update
  - cache-location
  - token-pool
  - ascendc
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/60"
---

# PR Insight: sgl-project/sgl-kernel-npu #60

**Title:** support cache loc update op

## Overview
This PR adds a cache location update operator that retrieves cache locations from token pools, complementing the cache assign operator. Uses same input format as cache assign but performs retrieval instead of assignment. Updates kernel implementation and adds test coverage.

## Technical Significance
Enables read-only cache location queries for inference scenarios where cache locations need to be retrieved without modification. The update operator complements the assign operator to provide full cache location management capabilities, critical for efficient KV cache access patterns.

## Related
- technique-cache-optimization
- technique-token-pool-management
- technique-kv-cache