---
id: technique-pr-samples-988
title: "PR Insight: Ascend/samples #988"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - bugfix
  - file-path
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/988"
---

# PR Insight: Ascend/samples #988

**Title:** modify link of record_file

## Overview
Fixes an incorrect link or path to a record_file in the samples codebase, likely causing file access errors during execution.

## Technical Significance
Correct file paths are essential for inference workflows that need to read input data or write results. This fix prevents runtime errors related to file I/O.

## Related
- `technique-inference-optimization`
