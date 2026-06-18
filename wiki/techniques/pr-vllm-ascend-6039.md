---
id: technique-pr-vllm-ascend-6039
title: "PR Insight: vllm-project/vllm-ascend #6039"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - mla
  - fia
  - cann85
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6039"
---

# PR Insight: vllm-project/vllm-ascend #6039

**Title:** [0.13.0][cherry-pick][CP&SP] Remove CP Redundant Variables after FIA operator enables for CANN 8.5

## Overview
This is a cherry-pick of PR #6013 for the v0.13.0 release branch. It removes redundant operations in CP/SP after integrating the FIA operator with CANN 8.5.0, eliminating precision workaround operations that are no longer needed.

## Technical Significance
This fix ensures the v0.13.0 branch benefits from CANN 8.5.0's improved FIA operator handling. The cherry-pick removes the redundant precision workaround operations for cards with no KV cache, reducing computational overhead. All CI tests pass with CANN 8.5.0 on the release branch.

## Related
- `technique-pr-vllm-ascend-6013`, `technique-context-parallel`, `technique-mla`, `technique-fia`