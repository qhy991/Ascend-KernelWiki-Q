---
id: pattern-ascendc-compile-troubleshooting
title: "AscendC Compile Error Diagnostics — bisheng & CMake"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [ascendc, pitfalls, diagnosis, cmake, pattern]
confidence: verified
sources: [doc-ascendc-pytorch-framework-adaptation, doc-bisheng-compiler-quickstart, code-multikernelbench-ascendc-direct-launch, code-ascend-samples-operator-ascendc, blog-ascendc-performance-tips]
symptoms: ["bisheng compile failed", "kernel_operator.h not found", "namespace matmul ambiguous", "LocalTensor type mismatch", "cmake cannot find bisheng", "NZ alignment error", "link error undefined reference"]
techniques: [tiling-strategy, nz-tiling]
related: [lang-ascendc-direct-launch-project, pattern-nz-format-traps, pattern-ub-oom, lang-mkb-integration-rules]
---

# AscendC Compile Error Diagnostics — bisheng & CMake

A troubleshooting playbook distilled from repeated MultiKernelBench compile failures (11/11 in early rounds). Each entry maps a **bisheng/g++ error** to a **concrete fix**.

## Environment Setup Errors

### `bisheng compiler does not exist`

**Cause**: `ASCEND_CANN_PACKAGE_PATH` not set or CANN not installed.

**Fix**:
```bash
export ASCEND_HOME_PATH=~/Ascend/ascend-toolkit/latest
export ASCEND_CANN_PACKAGE_PATH=$ASCEND_HOME_PATH
# Verify:
ls $ASCEND_CANN_PACKAGE_PATH/bin/bisheng
```

CMake also checks `$ASCEND_CANN_PACKAGE_PATH/${SYSTEM_PREFIX}/ccec_compiler/bin/bisheng`.

### `cmake: ASCEND_CANN_PACKAGE_PATH not defined`

**Fix**: Pass explicitly:
```bash
cmake -S . -B build -DASCEND_CANN_PACKAGE_PATH=$ASCEND_HOME_PATH -DSOC_VERSION=Ascend910B2
```

## Header / Include Path Errors

### `fatal error: 'kernel_operator.h' file not found`

**Cause**: Missing CANN AscendC include paths.

**Fix**: Add to compile flags (auto-generated CMake includes these):
```
-I${ASCEND_CANN_PACKAGE_PATH}/compiler/ascendc/include/basic_api/interface
-I${ASCEND_CANN_PACKAGE_PATH}/compiler/ascendc/include/basic_api/impl
-I${ASCEND_CANN_PACKAGE_PATH}/compiler/ascendc/impl/aicore/basic_api
```

### `fatal error: 'platform/platform_ascendc.h' file not found`

**Fix**: Add highlevel API tiling path:
```
-I${ASCEND_CANN_PACKAGE_PATH}/compiler/ascendc/include/highlevel_api/tiling
```

### `fatal error: 'torch_npu/csrc/core/npu/NPUStream.h' file not found`

**Cause**: Binding compiled without torch_npu include.

**Fix**:
```bash
python3 -c "import torch_npu; print(torch_npu.__path__[0])"
# Add ${TORCH_NPU_PATH}/include
```

### `fatal error: 'matmul/matmul_intf.h' file not found`

**Fix**: Add `-I.../compiler/ascendc/include/highlevel_api/impl`

## Namespace & Name Collision

### `reference to 'matmul' is ambiguous` / `matmul is not a member of 'AscendC'`

**Cause**: `using namespace AscendC;` combined with `using namespace matmul;` or Catlass `Matmul` type.

**Fix** (pick one):
```cpp
// Option A: fully qualify
AscendC::Matmul<...> mm;
matmul::MatmulType mmType;

// Option B: selective using
using namespace AscendC;
namespace matmulImpl = matmul;  // alias

// Option C: never use bare `using namespace` in kernel files with Matmul
```

### `error: expected unqualified-id before '__global__'`

**Cause**: `__global__ __aicore__` function placed inside a class body incorrectly, or missing includes.

**Fix**: Kernel entry must be at namespace scope or use class method with `__aicore__` attribute correctly per AscendC style.

## Type Mismatch Errors

### `no matching function for call to 'DeQue<half>'` / LocalTensor mismatch

**Cause**: `AllocTensor<T>()` and `DeQue<U>()` with `T != U`.

**Fix**: Use consistent dtype throughout queue lifecycle:
```cpp
auto xLocal = inQueue.AllocTensor<half>();
inQueue.EnQue(xLocal);
xLocal = inQueue.DeQue<half>();  // same T
```

### `cannot convert 'LocalTensor<half>' to 'LocalTensor<float>'`

**Cause**: Mixed precision without explicit cast.

**Fix**: Use separate buffers per dtype or explicit `Cast` API.

## bisheng-Specific Semantic Errors

### `error: GM_ADDR was not declared`

**Fix**:
```cpp
#ifndef GM_ADDR
#define GM_ADDR void*
#endif
```

Or `#include "kernel_operator.h"` which defines it.

### `error: GetBlockIdx is not a member of global namespace`

**Fix**: Use `AscendC::GetBlockIdx()` after including `kernel_operator.h`.

### `unsupported NPU architecture` / `Cannot find option named 'Ascend910B4-1'`

**Cause**: bisheng/bishengir target string not in supported list (common with Triton-Ascend on sub-version chips).

**Fix**:
- Use `-DSOC_VERSION=Ascend910B2` for 910B MKB eval
- bisheng kernel compile: `--npu-arch=dav-2201` (910B)
- Avoid non-standard suffixes like `910B4-1` in `--target` (see sglang issue #16360)

## NZ Format / Alignment Errors

### Cube matmul runtime error or garbage output (no compile error)

**Cause**: M/N/K not multiples of 16 for Cube path.

**Fix**: Pad dimensions before GEMM; see **pattern-nz-format-traps**.

### `error: DataCopy size not aligned`

**Fix**: Ensure copy length is 32-byte aligned for some paths; use `DataCopyPad` for tail tiles.

## CMake / Link Errors

### `undefined reference to 'launch_my_kernel_half'`

**Cause**: Launch wrapper in kernel `.o` but not `extern "C"`, or missing from link.

**Fix**:
```cpp
extern "C" void launch_my_kernel_half(/* ... */) { /* ... */ }
```

Ensure file is in `kernel_sources` (bisheng-compiled), not only in binding.

### `undefined reference to 'torch_npu::...'`

**Fix**: Link `torch_npu` and set RPATH to `${TORCH_NPU_PATH}/lib`.

### `version 'GLIBCXX_3.4.30' not found`

**Cause**: ABI mismatch between extension and libtorch.

**Fix**: Match `_GLIBCXX_USE_CXX11_ABI=1` and compile with same GCC as PyTorch build.

## kernel.cpp Boilerplate — Minimum Required

Every device `.cpp` in `kernel_sources` should start with:

```cpp
#include "kernel_operator.h"
// Optional for tiling:
#include "platform/platform_ascendc.h"
// Optional for Matmul:
#include "matmul/matmul_intf.h"

#ifndef GM_ADDR
#define GM_ADDR void*
#endif

// Kernels: __global__ __aicore__ void ...
// Launch:  extern "C" void launch_...(GM_ADDR ..., void* stream) {
//              kernel<<<blockDim, nullptr, stream>>>(...);
//          }
```

## Diagnostic Workflow

```
1. Can bisheng be found?          → ASCEND_HOME_PATH
2. kernel_operator.h found?       → CANN include paths
3. bisheng -xasc compiles?        → fix device code errors
4. g++ binding compiles?          → torch/torch_npu/pybind includes
5. Link succeeds?                 → extern "C", library paths
6. Runtime correctness?           → stream, dtype, NZ alignment
```

## Session Failure Patterns (Frequency Ranked)

| Rank | Error class | Round impact |
|------|-------------|--------------|
| 1 | Missing include paths / no CMake template | Blocks all builds |
| 2 | kernel/binding source split wrong | bisheng tries to compile pybind |
| 3 | Namespace matmul collision | Device compile fail |
| 4 | No extern "C" launch wrapper | Link fail |
| 5 | Missing NPUStream in binding | Runtime crash |
| 6 | NZ alignment | Correctness fail (post-compile) |

## Related Pages

- **lang-ascendc-direct-launch-project** — working CMake template
- **pattern-nz-format-traps** — alignment issues
- **pattern-ub-oom** — runtime UB overflow (not compile, but common next failure)
- **lang-mkb-integration-rules** — post-compile cheating detection
