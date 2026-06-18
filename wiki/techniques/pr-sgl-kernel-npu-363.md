---
id: technique-pr-sgl-kernel-npu-363
title: "PR Insight: sgl-project/sgl-kernel-npu #363"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - build-system
  - packaging
  - chip-model
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/363"
---

# PR Insight: sgl-project/sgl-kernel-npu #363

**Title:** Revert " Build the deepep package with the chip model included."

## Overview
This PR reverts a previous change that included chip model information in the DeepEP package build process. The rollback removes chip-model-specific modifications from the setup.py file, returning to a chip-agnostic packaging approach.

## Technical Significance
Reverting chip-model inclusion in the package build ensures broader compatibility and reduces maintenance overhead for supporting multiple Ascend chip variants. A chip-agnostic approach allows the same package to work across different hardware without requiring rebuilds for each target platform.

## Related
- `technique-build-optimization`, `technique-packaging`