---
id: technique-pr-samples-2025
title: "PR Insight: Ascend/samples #2025"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - samples
  - custom-op
  - runtime
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2025"
---

# PR Insight: Ascend/samples #2025

**Title:** cpp_extension里新增load_libray方式调用自定义API

## Overview
This PR adds load_library functionality to the cpp_extension for calling custom APIs. The enhancement enables dynamic loading of custom AscendC operators through C++ extension mechanisms.

## Technical Significance
Dynamic operator loading is critical for inference frameworks and production environments where custom kernels need to be registered at runtime without rebuilding the entire application. This sample demonstrates the proper API usage for registering and invoking custom AscendC operators dynamically.

## Related
- `technique-ascendc`