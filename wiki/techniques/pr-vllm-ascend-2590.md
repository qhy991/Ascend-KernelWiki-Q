---
id: technique-pr-vllm-ascend-2590
title: "PR Insight: vllm-project/vllm-ascend #2590"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - bugfix
  - cudagraph-mode
  - platform
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2590"
---

# PR Insight: vllm-project/vllm-ascend #2590

**Title:** [Bugfix] Fix aclgraph not enabled by default

## Overview
This PR fixes ACL Graph not being enabled by default. The issue was caused by vLLM setting `cudagraph_mode` to `NONE` before `check_and_update_config`, which prevented ACL Graph from being properly enabled. The fix removes the problematic check and updates platform configuration logic.

## Technical Significance
The bug fix ensures ACL Graph is properly enabled by default when configured. By removing the incorrect cudagraph_mode check in `acl_graph.py` and updating platform.py logic, the PR resolves the default enablement issue. This is part of a larger effort to improve ACL Graph integration, with e2e tests to be added after CI refactoring completes.

## Related
- `technique-aclgraph`
- `technique-platform-configuration`