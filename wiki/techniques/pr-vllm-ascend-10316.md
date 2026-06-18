---
id: technique-pr-vllm-ascend-10316
title: "PR Insight: vllm-project/vllm-ascend #10316"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - weight-loading
  - deepseek
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10316"
---

# PR Insight: vllm-project/vllm-ascend #10316

**Title:** [Bugfix] use endswith for .scale parameter matching in MTP model

## Overview
This PR fixes a parameter matching bug in the MTP (Multi-Token Prediction) model weight loading code. The original code used `if ".scale" in name` for substring matching, which was too broad and matched any parameter name containing `.scale` as a substring, even if it didn't end with `.scale` (e.g., `foo.scale_bar`). This caused unintended renaming of parameters to `.weight_scale`. The fix replaces the substring check with `name.endswith(".scale")` to precisely match only parameters whose names end with `.scale`.

## Technical Significance
While this is a simple one-line fix, it prevents subtle weight loading bugs that could cause incorrect model behavior. The substring matching approach could incorrectly identify parameters as scale parameters, leading to incorrect renaming and weight mapping. This is particularly important for MTP models where correct weight loading is essential for maintaining accuracy. The fix demonstrates the importance of precise string matching when processing parameter names during model weight loading.

## Related
- `technique-mtp`
- `technique-weight-loading`
- `technique-deepseek`