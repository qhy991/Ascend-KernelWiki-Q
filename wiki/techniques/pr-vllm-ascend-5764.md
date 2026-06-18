---
id: technique-pr-vllm-ascend-5764
title: "PR Insight: vllm-project/vllm-ascend #5764"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - mlapo
  - bmm-transpose
  - input-constraints
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5764"
---

# PR Insight: vllm-project/vllm-ascend #5764

**Title:** [Bugfix] Fix the input constraints checks for the mlapo and bmm_transpose operators

## Overview
This PR fixes input constraint validation for the `mlapo` and `bmm_transpose` operators in the SFA (Sparse Flash Attention) and MLA attention implementations. The bug was in `sfa_v1.py` and `mla_v1.py` where incorrect input dimension checks were causing operators to be incorrectly disabled or used with incompatible tensor shapes. The fix updates the constraint checking logic to properly validate input tensor dimensions and conditions for these operators.

## Technical Significance
This bugfix corrects operator selection logic that was preventing optimal operator usage or causing incorrect operator usage due to improper constraint validation. The impact was observed in performance benchmarks: before the fix, TPOT was 29ms, TTFT was 47s, and TPS was 606 token/s. After the fix, TPOT remained at 29ms, TTFT increased slightly to 48s, but TPS improved to 636 token/s. The 30 TPS improvement indicates that proper operator selection significantly improved inference throughput by ensuring operators were used correctly and efficiently.

## Related
- `technique-attention`, `technique-mla`, `technique-sfa`, `technique-operator-selection`