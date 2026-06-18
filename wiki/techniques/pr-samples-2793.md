---
id: technique-pr-samples-2793
title: "PR Insight: Ascend/samples #2793"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2793"
---

# PR Insight: Ascend/samples #2793

**Title:** 修改 test_perf.py 适配numpy2.×

## Overview
This PR modifies test_perf.py to adapt to NumPy 2.x API changes. The update ensures performance testing scripts work correctly with the latest NumPy version.

## Technical Significance
NumPy 2.x introduced API changes that broke compatibility with older code. Adapting performance test scripts ensures samples can be evaluated with current Python scientific computing environments.

## Related
- Python API compatibility patterns