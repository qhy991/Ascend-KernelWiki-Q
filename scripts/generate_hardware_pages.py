import os

wiki_hardware_path = "/Users/haiyan-mini/Agent4Kernel/ascend-kernelwiki-q/wiki/hardware"

mte_content = """---
id: hw-mte
title: "MTE (Memory Transfer Engine) in Ascend AICore"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [mte, unified-buffer, pipeline-scheduling]
confidence: verified
sources: [doc-ascendc-api-reference]
cuda_equivalent: tma
---

# Memory Transfer Engine (MTE)

The Memory Transfer Engine (MTE) is a critical hardware component in the Ascend AICore. It acts as an asynchronous DMA (Direct Memory Access) engine responsible for moving data between the different layers of the memory hierarchy without stalling the compute units (Cube and Vector).

## MTE Sub-Engines

To allow simultaneous inbound and outbound data movements, the MTE is divided into specific channels:

- **MTE1 (L1 to L0A/L0B)**: Responsible for feeding the Cube Unit. It moves matrix tiles from the L1 Buffer into the L0A and L0B registers (the immediate operands for the Cube).
- **MTE2 (GM to UB/L1)**: Responsible for inbound transfers. It moves data from off-chip Global Memory (GM) into the on-chip Unified Buffer (UB) or L1 Buffer. `DataCopy` operations moving data *in* utilize MTE2.
- **MTE3 (UB/L1/L0C to GM)**: Responsible for outbound transfers. It moves computed results from the Unified Buffer, L1, or the Cube's output register (L0C) back to Global Memory. `DataCopy` operations moving data *out* utilize MTE3.

## Asynchronous Execution & Pipeline Overlap

The MTE runs completely independently of the Vector and Cube compute units. When an Ascend C kernel calls `DataCopy`, it dispatches an instruction to the MTE queue. The execution then immediately proceeds to the next instruction in the scalar pipeline.

This separation is what enables **Pipeline Scheduling (CopyIn -> Compute -> CopyOut)**:
- MTE2 can be busy loading Tile `N+1` into UB.
- Vector Unit can be computing Tile `N` in UB.
- MTE3 can be busy storing Tile `N-1` from UB to GM.

To synchronize these independent engines, the hardware uses **Event Synchronization** (the `EnQue` and `DeQue` barrier signals).

## Performance Characteristics

- MTE performs best with **contiguous, 32-byte aligned** memory accesses. Unaligned or scattered memory accesses will severely degrade GM bandwidth utilization.
- MTE incorporates on-the-fly data format conversion (e.g., from ND to NZ format) during the transfer, though this adds some latency overhead compared to a straight copy.
"""

scalar_unit_content = """---
id: hw-scalar-unit
title: "Scalar Unit in Ascend AICore"
type: wiki-hardware
architectures: [ascend910, ascend910b]
tags: [scalar-unit]
confidence: verified
sources: [doc-ascendc-api-reference]
---

# Scalar Unit

The Scalar Unit in the Ascend AICore acts as the primary control processor for the core. While the Cube and Vector units perform the heavy lifting of mathematical computations on tensors, the Scalar Unit acts as the "conductor", orchestrating the flow of the program.

## Core Responsibilities

1. **Address Calculation**: The Scalar Unit computes the pointers and offsets required for memory access. When you calculate memory strides or tile offsets in Ascend C, these integer calculations run on the Scalar Unit.
2. **Control Flow**: `if/else` branching, `for/while` loops, and function calls are managed by the Scalar Unit.
3. **Instruction Dispatching**: The Scalar Unit reads the instruction stream and pushes instructions to the respective queues (Vector Queue, Cube Queue, MTE Queues) for asynchronous execution.
4. **Parameter Parsing**: When a kernel is launched, the Scalar Unit is responsible for reading the kernel arguments passed from the Host.

## Execution Model

The Scalar Unit executes instructions sequentially. However, when it encounters an instruction meant for another unit (e.g., a `Matmul` instruction for the Cube Unit, or a `DataCopy` for MTE), it places the instruction in that unit's hardware queue and immediately proceeds to the next instruction.

This means the Scalar Unit can run far ahead of the actual computation. 

## Optimization Considerations

### Scalar-Vector Synchronization Overhead
Because the Scalar Unit runs ahead, reading a computed value from a Vector register back into a Scalar register forces the Scalar Unit to stop and wait for the Vector queue to drain (a synchronization barrier). 

**Avoid data-dependent control flow where possible.** For example, using a vector computation result to determine the number of loop iterations will force a stall. Instead of `if (vector_val > 0)`, use Vector-native selection instructions (like `Select` or masks).

### Register Pressure
The Scalar Unit has its own dedicated register file. Complex addressing logic or excessive loop unrolling can exhaust scalar registers.
"""

data_formats_content = """---
id: hw-data-formats
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
"""

os.makedirs(wiki_hardware_path, exist_ok=True)

with open(os.path.join(wiki_hardware_path, "mte.md"), "w") as f:
    f.write(mte_content)

with open(os.path.join(wiki_hardware_path, "scalar-unit.md"), "w") as f:
    f.write(scalar_unit_content)

with open(os.path.join(wiki_hardware_path, "data-formats.md"), "w") as f:
    f.write(data_formats_content)

print("Ascend hardware generation script complete.")
