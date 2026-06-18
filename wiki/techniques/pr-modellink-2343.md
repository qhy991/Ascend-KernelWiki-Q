---
id: technique-pr-modellink-2343
title: "PR Insight: Ascend/ModelLink #2343"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - tp2d
  - documentation
  - testing
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2343"
---

# PR Insight: Ascend/ModelLink #2343

**Title:** TP2D看护用例+说明文档

## Overview
This PR adds test cases and documentation for TP2D (2D Tensor Parallelism). The work includes validation test cases and explanatory documentation for using 2D tensor parallelism in ModelLink.

## Technical Significance
2D tensor parallelism distributes matrix operations across both row and column dimensions, enabling better scalability for very large models. This requires specialized data layout transformations and communication patterns. The test cases ensure correctness of the 2D TP implementation on Ascend hardware, while documentation guides users on when and how to use 2D TP versus 1D tensor parallelism for optimal performance on large models like DeepSeekV3 and Qwen.

## Related
- `technique-tensor-parallelism`
- `technique-2d-tp`