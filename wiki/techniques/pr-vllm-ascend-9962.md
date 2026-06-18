---
id: technique-pr-vllm-ascend-9962
title: "PR Insight: vllm-project/vllm-ascend #9962"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - acl-graph
  - capture-size
  - pruning
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9962"
---

# PR Insight: vllm-project/vllm-ascend #9962

**Title:** [BugFix] Remove legacy capture-size pruning `update_aclgraph_sizes`

## Overview
This PR removes legacy capture-size pruning code from `update_aclgraph_sizes`, cleaning up obsolete functionality that was previously used for managing ACL graph capture sizes.

## Technical Significance
Removes obsolete code for ACL graph capture size pruning, reducing code maintenance burden and eliminating potential bugs from legacy functionality. Simplifies ACL graph management by removing outdated pruning mechanisms.

## Related
- `technique-acl-graph`, `pattern-cleanup`, `pattern-refactoring`