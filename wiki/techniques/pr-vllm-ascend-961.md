---
id: technique-pr-vllm-ascend-961
title: "PR Insight: vllm-project/vllm-ascend #961"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - expert-parallel
  - bugfix
  - compatibility
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/961"
---

# PR Insight: vllm-project/vllm-ascend #961

**Title:** [WIP][BugFix]Fix accuracy issues caused by wrong etp_size passed into FusedMoEParallelConfig when using vLLM 0.9.0

## Overview
This PR fixes accuracy issues in vLLM 0.9.0 caused by incorrect `tp_size` passed to `FusedMoEParallelConfig`. The root cause is different EP (expert parallel) detection logic between vLLM and vllm-ascend - vLLM uses flags while vllm-ascend uses etp groups.

## Technical Significance
Correct parallel configuration is essential for MoE model accuracy. The fix addresses vLLM 0.9.0 changes to EP detection, ensuring that weight splitting uses the correct tensor parallel size and preventing numerical errors in MoE computations.

## Related
- `kernel-moe`
- `technique-expert-parallel`
- `technique-tensor-parallel`