---
id: wiki-hardware-data-formats
title: "Data Formats: ND vs FRACTAL_NZ"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [nd-format, nz-format, format-conversion, cube-unit]
confidence: verified
sources: [doc-ascendc-api-reference]
---

# Data Formats: ND vs FRACTAL_NZ

Ascend NPUs utilize specific memory layouts to feed the high-throughput Cube Unit efficiently. Understanding the distinction between standard formats and Ascend's internal formats is crucial for optimization.

## 1. ND Format (N-Dimensional)

ND format refers to the standard, continuous memory layout commonly used by frameworks like PyTorch or NumPy (typically row-major, e.g., NCHW or NHWC).

- **Usage**: Data in Global Memory (GM) is almost always stored in ND format.
- **Hardware Unit**: The **Vector Unit** and **Scalar Unit** operate naturally on ND format.

## 2. FRACTAL_NZ (NZ Format)

FRACTAL_NZ (often just called NZ format) is a specialized 5-dimensional tiled layout specifically required by the **Cube Unit**. 

To maximize the utilization of the Cube's MAC (Multiply-Accumulate) arrays, the matrix must be partitioned into 16x16 blocks (for FP16). The internal memory layout is rearranged so that these 16x16 sub-matrices (fractals) are stored contiguously in memory.

### The Layout Structure
A 2D matrix of size `[M, N]` is transformed into a 4D layout of shape `[N1, M1, M0, N0]`, where:
- `M0 = 16`, `N0 = 16` (the inner fractal block)
- `M1 = ceil(M / 16)`
- `N1 = ceil(N / 16)`

## Format Conversion (`DataCopy`)

Because Global Memory holds ND data but the Cube Unit requires NZ data, a conversion must occur. 

In Ascend C, this conversion is often handled implicitly by the Memory Transfer Engine (MTE) during the `DataCopy` from Global Memory to Unified Buffer/L1.

```cpp
// Moving data from GM (ND) to UB (NZ)
DataCopy(ub_nz_tensor, gm_nd_tensor, {M, N}); 
```

### Overhead and Optimization

- **Conversion Cost**: While hardware-accelerated, converting ND to NZ on-the-fly during MTE transfers is slower than a straight memory copy. It reduces the effective memory bandwidth.
- **Alignment Penalty**: If the dimensions `M` or `N` are not multiples of 16, the MTE must pad the data with zeros. This padding wastes UB space and transfer cycles.
- **Optimization Strategy (Data Reuse)**: If a matrix will be used multiple times in a computation (e.g., weights in an LLM), convert it to NZ format once and store the NZ version in Global Memory, or keep it in L1 cache if it fits.
