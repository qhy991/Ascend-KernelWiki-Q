---
id: technique-pr-vllm-ascend-9530
title: "PR Insight: vllm-project/vllm-ascend #9530"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v4
  - dsa
  - multistream
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9530"
---

# PR Insight: vllm-project/vllm-ascend #9530

**Title:** [BugFix] Fixed the issue where cv_indexer_qkv_prepare's multistream parallel capability was not enabled when multistream-dsv4-dsa-overlap=true

## Overview
This PR fixes an issue where the cv_indexer_qkv_prepare operation's multistream parallel capability was not being enabled even when the multistream-dsv4-dsa-overlap configuration was set to true. The fix is in the DSA attention and operator implementations.

## Technical Significance
Multistream parallelism is a key optimization for DSA operations, and ensuring it's properly enabled when configured is critical for achieving expected performance. The fix ensures that the configuration flag correctly enables the optimization.

## Related
- `kernel-attention`
- `technique-pipeline-scheduling`