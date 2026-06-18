---
id: technique-pr-sgl-kernel-npu-533
title: "PR Insight: sgl-project/sgl-kernel-npu #533"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - mte
  - kernel-scheduling
  - dynamic-shape
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/533"
---

# PR Insight: sgl-project/sgl-kernel-npu #533

**Title:** feat: PTO chunk gdn support H=12, 8

## Overview
This PR extends the PTO mega-chunk GDN attention kernel to support smaller head configurations (H=12, 8) by adding a separate transpose path for H<16. The implementation enables support for additional head count configurations across different tensor parallelism settings, with proper handling of (value_heads, key_heads) combinations for global H values of 16, 32, 48, and 64.

## Technical Significance
Supporting smaller head counts expands the applicability of the optimized GDN attention kernel to a wider range of model architectures. The separate transpose path addresses MTE (Memory Transfer Engine) alignment and padding issues that occur with smaller configurations. This enhancement ensures efficient attention computation for models with fewer heads, which is common in certain architecture designs or tensor parallelism configurations.

## Related
- `kernel-attention`
- `kernel-gdn`
- `technique-mte-optimization`
- `pattern-dynamic-shape`