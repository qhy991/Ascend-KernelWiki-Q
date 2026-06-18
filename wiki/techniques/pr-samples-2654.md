---
id: technique-pr-samples-2654
title: "PR Insight: Ascend/samples #2654"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - torch
  - compatibility
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2654"
---

# PR Insight: Ascend/samples #2654

**Title:** fix error in torch 2.1

## Overview
This PR fixes compatibility errors when running samples with PyTorch 2.1. The changes address API changes or breaking issues introduced in the newer PyTorch version, ensuring samples work correctly with torch-npu.

## Technical Significance
Maintaining compatibility with PyTorch versions is critical for developers using the torch-npu backend. Proper sample code helps users understand how to adapt their applications for different PyTorch versions on Ascend hardware.

## Related
- `technique-operator-fusion`
- `kernel-attention-ascendc`