---
id: technique-pr-pto-vs-triton
title: "PR Insight: Custom PTO vs Triton Backend"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - triton
  - performance
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/517"
---

# PR Insight: Custom PTO vs Triton Backend

**Source:** [sgl-kernel-npu PR #517](https://github.com/sgl-project/sgl-kernel-npu/pull/517)

A major debate in modern AI compilation is whether to use the Triton compiler (which is increasingly supporting the Ascend backend) or hand-write native C++ AscendC operators (PTO - PyTorch Operator backend). This PR provides concrete benchmarking data regarding the `MEGA-GDN` attention operator.

## The Benchmark Result
The PR introduced a native AscendC `pto` implementation of the GDN (Gated Data-Dependent Normalization) Attention mechanism and set it as the default, overriding the previous Triton backend (which is now hidden behind the `GDN_ATTN_BACKEND_TRITON=1` environment variable).

**Result**: Depending on the input size, the native `pto` kernel is **50% to 300% faster** than the Triton-generated backend, with the most significant gains observed at smaller context lengths (Amdahl's Law effect).

## Why is AscendC Faster?

### 1. Dynamic Head Support
The PR made the number of Key heads fully dynamic and compiled a single binary supporting multiple Value head counts (16, 24, 32, 48, 64). 
- **Triton Issue**: Triton often struggles to generate optimal loops and memory layouts when tensor shapes are completely dynamic at runtime, often falling back to conservative, un-unrolled loops.
- **AscendC Advantage**: Native C++ allows developers to use `DataCopyExtParams` and explicit vector loop unrolling, handling dynamic bounds efficiently via the Scalar unit.

### 2. Dispatch Overhead
At smaller context lengths, the kernel execution time is very short. The Triton JIT (or even AOT) wrapper in Python introduces microsecond-level dispatch overheads. The `pto` backend simplifies the CMake and launch logic, pushing input assertions and dispatch directly into native C++, keeping the NPU fed.
