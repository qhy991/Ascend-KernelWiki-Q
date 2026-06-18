---
id: technique-pr-vllm-ascend-2409
title: "PR Insight: vllm-project/vllm-ascend #2409"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-ops
  - registration
  - worker
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2409"
---

# PR Insight: vllm-project/vllm-ascend #2409

**Title:** [Bugfix] Fix custom op register issue

## Overview
This PR fixes a custom operator registration issue where the registration patch lost its effect when new processes were started by creating workers. The fix moves the patch code from platform initialization to the worker initialization in `vllm_ascend/worker/worker_v1.py` to ensure custom ops are properly registered in all processes.

## Technical Significance
This bugfix ensures that custom operator registrations persist across worker process creation, preventing fallback to native vLLM passes when workers are spawned. By moving the registration to the worker initialization phase, the system guarantees that custom operators work as expected in all execution contexts.

## Related
- `technique-custom-ops`, `technique-operator-registration`, `technique-worker-initialization`, `technique-process-management`