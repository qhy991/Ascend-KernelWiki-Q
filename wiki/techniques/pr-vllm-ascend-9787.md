---
id: technique-pr-vllm-ascend-9787
title: "PR Insight: vllm-project/vllm-ascend #9787"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - glm
  - tool-call
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9787"
---

# PR Insight: vllm-project/vllm-ascend #9787

**Title:** [BugFix][Platform] Patch GLM tool-call final chunks

## Overview
This PR patches GLM tool-call handling for final chunks, addressing issues that occur when tool-call responses are split across multiple decode steps. It ensures correct handling of tool-call content in chunked output scenarios.

## Technical Significance
Fixes GLM tool-call inference by properly handling final chunks, ensuring that tool-call responses are correctly assembled and returned even when split across multiple decode iterations. This prevents malformed or incomplete tool-call outputs.

## Related
- `technique-tool-call`, `pattern-chunking`, `technique-glm`