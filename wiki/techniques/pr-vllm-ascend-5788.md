---
id: technique-pr-vllm-ascend-5788
title: "PR Insight: vllm-project/vllm-ascend #5788"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - dispatch-ffn-combine
  - ep32
  - configuration
  - moe
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5788"
---

# PR Insight: vllm-project/vllm-ascend #5788

**Title:** [0.13.0]enable ep32 for dispatch_ffn_combine

## Overview
This PR is a cherry-pick to version 0.13.0 that enables ep32 (expert parallel with 32 experts per device) support for the dispatch_ffn_combine operator. The changes are identical to PR #5787, updating `ascend_forward_context.py` and `envs.py` configuration settings to allow the operator to work with ep32 configurations in the 0.13.0 release branch.

## Technical Significance
This cherry-pick brings the ep32 support to the 0.13.0 release branch, enabling users on this version to benefit from higher expert parallelism degrees with the dispatch_ffn_combine operator. The configuration change allows large MoE models to better scale by distributing experts across more devices. The single operator testing confirmed functionality, ensuring users can leverage improved throughput on large MoE deployments with the 0.13.0 release.

## Related
- `technique-moe`, `technique-expert-parallel`, `technique-dispatch-ffn-combine`