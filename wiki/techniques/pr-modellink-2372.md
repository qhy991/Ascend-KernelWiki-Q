---
id: technique-pr-modellink-2372
title: "PR Insight: Ascend/ModelLink #2372"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - deterministic
  - reproducibility
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2372"
---

# PR Insight: Ascend/ModelLink #2372

**Title:** 加入npu-deterministic的dummy arg

## Overview
This PR adds a dummy argument for `npu-deterministic` configuration, enabling deterministic computation mode for NPU operations. This feature ensures reproducible training results across runs by controlling nondeterministic operations like atomic reductions.

## Technical Significance
Deterministic training is essential for debugging, scientific reproducibility, and compliance requirements. On NPU hardware, operations like reduction and attention computation may have implementation-level nondeterminism due to parallel execution order. The `npu-deterministic` flag forces serialized or deterministic execution paths at the cost of some performance, enabling exact reproducibility of training results on Ascend hardware for ModelLink workloads.

## Related
- `technique-deterministic-execution`
- `technique-reduction-optimization`