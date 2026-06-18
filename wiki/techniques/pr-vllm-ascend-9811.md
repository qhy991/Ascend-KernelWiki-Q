---
id: technique-pr-vllm-ascend-9811
title: "PR Insight: vllm-project/vllm-ascend #9811"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/9811"
---

# PR Insight: vllm-project/vllm-ascend #9811

**Title:** [BugFix] [P/D] avoid MTP placeholders exceeding max model length

## Overview
This PR is another backport of the MTP placeholder overflow fix (#9688, #9749) to address the same scheduling issue where MTP placeholder tokens could exceed max_model_len for the first incoming request on decode nodes.

## Technical Significance
Ensures robust MTP operation across multiple maintenance branches by backporting critical scheduling fixes. Prevents invalid scheduling behavior in production environments using different release branches.

## Related
- `technique-spec-decode`, `technique-mtp`, `pattern-scheduler`