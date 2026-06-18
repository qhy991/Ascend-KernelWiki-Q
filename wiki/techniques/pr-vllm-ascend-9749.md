---
id: technique-pr-vllm-ascend-9749
title: "PR Insight: vllm-project/vllm-ascend #9749"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - mtp
  - scheduler
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9749"
---

# PR Insight: vllm-project/vllm-ascend #9749

**Title:** [BugFix] [P/D] avoid MTP placeholders exceeding max model length

## Overview
This PR is a backport of the fix for MTP placeholder token overflow in recompute scheduler, identical to #9688. It addresses the issue where MTP placeholder tokens could exceed max_model_len for the first incoming request on decode nodes.

## Technical Significance
Adds boundary check before filling MTP placeholder tokens, preventing invalid scheduling behavior when request length plus spec tokens exceeds model length limit. Ensures robust MTP operation in production (v0.20.2rc) scenarios.

## Related
- `technique-spec-decode`, `technique-mtp`, `pattern-scheduler`