---
id: technique-pr-vllm-ascend-7309
title: "PR Insight: vllm-project/vllm-ascend #7309"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eagle3
  - context-parallelism
  - speculative-decoding
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7309"
---

# PR Insight: vllm-project/vllm-ascend #7309

**Title:** [eagle3][pcp] fix bug for eagle3 and cp enable

## Overview
This PR fixes a bug introduced by the parallel speculative inference PR when Eagle3 and context parallelism are both enabled. The fix addresses compatibility issues between the Eagle3 draft proposer and CP-enabled scenarios.

## Technical Significance
This bugfix matters for Ascend speculative decoding with context parallelism. Eagle3 is a popular draft model for speculative decoding, and combining it with CP requires careful handling of metadata and attention state. The fix ensures correct draft proposal and acceptance when CP is enabled, enabling efficient inference with both techniques.

## Related
- technique-speculative-decoding
- technique-context-parallelism