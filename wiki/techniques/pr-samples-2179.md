---
id: technique-pr-samples-2179
title: "PR Insight: Ascend/samples #2179"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - build
  - cmake
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2179"
---

# PR Insight: Ascend/samples #2179

**Title:** CMakeLists.统一使用python3 替换python

## Overview
This PR updates CMakeLists.txt files to use python3 instead of python, ensuring compatibility with systems where python refers to Python 2.

## Technical Significance
Python 3 compatibility is essential for modern development workflows. This change ensures build scripts work correctly on systems with Python 3 as the default python3 command.

## Related