---
id: technique-pr-modellink-2474
title: "PR Insight: Ascend/ModelLink #2474"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - dualpipe
  - optimizer
  - overlapping
  - communication
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2474"
---

# PR Insight: Ascend/ModelLink #2474

**Title:** 【master】【dualpipeV +1f1b overlap+swap optimizer】

## Overview
This PR implements DualPipeV with 1F1B (one forward one backward) overlap and optimizer state swapping. DualPipe is an advanced pipeline parallelism technique that overlaps computation and communication more efficiently.

## Technical Significance
DualPipeV with 1F1B overlap and optimizer swapping improves training throughput by better utilizing Ascend NPU compute and communication resources. This reduces pipeline bubbles and improves overall training efficiency.

## Related
- DualPipe parallelism
- 1F1B scheduling
- optimizer state offloading