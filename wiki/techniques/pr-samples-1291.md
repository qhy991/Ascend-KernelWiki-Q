---
id: technique-pr-samples-1291
title: "PR Insight: Ascend/samples #1291"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - build
  - output
  - samples
  - shell
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1291"
---

# PR Insight: Ascend/samples #1291

**Title:** mkdir out/output

## Overview
This PR adds a command to create the out/output directory. The directory is likely needed for storing sample output files or build artifacts.

## Technical Significance
Proper directory structure is important for build systems and runtime operation. Creating output directories ensures samples run correctly and have a place to store results.

## Related
- `pattern-build-system`
- `pattern-file-structure`