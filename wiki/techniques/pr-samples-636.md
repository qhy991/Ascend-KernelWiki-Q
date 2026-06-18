---
id: technique-pr-samples-636
title: "PR Insight: Ascend/samples #636"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - documentation
  - accuracy
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/636"
---

# PR Insight: Ascend/samples #636

**Title:** 样例运行结果处增加提示说明，结果信息中的精度需以实际情况为准

## Overview
This PR adds explanatory notes to sample output results, clarifying that accuracy information shown in results should be based on actual conditions rather than fixed expected values. This prevents users from being misled by static accuracy numbers in sample documentation.

## Technical Significance
Improves user expectations by clarifying that inference accuracy varies based on factors like input data, model version, quantization settings, and hardware configuration. This documentation improvement helps users understand that reported accuracy is for reference and actual results may differ.

## Related
- Documentation clarity
- Accuracy reporting
- Inference results
- User expectations