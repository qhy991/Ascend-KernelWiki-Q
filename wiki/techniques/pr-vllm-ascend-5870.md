---
id: technique-pr-vllm-ascend-5870
title: "PR Insight: vllm-project/vllm-ascend #5870"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactor
  - spec-decode
  - eagle
  - mtp
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5870"
---

# PR Insight: vllm-project/vllm-ascend #5870

**Title:** [Refactor][EAGLE] 4/N extract common methods from eagle and mtp

## Overview
This PR extracts common methods from eagle_proposer and mtp_proposer as part of a multi-step effort to merge the two speculative decoding approaches. It's the fourth step in the refactoring process outlined in RFC #5467.

## Technical Significance
EAGLE and MTP are both speculative decoding techniques with overlapping functionality. By extracting common methods into shared utilities, the PR reduces code duplication and paves the way for eventual unification. This refactoring improves maintainability by consolidating duplicate logic and making it easier to add features that benefit both approaches. The changes affect both proposer implementations and their corresponding unit tests.

## Related
- `technique-spec-decode`, `technique-eagle`, `technique-mtp`, `technique-code-refactor`