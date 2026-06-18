---
id: technique-pr-vllm-ascend-3889
title: "PR Insight: vllm-project/vllm-ascend #3889"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - testing
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3889"
---

# PR Insight: vllm-project/vllm-ascend #3889

**Title:** add new test model for aclgraph single_request v0.11.0

## Overview
This PR adds new test models for ACLGraph single request scenarios specifically targeting v0.11.0 release. Similar to PR #3888, this expands test coverage for ACLGraph functionality in single request multi-card scenarios, ensuring graph mode correctness for the v0.11.0 version.

## Technical Significance
Version-specific test coverage ensures that ACLGraph optimizations work correctly in the v0.11.0 release. Single request testing in distributed scenarios is critical for validating that graph capture doesn't introduce edge cases or correctness issues when requests span multiple Ascend devices.

## Related
- `technique-aclgraph`, `technique-distributed-inference`, `technique-version-compatibility`