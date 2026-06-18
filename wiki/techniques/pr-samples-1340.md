---
id: technique-pr-samples-1340
title: "PR Insight: Ascend/samples #1340"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - amct
  - tensorflow
  - sparsity
  - quantization
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1340"
---

# PR Insight: Ascend/samples #1340

**Title:** amct_tensorflow新增4选2稀疏配置文件

## Overview
This PR adds a new 4-select-2 sparsity configuration file for the AMCT (Ascend Model Compression Toolkit) TensorFlow samples. The configuration enables model compression through structured sparsity.

## Technical Significance
Sparsity compression reduces model size and improves inference performance by removing redundant parameters. The 4-select-2 pattern is a common structured sparsity scheme compatible with Ascend hardware acceleration.

## Related
- `technique-model-compression`
- `pattern-sparsity`