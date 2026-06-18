---
id: technique-pr-vllm-ascend-8178
title: "PR Insight: vllm-project/vllm-ascend #8178"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - tool-call
  - glm
  - streaming
  - api
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8178"
---

# PR Insight: vllm-project/vllm-ascend #8178

**Title:** [BugFix][Platform] Fix extra function name in final chunk of streaming tool calls

## Overview
This PR fixes a bug in the GLM tool call parser where the `function.name` field was incorrectly included in non-first chunks of streaming tool calls. According to OpenAI streaming semantics, `id`, `type`, and `function.name` should only appear in the first chunk for each tool call index. The fix tracks whether arguments have already been streamed and only populates header fields for genuine first chunks.

## Technical Significance
The fix ensures OpenAI API compatibility for GLM models using tool calls by preventing duplicate `function.name` fields in streaming responses. This correctness fix addresses a violation of streaming API semantics that could cause client-side parsing errors. The solution involves careful state tracking to distinguish between first and subsequent chunks in the streaming protocol.

## Related
- `technique-api-compatibility`
- `technique-streaming-protocol`