---
id: technique-pr-vllm-ascend-8547
title: "PR Insight: vllm-project/vllm-ascend #8547"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - mtp
  - deepseek-v3.2
  - bugfix
  - slot-mapping
  - decode
  - corner-case
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8547"
---

# PR Insight: vllm-project/vllm-ascend #8547

**Title:** [BugFix][PCP] Fix incorrect slot mapping for DeepSeek 3.2 PCP+MTP decode path

## Overview
This PR fixes a bug in certain corner cases when PCP (Prefill Context Parallelism) and MTP are enabled together for DeepSeek 3.2. In the original decode + PCP + MTP branch, the code assumed that every request has the same number of decode tokens. In special cases, this assumption does not hold, which can cause the decode slot mapping to be computed incorrectly. The fix computes the decode slot mapping using the actual decode token count of each request.

## Technical Significance
This fix is critical for correct inference in DeepSeek 3.2 deployments with PCP+MTP enabled. The assumption of uniform decode token counts is a common simplification that can fail in edge cases, leading to incorrect slot mapping and inference errors. The PR demonstrates the importance of handling variable-length sequences correctly in complex parallel deployment scenarios.

## Related
- `technique-context-parallel`
- `technique-slot-mapping`
- `technique-deepseek-v3.2`