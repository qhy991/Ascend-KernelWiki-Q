---
id: technique-pr-samples-543
title: "PR Insight: Ascend/samples #543"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - atlasutil
  - c++
  - python
  - arm
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/543"
---

# PR Insight: Ascend/samples #543

**Title:** 修改c++和python公共库，不仅仅支持Atlas200DK和Atlas300

## Overview
This PR modifies the C++ and Python common utility libraries (atlasutil) to support more Ascend hardware platforms beyond Atlas200DK and Atlas300, expanding the library's compatibility across the Ascend product line.

## Technical Significance
Increases the utility library's platform coverage, enabling developers to use common abstractions across more Ascend hardware variants. This reduces platform-specific code and improves code portability.

## Related
- `pattern-library-maintenance`
- `pattern-cross-platform`