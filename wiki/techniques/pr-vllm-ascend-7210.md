---
id: technique-pr-vllm-ascend-7210
title: "PR Insight: vllm-project/vllm-ascend #7210"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - tensor-parallelism
  - linear-op
  - code-refactoring
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7210"
---

# PR Insight: vllm-project/vllm-ascend #7210

**Title:** Refactor duplicated code into a common method to reduce redundancy

## Overview
This PR refactors duplicated tensor parallelism code by extracting _get_input_parallel_ into the parent class _CustomRowParallelOp_ and using it across five child classes (MLPRowParallelOp, OProjRowParallelOp, Flashcomm2OProjRowParallelOp, MatmulAllreduceRowParallelOp, SequenceRowParallelOp). It also fixes a typo (split vs splitted).

## Technical Significance
This refactoring improves code maintainability for tensor-parallel linear operators on Ascend. The duplication was affecting multiple linear operation variants including MLP output projection and flash communication paths. By centralizing the input parallel preparation logic, it ensures consistent behavior across all tensor-parallel linear operations and reduces bugs from不一致的实现。

## Related
- technique-tensor-parallelism
- technique-operator-fusion