---
id: technique-pr-modellink-2737
title: "PR Insight: Ascend/ModelLink #2737"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mindspore
  - dualpipe
  - feature
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2737"
---

# PR Insight: Ascend/ModelLink #2737

**Title:** support mindspore dualpipe

## Overview
This PR adds support for the dualpipe mechanism in the MindSpore backend. Dualpipe enables overlapping computation and communication operations to hide latency during distributed training.

## Technical Significance
Dualpipe is a key optimization for distributed training on Ascend NPUs. By overlapping computation with HCCL communication, it reduces idle time and improves overall training throughput for large-scale models using MindSpore.

## Related
- technique-pipeline-scheduling
- technique-hccl-optimization