---
id: technique-pr-vllm-ascend-3208
title: "PR Insight: vllm-project/vllm-ascend #3208"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - dp
  - dummy-run
  - mode-consistency
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3208"
---

# PR Insight: vllm-project/vllm-ascend #3208

**Title:** [Aclgraph][DP] Fix dp dummy run not in aclgraph error

## Overview
This PR fixes an issue where DP (Data Parallel) groups executing dummy_run would use different execution modes than other DP groups in non-equilibrium scenarios. The fix ensures all DP groups run in the same mode, improving performance consistency in DP scenarios.

## Technical Significance
Execution mode consistency across DP groups is critical for performance and correctness. Mixed execution modes can cause performance degradation or correctness issues. The fix ensures that dummy_run uses the same ACL graph mode as actual execution, providing accurate profiling and consistent behavior.

## Related
- `technique-aclgraph`, `pattern-dp-consistency`, `pattern-dummy-run-optimization`