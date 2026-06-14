---
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
