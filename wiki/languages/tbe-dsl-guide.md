---
id: lang-tbe-dsl-guide
title: "TBE-DSL — High-Level Operator Development (Deprecated)"
type: wiki-language
tags: [tbe-dsl, deprecated, python, operator]
confidence: source-reported
sources: [doc-cann-architecture-guide]
architectures: [ascend910]
languages: [tbe-dsl, python]
related: [lang-ascendc-guide]
---

## Overview

TBE-DSL (Tensor Boost Engine DSL) was Huawei's Python-based operator development framework for Ascend NPUs, introduced in CANN 5.0 and based on TVM (Tensor Virtual Machine). It provided a high-level abstraction for defining custom operators using Python decorators and a DSL that compiled down to Ascend-specific binaries.

**Status**: TBE-DSL is **deprecated** and has been superseded by AscendC starting from CANN 7.0. New operator development should use AscendC instead.

## Two Programming Modes

### 1. TBE DSL Mode (High-Level)
- Uses Python decorators (`@fusion_manager.register`)
- Declarative specification of compute schedule
- Automatic optimization and code generation
- Best for simple operators from standard mathematical operations

```python
@fusion_manager.register("custom_add")
def custom_add(x, y, output_z):
    return x + y

# Compiler automatically generates memory management and scheduling
```

### 2. TIK Mode (Low-Level)
- Imperative Python API (Tensor Interface Kernel)
- Explicit buffer management and instruction scheduling
- Closer to hardware architecture
- Required for complex operators with custom memory patterns

```python
# TIK example with explicit buffer allocation
tik_instance = Tik()
src = tik_instance.Tensor("float16", (128,), name="src", scope=tik.scope_gm)
dst = tik_instance.Tensor("float16", (128,), name="dst", scope=tik.scope_gm)
ub_buffer = tik_instance.Tensor("float16", (128,), name="ub_buf", scope=tik.scope_ub)
tik_instance.data_copy(ub_buffer, src)
tik_instance.vec_add(ub_buffer, ub_buffer, ub_buffer, 128, 0, 0, 0)
tik_instance.data_copy(dst, ub_buffer)
```

## Architecture and Execution Model

- **Compute Engine**: TVM-based compilation to Ascend AI Core instructions
- **Memory Model**: Abstracted GM (Global Memory) and UB (Unified Buffer)
- **Scheduling**: Automatic (DSL mode) or manual (TIK mode) instruction scheduling
- **Fusion Support**: Automatic operator fusion via decorator-based framework

## Limitations (Why AscendC Replaced TBE)

1. **Abstraction Overhead**: Python-based DSL introduced compilation latency
2. **Performance Ceiling**: Automatic optimization couldn't match hand-tuned AscendC kernels
3. **Hardware Evolution**: New Ascend910B features required more explicit control
4. **Toolchain Complexity**: TVM dependency made build system fragile
5. **Debugging Difficulty**: Python-to-instruction compilation obscured performance issues

## Migration Recommendation

**All new operator development should use AscendC** instead of TBE-DSL. Existing TBE operators should be migrated to AscendC for:

- Better performance (15-30% typical improvement)
- Hardware feature support (e.g., Ascend910B Cube units)
- Improved debugging (C++ is closer to metal)
- Future toolchain support (TBE will not receive updates)

See [migration-cuda-to-ascendc](/Users/haiyan/Documents/Infinity/Agent4Kernel/Ascend-KernelWiki-Q/wiki/migration/cuda-to-ascendc.md) for guidance on direct AscendC development. For TBE → AscendC migration, refactor TIK code to AscendC class-based model (similar semantic mapping, different syntax).

## Historical Context

TBE-DSL was introduced as a rapid prototyping framework when Ascend NPU ecosystem was nascent. The Python-based approach aimed to accelerate operator development by abstracting hardware complexity. However, as workloads became performance-critical and hardware evolved (Ascend910B with enhanced Cube units, improved memory hierarchy), the abstraction became a bottleneck. AscendC was designed from the ground up to provide explicit control while maintaining productivity through C++ templates and structured APIs.
