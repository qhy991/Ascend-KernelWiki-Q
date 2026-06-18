---
id: technique-pr-mindspeed-2570
title: "PR Insight: Ascend/MindSpeed #2570"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - feature
  - communication
  - performance
  - dualpipev
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2570"
---

# PR Insight: Ascend/MindSpeed #2570

**Title:** [Feat] dualpipev&fboverlap mtp support with core

## Overview
This PR adds support for dual pipeline and forward-backward overlap MTP (Megatron-Transformer-Pipeline) integration with the core training framework. The feature enables advanced pipeline parallelism strategies with compute-communication overlap to improve training throughput.

## Technical Significance
Dual pipeline and forward-backward overlap are advanced techniques for maximizing hardware utilization in large-scale distributed training. This feature enables overlapping computation with communication across pipeline stages, reducing idle time and improving training efficiency. It's particularly valuable for memory-bound workloads on Ascend clusters with HCCS interconnects.

## Related
- `technique-pipeline-scheduling`
- `technique-cube-vector-overlap`
- `technique-hccl-optimization`