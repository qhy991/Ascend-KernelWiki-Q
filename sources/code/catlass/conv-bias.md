---
id: code-catlass-conv-bias
title: CATLASS Conv Bias Example
type: source-code
repo: Ascend/catlass
path: examples/24_conv_bias
url: https://gitee.com/ascend/catlass/tree/master/examples/24_conv_bias
source_category: upstream-code
architectures:
- ascend910b
tags:
- catlass
- convolution
- bias
- cube
date: '2026-06-18'
captured_at: '2026-06-18'
confidence: source-reported
hardware_features:
- cube-unit
- vector-unit
- l1-buffer
- l0-buffer
techniques:
- data-reuse
- tiling-strategy
- cube-vector-overlap
kernel_types:
- conv
- elementwise
languages:
- cpp
- ascendc
---

# CATLASS Conv Bias Example

CATLASS convolution-plus-bias example anchoring non-GEMM Cube workloads and fused vector epilogue patterns in the Ascend code corpus.

## Code Location

- Repository: `Ascend/catlass`
- Path: `examples/24_conv_bias`
- URL: https://gitee.com/ascend/catlass/tree/master/examples/24_conv_bias
