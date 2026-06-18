---
id: technique-pr-vllm-ascend-10612
title: "PR Insight: vllm-ascend #10612"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactor
  - deepseek
  - integration
  - vllm-core
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10612"
---

# PR Insight: vllm-ascend #10612 - Remove redundant DeepSeek V4 thinking patch

## Overview

PR #10612 is a refactoring effort in the `vllm-ascend` repository to clean up redundant platform patches related to DeepSeek V4's reasoning and thinking capabilities. As the Ascend ecosystem tracks upstream `vllm-project/vllm` features, patches are sometimes used to temporarily backport upstream changes to supported release versions. 

With the adoption of the officially supported vLLM release `v0.22.1`, the specific behaviors patched for DeepSeek V4 are now natively supported by the upstream core, making the Ascend-specific platform patch redundant.

## Technical Details

The removed patch was originally used to backport support for specific reasoning parameter configurations in the DeepSeek V4 tokenizer and chat API. The upstream `v0.22.1` release handles this natively by:

1. **`reasoning_effort` API Expansion**: Allowing the `reasoning_effort` parameter to accept expanded values such as `minimal`, `xhigh`, and `max`.
2. **Thinking Flag Propagation**: Ensuring `ChatCompletionRequest.build_chat_params` properly propagates the `enable_thinking` flag whenever a specific `reasoning_effort` is requested.
3. **Tokenizer Mapping**: Implementing native logic in the DeepSeek V4 tokenizer to correctly map `reasoning_effort=none` to standard chat mode, while interpreting `xhigh` or `max` as maximum reasoning effort contexts.

## Conclusion

By removing this redundant patch, the `vllm-ascend` integration reduces its maintenance burden and aligns more closely with the upstream `vllm` codebase. This ensures the tokenizer and chat parameter processing for DeepSeek V4 rely entirely on the robust upstream implementations provided in vLLM `v0.22.1`.
