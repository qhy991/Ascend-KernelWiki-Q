---
id: technique-pr-modellink-2578
title: "PR Insight: Ascend/ModelLink #2578"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - dualpipe
  - training
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2578"
---

# PR Insight: Ascend/ModelLink #2578

**Title:** [mcore]support mla-swap-core-attn-out in dualpipev with 1f1b_overlap

## Overview
This PR adds support for MLA (Multi-Head Latent Attention) swap-core-attention-output operations in dualpipev with 1F1B (one-forward-one-backward) overlap scheduling. The implementation optimizes attention output handling in the dual pipeline execution engine.

## Technical Significance
Dualpipe with 1F1B overlap is a pipeline parallelism technique that improves device utilization by overlapping forward and backward passes. MLA swap operations require careful synchronization and memory management. This change optimizes the attention output swap, reducing memory footprint and improving training throughput on Ascend NPUs.

## Related
- `technique-pipeline-scheduling`