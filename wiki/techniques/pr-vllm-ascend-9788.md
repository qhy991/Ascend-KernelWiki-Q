---
id: technique-pr-vllm-ascend-9788
title: "PR Insight: vllm-project/vllm-ascend #9788"
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
  - "https://github.com/vllm-project/vllm-ascend/pull/9788"
---

# PR Insight: vllm-project/vllm-ascend #9788

**Title:** [BugFix][v0.20.2rc] Patch GLM tool-call final chunks

## Overview
This PR is a backport of the GLM tool-call final chunks patch (#9787) to the v0.20.2rc branch. It addresses the same issue of handling tool-call responses split across multiple decode steps.

## Technical Significance
Ensures production stability by backporting critical GLM tool-call fixes to the release candidate branch. Prevents malformed tool-call outputs in production deployments using v0.20.2rc.

## Related
- `technique-tool-call`, `pattern-chunking`, `technique-glm`