---
id: technique-pr-vllm-ascend-10004
title: "PR Insight: vllm-project/vllm-ascend #10004"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - sampling
  - top-k
  - top-p
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10004"
---

# PR Insight: vllm-project/vllm-ascend #10004

**Title:** [BugFix] Fix reduce sampling where top_k and top_p could be None

## Overview
This PR fixes reduce sampling logic where top_k and top_p parameters could be None, causing errors in sampling operations. It adds proper handling for cases where these sampling parameters are not specified.

## Technical Significance
Fixes sampling robustness by properly handling None values for top_k and top_p parameters. Prevents crashes or incorrect behavior when sampling parameters are unset or explicitly set to None, improving sampling flexibility and reliability.

## Related
- `technique-sampling`, `pattern-validation`, `pattern-parameter-handling`