---
id: tool-camodel-simulator
title: "Ascend Simulator (Camodel)"
type: wiki-tool
tags:
  - simulator
confidence: inferred
sources: []
---

# Ascend Simulator (Camodel)

Camodel is the CPU-based simulator for AscendC kernel development. It allows developers to test, verify, and debug kernels without physical NPU access.

## Capabilities

- **Functional Verification**: Runs AscendC code natively on the CPU to check for logical correctness.
- **Memory Violation Detection**: Can catch out-of-bounds accesses to the Unified Buffer (UB) or Global Memory (GM).
- **Printf Debugging**: Supports standard `printf` within device code for easy variable inspection (not recommended for actual NPU hardware).

## Running in Simulator Mode

To compile and run a kernel for Camodel, use the `ascendc_api` with the CPU flag. The underlying code is compiled using standard GCC/Clang with simulation macros enabled.

```bash
# Compile for CPU execution
g++ -O0 -g -I/usr/local/Ascend/ascend-toolkit/latest/include -D__CCE_KT_TEST__ my_kernel.cpp -o sim_run

# Execute
./sim_run
```

## Debugging

You can attach `gdb` to the `sim_run` executable just like any standard C++ program. This enables stepping through the `Init`, `Process`, and TPipe queue operations line-by-line, which is invaluable for understanding complex pipeline schedules and data flows.
