---
id: technique-pr-vllm-ascend-3822
title: "PR Insight: vllm-project/vllm-ascend #3822"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pcp
  - mtp
  - pd
  - disaggregated
  - spec-decode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3822"
---

# PR Insight: vllm-project/vllm-ascend #3822

**Title:** [feature] support pcp + mtp (with pd disaggregate, only pcp in P nodes)

## Overview
This PR adds support for PCP (Prefill-Compute-Parallel) combined with MTP (multi-text-prompt) in disaggregated inference with PD (Prefill-Decode) separation, where only PCP is used in P nodes. The implementation adds 112 lines to `vllm_ascend/spec_decode/mtp_proposer.py` and 73 lines to `vllm_ascend/worker/model_runner_v1.py`.

## Technical Significance
Combining PCP with MTP in disaggregated inference enables efficient resource utilization by parallelizing prefill computation while maintaining MTP's speculative decoding benefits. This allows P nodes to handle prefill phases efficiently with PCP while MTP provides spec decode acceleration across the distributed system.

## Related
- `technique-pcp`
- `technique-mtp`
- `technique-disaggregated-inference`
- `technique-spec-decode`