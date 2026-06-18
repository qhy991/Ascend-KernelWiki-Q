---
id: technique-pr-samples-1664
title: "PR Insight: Ascend/samples #1664"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - g-select-one-thread
  - threading
  - configuration
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1664"
---

# PR Insight: Ascend/samples #1664

**Title:** 【轻量级 PR】：修改g_select_one_thread默认值为1

## Overview
This PR changes the default value of g_select_one_thread to 1, modifying thread selection behavior in sample applications.

## Technical Significance
The g_select_one_thread configuration affects how samples handle multi-threading for inference. Setting the default to 1 suggests single-threaded operation as the safe default, which is important for stability and resource management in sample code that may run on various hardware configurations.

## Related
- technique-threading