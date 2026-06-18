---
id: technique-pr-mindspeed-2542
title: "PR Insight: Ascend/MindSpeed #2542"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - ema
  - test
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2542"
---

# PR Insight: Ascend/MindSpeed #2542

**Title:** fix test_ema_api.py error

## Overview
This PR fixes errors in the EMA (Exponential Moving Average) API test file (test_ema_api.py). The changes ensure that EMA functionality tests pass correctly and validate the expected behavior.

## Technical Significance
Test suite reliability is essential for maintaining code quality. Fixing test errors ensures that EMA functionality is properly validated and prevents false positives in CI/CD pipelines.

## Related