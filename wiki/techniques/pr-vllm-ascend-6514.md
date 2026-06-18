---
id: technique-pr-vllm-ascend-6514
title: "PR Insight: vllm-project/vllm-ascend #6514"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - speculative-decoding
  - bugfix
  - eager-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6514"
---

# PR Insight: vllm-project/vllm-ascend #6514

**Title:** [Bugfix] fix bug for mtp

## Overview
This PR fixes critical bugs in the MTP (Multi-Token Proposal) speculative decoding core execution logic, specifically addressing issues in eager mode execution and the _update_states_after_model_execute function. It also updates test cases to validate eager mode acceptance rates.

## Technical Significance
Resolves functional issues in MTP speculative decoding that could cause incorrect token proposal generation or state management. The fixes improve stability and correctness of speculative decoding workflows, particularly in eager execution mode.

## Related
- `technique-speculative-decoding`