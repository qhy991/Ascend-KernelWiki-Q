---
id: technique-pr-vllm-ascend-10003
title: "PR Insight: vllm-ascend #10003"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - cudagraph
  - eager-mode
  - dsv4
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10003"
---

# PR Insight: vllm-ascend #10003 - Fix dsv4 Piecewise Scenario

## Overview

This PR addresses a configuration parsing bug affecting the DeepSeek V4 (dsv4) piecewise scenario within `vllm-ascend`. It resolves an issue where the model execution incorrectly falls back to eager mode when it should be utilizing graph compilation.

## Architectural Explanation

In vLLM, graph execution (via CUDA Graphs or Ascend Graphs) is critical for reducing CPU overhead and improving latency during the decode phase. However, dynamic execution scenarios often require graph breaks, managed by features like breakable graphs.

In upstream vLLM (e.g., PR #43746), the `VLLM_USE_BREAKABLE_CUDAGRAPH` environment variable was introduced to manage breakable graph modes. Prior to this fix in `vllm-ascend`, if `VLLM_USE_BREAKABLE_CUDAGRAPH` was detected as `True`, a logic error caused `compilation_config.mode` to be set to `None`—even if a compilation mode was explicitly specified. 

Because the compilation mode evaluated to `None`, the backend skipped generating the execution graph. As a result, the server silently fell back to running in **eager mode**. Running a large model like DeepSeek V4 in eager mode leads to significant performance degradation due to the continuous operator dispatch overhead.

### Resolution
This patch ensures that `compilation_config.mode` is properly preserved when breakable graphs are enabled. This allows the DeepSeek V4 piecewise scenario to correctly compile and execute in graph mode, restoring optimal inference performance on Ascend NPUs.
