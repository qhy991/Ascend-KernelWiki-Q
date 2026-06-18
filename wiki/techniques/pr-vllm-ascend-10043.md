---
id: technique-pr-vllm-ascend-10043
title: "PR Insight: vllm-project/vllm-ascend #10043"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - placeholder-tokens
  - sampler
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10043"
---

# PR Insight: vllm-project/vllm-ascend #10043

**Title:** [BugFix][SpecDecode] Reject placeholder draft tokens in sampler

## Overview
This PR fixes speculative decoding by ensuring that placeholder draft tokens are rejected in the sampler. Placeholder tokens were being accepted incorrectly, leading to invalid draft sequences and reduced acceptance rates.

## Technical Significance
Improves spec decode correctness by explicitly rejecting placeholder draft tokens in the sampler. Prevents invalid token sequences from being processed and ensures that only legitimate draft tokens are considered during validation, improving spec decode reliability and accuracy.

## Related
- `technique-spec-decode`, `technique-sampling`, `pattern-token-handling`