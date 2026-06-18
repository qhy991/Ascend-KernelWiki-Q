---
id: technique-pr-samples-878
title: "PR Insight: Ascend/samples #878"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - custom-op
  - build-fix
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/878"
---

# PR Insight: Ascend/samples #878

**Title:** modify the default path to make custom op compile success

## Overview
This PR fixes build issues in custom operator samples by correcting default path configurations, ensuring that the compilation process can locate required headers, libraries, and build artifacts.

## Technical Significance
Improves developer experience by fixing build configuration issues, reducing the friction of setting up and compiling custom operators in local development environments.

## Related
- `technique-operator-fusion`