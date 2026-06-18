---
id: technique-pr-vllm-ascend-5095
title: "PR Insight: vllm-project/vllm-ascend #5095"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - testing
  - deepseek
  - eplb
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5095"
---

# PR Insight: vllm-project/vllm-ascend #5095

**Title:** [Bugfix] EPLB nightly deepseek

## Overview
This PR fixes a bug in the nightly test workflow where the smoke test file name for DeepSeek EPLB (Expert Parallel Load Balancing) was changed but the script wasn't updated accordingly.

## Technical Significance
Proper test file referencing is essential for CI/CD pipeline reliability. This fix ensures that nightly regression tests for DeepSeek models with EPLB run correctly on Ascend NPUs, catching regressions early in the development cycle.

## Related
- technique-moe
- technique-load-balancing