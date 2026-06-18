---
id: technique-pr-vllm-ascend-913
title: "PR Insight: vllm-project/vllm-ascend #913"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - moe
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/913"
---

# PR Insight: vllm-project/vllm-ascend #913

**Title:** [Fix] Fix update_aclgraph_sizes when running MoE models

## Overview
This PR fixes the `update_aclgraph_sizes` function when running MoE models, addressing issues with size calculations in aclgraph mode. The changes affect distributed parallel state, platform, utilities, and worker implementations.

## Technical Significance
Correct size calculations are critical for aclgraph mode, which requires accurate tensor shape information for graph compilation. MoE models introduce additional complexity with expert routing and parallel communication, making proper size updates essential for correct execution and resource allocation.

## Related
- `technique-aclgraph`
- `kernel-moe`
- `kernel-inference`