---
id: technique-pr-sgl-kernel-npu-515
title: "PR Insight: sgl-project/sgl-kernel-npu #515"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - deepep
  - tiling
  - kernel-scheduling
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/515"
---

# PR Insight: sgl-project/sgl-kernel-npu #515

**Title:** DeepEP: expand moe specifications

## Overview
This PR significantly expands the MoE specifications supported by the intranode dispatch and combine operations on Atlas A3 hardware. The changes enable support for up to 1024 experts, top-k up to 16, and hidden sizes up to 8192, while also adapting for long-sequence scenarios. The implementation modifies kernel tiling configurations and operator host code to handle these expanded MoE configurations.

## Technical Significance
Expanding MoE support to larger expert counts and hidden sizes enables the deployment of more powerful and capable MoE models on Ascend hardware. This enhancement is crucial for modern large language models that use MoE architectures with hundreds or thousands of experts. The tiling optimizations ensure efficient memory access and computation patterns for these larger configurations, while the long-sequence adaptation improves performance for extended context lengths.

## Related
- `technique-moe-dispatch`
- `technique-tiling`
- `pattern-expert-parallelism`
- `kernel-moe`