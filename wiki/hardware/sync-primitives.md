---
id: hw-sync-primitives
title: "Hardware Synchronization Primitives"
type: wiki-hardware
architectures:
  - ascend910b
tags:
  - hardware-overview
confidence: inferred
sources: []
---

# Hardware Synchronization Primitives

Ascend AI Cores employ a decoupled, multi-queue pipeline architecture. Because the Matrix (Cube), Vector, and Memory Transfer Engines (MTE) operate asynchronously, explicit hardware synchronization is required to ensure data dependencies are respected.

## TPipe and TQue (Software Abstraction)

In AscendC, synchronization is primarily abstracted through `TPipe` and `TQue`. When you allocate memory from a `TQue` (e.g., `EnQue` and `DeQue`), the compiler automatically inserts the underlying hardware synchronization instructions.

```cpp
// Example: MTE to Vector Sync
TQue<QuePosition::VECIN, 2> inQueue;
// ... MTE loads data ...
inQueue.EnQue(tensor); // MTE signals Vector
// ... Vector unit waits ...
auto work_tensor = inQueue.DeQue<half>(); // Vector waits for MTE signal
```

## Hardware Level: Flags and Events

Underneath the `TQue` abstraction, the Da Vinci architecture uses a system of Hardware Flags (also called Semaphores or Events).

1. **SetFlag**: An execution unit (e.g., MTE) completes a memory transfer and executes a `SetFlag` instruction to flip a specific hardware bit.
2. **WaitFlag**: The dependent unit (e.g., Vector) executes a `WaitFlag` instruction. If the flag is not set, the Vector pipeline stalls. Once set, it clears the flag and continues execution.

### The 4-Queue Pipeline Sync
A standard `CopyIn -> Compute -> CopyOut` pipeline uses a circular token system:
- MTE1/2 waits for a "Buffer Empty" flag from Cube/Vector.
- MTE1/2 writes data, then sets a "Buffer Full" flag.
- Cube/Vector waits for "Buffer Full", processes data, then sets "Buffer Empty".

### Barrier Instructions
For Intra-Core synchronization across different threads or blocks within the same AI Core (if applicable), `__syncthreads()` equivalents exist, usually translating to a system-level pipeline flush or global barrier instruction (`PipeBarrier`).
- `PipeBarrier<PIPE_ALL>()`: Blocks all instruction queues until previous instructions complete. Heavyweight, use sparingly.
- `PipeBarrier<PIPE_V>()`: Blocks only the Vector queue.
