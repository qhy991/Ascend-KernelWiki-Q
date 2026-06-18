---
id: technique-pr-cann-ops-adv-308
title: "PR Insight: Ascend/cann-ops-adv #308"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - softmax
  - transformer
  - validation
  - api-compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/cann-ops-adv/pulls/308"
---

# PR Insight: Ascend/cann-ops-adv #308

**Title:** 修复高阶API新增校验导致ScaledMaskedSoftmaxGradV2算子ut报错问题

## Overview
This PR fixes unit test errors in the ScaledMaskedSoftmaxGradV2 operator caused by newly added validation in high-level APIs. The changes address compatibility issues between API validation logic and existing operator implementations.

## Technical Significance
API validation additions can break existing operator tests if not carefully designed. This fix ensures the ScaledMaskedSoftmaxGradV2 operator works correctly with new high-level API checks while maintaining backward compatibility. The operator is critical for transformer attention gradient computation, so ensuring it passes unit tests is essential for model training correctness. The fix likely adjusts validation thresholds, adds compatibility handling, or fixes the validation logic itself.

## Related
- `technique-softmax-ascendc`
- `technique-transformer-attention`
- `technique-api-validation`
- `technique-backward-compatibility`