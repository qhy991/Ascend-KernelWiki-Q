---
id: technique-pr-vllm-ascend-9688
title: "PR Insight: vllm-project/vllm-ascend #9688"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - mtp
  - scheduler
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9688"
---

# PR Insight: vllm-project/vllm-ascend #9688

**Title:** [BugFix] [P/D] avoid MTP placeholders exceeding max model length

## Overview
This PR fixes MTP placeholder token overflow in recompute scheduler when decode nodes enable MTP. When `is_mtp_kv_consumer` is enabled, the scheduler fills `request.spec_token_ids` with MTP placeholders, but for the first incoming request where length is close to `max_model_len`, this could exceed the limit.

## Technical Significance
Adds boundary check `self.max_model_len >= (request.num_tokens + self.num_spec_tokens)` before filling MTP placeholders, preventing invalid scheduling behavior. Ensures MTP placeholders are only added when requests can fit within the model length limit, avoiding scheduling failures for the first request on decode nodes.

## Related
- `technique-spec-decode`, `technique-mtp`, `pattern-scheduler`