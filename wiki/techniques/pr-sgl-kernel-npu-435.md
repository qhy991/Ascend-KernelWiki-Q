---
id: technique-pr-sgl-kernel-npu-435
title: "PR Insight: sgl-project/sgl-kernel-npu #435"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - long-sequences
  - a3
  - memory-scaling
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/435"
---

# PR Insight: sgl-project/sgl-kernel-npu #435

**Title:** The A3 normal operator is modified to support a maximum of 128K long sequences.

## Overview
This PR modifies the A3 DeepEP normal operator to support maximum sequence lengths of 128K tokens. The changes update the combine and dispatch tiling logic to handle the extended sequence length requirements, enabling very long context processing on A3 hardware.

## Technical Significance
Supporting 128K sequences enables DeepEP to handle extremely long context scenarios required by modern large language models. This extension is critical for applications that need to process very long documents or maintain extensive conversation contexts on A3 hardware.

## Related
- `kernel-deepep-normal`, `kernel-deepep-dispatch`, `kernel-deepep-combine`, `technique-long-sequence-optimization`