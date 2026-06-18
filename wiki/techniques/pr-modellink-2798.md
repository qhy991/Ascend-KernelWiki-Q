---
id: technique-pr-modellink-2798
title: "PR Insight: Ascend/ModelLink #2798"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - pytorch
  - performance
  - pipeline-parallel
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2798"
---

# PR Insight: Ascend/ModelLink #2798

**Title:** add pipeline time info for update 0.12.1

## Overview
This PR adds pipeline time information tracking for LLM version 0.12.1 update. It enables performance monitoring for pipeline parallelism training.

## Technical Significance
Pipeline timing information helps identify inefficiencies in pipeline parallel execution on Ascend NPUs. This monitoring capability enables users to optimize pipeline configuration and reduce idle time, improving overall throughput.

## Related
- `technique-pipeline-scheduling`
- `technique-distributed-training`