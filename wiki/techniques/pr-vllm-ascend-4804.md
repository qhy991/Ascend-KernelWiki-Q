---
id: technique-pr-vllm-ascend-4804
title: "PR Insight: vllm-project/vllm-ascend #4804"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - aclgraph
  - ut
  - testing
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4804"
---

# PR Insight: vllm-project/vllm-ascend #4804

**Title:** [UT]add pcp aclgraph ut

## Overview
This PR adds unit tests for PCP (prefill chunk parallelism) ACL graph functionality to tests/ut/compilation/test_acl_graph.py.

## Technical Significance
Adds test coverage for ACL graph compilation in PCP scenarios, improving code quality and preventing regressions in prefilled chunk parallelism operator graph generation.

## Related
- `technique-pcp`
- `technique-aclgraph`
- `technique-chunked-prefill`