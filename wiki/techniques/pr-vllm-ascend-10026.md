---
id: technique-pr-vllm-ascend-10026
title: "PR Insight: vllm-project/vllm-ascend #10026"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - dsv4-flash
  - dsa-cp
  - ascend-a5
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10026"
---

# PR Insight: vllm-project/vllm-ascend #10026

**Title:** [BugFix][dsv4-flash] add dsa-cp support for a5

## Overview
This PR adds dsa-cp (distributed self-attention context parallel) support for Ascend A5 devices in the dsv4-flash implementation, enabling context parallelism for flash attention on A5.

## Technical Significance
Enables distributed self-attention context parallelism on Ascend A5 devices for dsv4-flash, improving scalability for long-context inference on A5 hardware. Extends context parallel capabilities to support A5 devices.

## Related
- `technique-context-parallel`, `kernel-flash-attention`, `technique-dsa-cp`