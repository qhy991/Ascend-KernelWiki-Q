---
id: technique-pr-vllm-ascend-10191
title: "PR Insight: vllm-project/vllm-ascend #10191"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - npugraph
  - communication
  - graph-mode
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10191"
---

# PR Insight: vllm-project/vllm-ascend #10191

**Title:** [Feature] Auto-compute LOCAL_WORLD_SIZE when static_kernel is enabled

## Overview
This PR adds automatic computation of the `LOCAL_WORLD_SIZE` environment variable for static kernel coordination and adds `clone_input=False` and `clone_output=False` options to npugraph_ex. The auto-computation derives the value from parallel configuration (`local_world_size * data_parallel_size_local`) when static kernels are enabled and the environment variable is not already set. This is necessary because npugraph_ex's static kernel feature requires `LOCAL_WORLD_SIZE` for creating per-node Gloo groups for coordinating compilation and `.run` package installation across ranks.

## Technical Significance
This feature enables reliable static kernel compilation and graph replay in distributed environments on Ascend. The `LOCAL_WORLD_SIZE` coordinate ensures that all ranks within a node can properly synchronize during graph compilation and package installation, which is critical for npugraph_ex's static kernel functionality. The addition of `clone_input=False` eliminates redundant tensor copying during graph capture and replay, improving performance by avoiding unnecessary memory operations.

## Related
- `technique-graph-mode`
- `technique-distributed-communication`
- `technique-npugraph`