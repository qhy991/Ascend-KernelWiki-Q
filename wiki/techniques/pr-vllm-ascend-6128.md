---
id: technique-pr-vllm-ascend-6128
title: "PR Insight: vllm-project/vllm-ascend #6128"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - npugraph-ex
  - static-kernel
  - lifecycle
  - signal-handling
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6128"
---

# PR Insight: vllm-project/vllm-ascend #6128

**Title:** [bugfix][npugraph_ex]fix static kernel uninstall issue

## Overview
This PR fixes a static kernel uninstall issue when using the npugraph_ex backend. The issue occurs because vLLM terminates worker processes directly without triggering Python's atexit mechanism that normally unloads static kernels. The fix adds a signal handler to explicitly unload static kernels before process termination, and handles slow unloads by starting a new process.

## Technical Significance
Static kernel unloading can be time-consuming with many kernels, and direct process killing leaves kernels loaded on the NPU. The signal handler ensures proper cleanup and resource management, while the new process spawning handles cases where unloading takes longer than the termination timeout, preventing resource leaks across model service restarts.

## Related
- `technique-npugraph-ex`, `technique-static-kernel`, `technique-lifecycle-management`