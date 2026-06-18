---
id: technique-pr-vllm-ascend-233
title: "PR Insight: vllm-project/vllm-ascend #233"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ascendc
  - custom-kernels
  - rope
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/233"
---

# PR Insight: vllm-project/vllm-ascend #233

**Title:** [core] Support custom ascendc kernels in vllm-ascend

## Overview
This PR adds infrastructure for custom AscendC kernels in vllm-ascend, including CMakeLists, build system, and the first custom kernel: rotary_embedding (367 lines C++). The setup includes torch bindings, environment configuration, and comprehensive tests.

## Technical Significance
Foundation for high-performance custom kernels on Ascend. The build infrastructure enables compiling and loading AscendC operators from C++, bypassing PyTorch's generic implementations. The rotary_embedding kernel is the first proof-of-concept for this system.

## Related
- technique-rope
- technique-ascendc