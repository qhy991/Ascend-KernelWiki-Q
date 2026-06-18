---
id: technique-pr-samples-2013
title: "PR Insight: Ascend/samples #2013"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - amct
  - tensorflow
  - pruning
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2013"
---

# PR Insight: Ascend/samples #2013

**Title:** modify amct tf auto channel prune code path

## Overview
This PR modifies the code path for automatic channel pruning in AMCT (Ascend Model Compression Toolkit) TensorFlow samples. The changes improve or fix channel pruning functionality for model compression workflows.

## Technical Significance
Channel pruning reduces model size and inference latency by removing less important output channels. This sample demonstrates how to use AMCT for automated channel pruning on TensorFlow models, which is a key technique for optimizing models for deployment on Ascend hardware.

## Related
- `technique-ascendc`