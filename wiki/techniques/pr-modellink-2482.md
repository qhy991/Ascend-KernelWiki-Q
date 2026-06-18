---
id: technique-pr-modellink-2482
title: "PR Insight: Ascend/ModelLink #2482"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - mtp
  - arguments
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2482"
---

# PR Insight: Ascend/ModelLink #2482

**Title:** add mtp-optim-mem args

## Overview
This PR adds mtp-optim-mem arguments to the training configuration. MTP (likely Multi-Task Parallelism or similar) memory optimization arguments help control memory usage during training on Ascend hardware.

## Technical Significance
Memory optimization arguments enable fine-grained control over memory consumption for large model training on Ascend NPUs. This helps balance training speed and memory usage constraints.

## Related
- memory optimization
- training configuration