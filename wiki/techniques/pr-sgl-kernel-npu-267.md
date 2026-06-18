---
id: technique-pr-sgl-kernel-npu-267
title: "PR Insight: sgl-project/sgl-kernel-npu #267"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - long-sequence
  - ant-migration
  - prefill
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/267"
---

# PR Insight: sgl-project/sgl-kernel-npu #267

**Title:** Add the long-sequence ant migration feature for the prefill combine operator.

## Overview
Implements long-sequence ant migration feature for prefill combine operators, supporting sequences up to 32K tokens with configurable round-based processing. Performance benchmarks show 82-110 GB/s bandwidth across various batch sizes.

## Technical Significance
Long sequence support is critical for modern LLM applications requiring extended context windows. The ant migration feature enables efficient processing of sequences that exceed standard memory limits, while the configurable round-based processing provides flexibility for different hardware constraints. The excellent bandwidth utilization ensures efficient long-sequence inference.

## Related
- `wiki-kernel-moe`
- `wiki-technique-long-sequence`
- `wiki-technique-prefill`
- `wiki-technique-segmentation`