---
id: lang-torch-npu-cpp-api
title: "torch_npu C++ API Reference — pybind11 Integration"
type: wiki-language
architectures: [ascend910, ascend910b]
tags: [torch-npu, cpp, pybind, operator, binding]
confidence: verified
languages: [cpp, python]
sources: [doc-torch-npu-get-current-npu-stream, doc-ascendc-pytorch-framework-adaptation, doc-torch-npu-npu-ffn, doc-torch-npu-adapter, code-multikernelbench-ascendc-direct-launch, code-vllm-ascend-csrc, code-catlass-python-extension]
related: [lang-ascendc-direct-launch-project, lang-pytorch-npu-guide, migration-pytorch-custom-op]
reproducibility: runnable
---

# torch_npu C++ API Reference — pybind11 Integration

The Python `torch_npu` guide covers `.npu()` and fused ops; this page documents the **C++ layer** needed to bind AscendC kernels via pybind11 — the most reliable path for MultiKernelBench `ascendc_direct_launch` submissions.

Official API reference: [c10_npu::getCurrentNPUStream](https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/apilist/ptaoplist_001029.html) (doc-torch-npu-get-current-npu-stream).

## Essential Headers

```cpp
#include <torch/extension.h>                          // at::Tensor, TORCH_CHECK, empty_like
#include <ATen/Operators.h>                           // ATen operator infrastructure
#include "torch_npu/csrc/core/npu/NPUStream.h"        // c10_npu::getCurrentNPUStream()
#include "torch_npu/csrc/core/npu/NPUFunctions.h"     // optional: device guards
#include "torch_npu/csrc/framework/OpCommand.h"       // optional: aclnn dispatch wrapper
```

| Header | Provides |
|--------|----------|
| `torch/extension.h` | `torch::Tensor`, `torch::empty_like`, pybind macros |
| `torch_npu/.../NPUStream.h` | `c10_npu::getCurrentNPUStream()` |
| `torch_npu/.../NPUFunctions.h` | NPU device index, sync helpers |
| `torch_npu/.../OpCommand.h` | Higher-level aclnn launch (used in vllm-ascend) |

Include paths (CMake):

```
${TORCH_NPU_PATH}/include
${TORCH_PATH}/include
${TORCH_PATH}/include/torch/csrc/api/include
```

## NPU Stream — Required for Kernel Launch

Every direct-launch kernel must enqueue on the **current NPU stream** matching PyTorch's execution context.

**Official signature** (doc-torch-npu-get-current-npu-stream):

```cpp
c10_npu::NPUStream c10_npu::getCurrentNPUStream(c10::DeviceIndex device_index = -1)
```

- Header: `torch_npu/csrc/core/npu/NPUStream.h`
- `device_index = -1` → current device (default)
- Analogous to `c10::cuda::getCurrentCUDAStream()`

```cpp
#include "torch_npu/csrc/core/npu/NPUStream.h"

torch::Tensor my_op(const torch::Tensor& x)
{
    const c10::OptionalDeviceGuard guard(x.device());
    auto y = torch::empty_like(x);
    void* stream = c10_npu::getCurrentNPUStream().stream(false);
    auto xPtr = reinterpret_cast<GM_ADDR>(x.data_ptr());
    auto yPtr = reinterpret_cast<GM_ADDR>(y.data_ptr());
    launch_my_kernel(xPtr, yPtr, stream);
    return y;
}
```

**Official CANN launch pattern** (doc-ascendc-pytorch-framework-adaptation):

```cpp
auto aclStream = c10_npu::getCurrentNPUStream().stream(false);
add_custom<<<numBlocks, nullptr, aclStream>>>(xPtr, yPtr, zPtr, totalLength);
```

**Semantics**:
- `.stream(false)` — return current aclrtStream directly (ptaoplist_000325)
- Input memory allocated in Python caller; binding allocates output only via `at::empty_like`
- Omitting stream binding causes silent correctness bugs (race with other ops)

## at::Tensor on NPU

```cpp
// Device check
TORCH_CHECK(x.device().type() == c10::DeviceType::PrivateUse1, "expected NPU tensor");
// Or after torch_npu import, PrivateUse1 == "npu"

// Data pointer — already on device
void* devicePtr = x.data_ptr();

// Shape / dtype
int64_t M = x.size(0);
auto dtype = x.scalar_type();  // torch::kFloat16, kBFloat16, kFloat32

// Allocate output
auto y = torch::empty_like(x);           // same device, dtype, shape
auto y = torch::empty({M, N}, x.options());  // explicit shape
```

**Allowed in binding layer**: `empty`, `empty_like`, `TORCH_CHECK`, `reinterpret_cast<GM_ADDR>`, device guard, stream fetch.

**Not allowed in ModelNew.forward()** (Python): any compute — see lang-mkb-integration-rules.

## pybind11 Module Template

```cpp
namespace my_ops {

torch::Tensor ffn(const torch::Tensor& x,
                  const torch::Tensor& w1,
                  const torch::Tensor& w2,
                  const std::string& activation)
{
    // Option A: call your AscendC direct launch
    // Option B: delegate to torch_npu fused op from C++
    const c10::OptionalDeviceGuard guard(x.device());
    // ...
}

} // namespace

PYBIND11_MODULE(benchmark_ops, m)
{
    m.doc() = "Custom AscendC ops";
    m.def("ffn", &my_ops::ffn, "Fused FFN",
          py::arg("x"), py::arg("w1"), py::arg("w2"), py::arg("activation"));
}
```

CMake must set:

```cmake
target_compile_definitions(pybind11_lib PRIVATE TORCH_EXTENSION_NAME=benchmark_ops)
```

Module name in Python import must match `PYBIND11_MODULE` first argument.

## Calling npu_ffn from C++ Binding Layer

`npu_ffn` is registered in **op-plugin** (doc-torch-npu-npu-ffn), not as a public stable C++ header API for third-party extensions. Practical options for MKB:

| Approach | How | Speedup potential |
|----------|-----|-------------------|
| **A. Custom AscendC kernel** | Implement fused GEMM+act+GEMM in kernel.cpp | Highest — beats aclnn if tuned |
| **B. OpCommand / internal dispatch** | Use `torch_npu/csrc/framework/OpCommand.h` to invoke registered op | ~1.0x — same as baseline |
| **C. Python in binding** | Avoid — MKB cheating detector scans Python only, not C++ | N/A |

For approach B, inspect op-plugin generated registration in installed torch_npu; the stable public surface is Python `torch_npu.npu_ffn(...)`. Official op-plugin signature:

```python
torch_npu.npu_ffn(x, weight1, weight2, activation, *, expert_tokens=None,
                  bias1=None, bias2=None, inner_precise=None, ...)
```

Supported activations (official): `fastgelu`, `gelu`, `relu`, `silu`, `geglu`, `swiglu`, `reglu`.

## TORCH_LIBRARY Alternative (Production Path)

For production extensions (vllm-ascend style), use `TORCH_LIBRARY` instead of raw pybind:

```cpp
#include <torch/library.h>

at::Tensor my_kernel_npu(const at::Tensor& x);

TORCH_LIBRARY(_C, m) {
  m.def("my_kernel(Tensor x) -> Tensor");
}
TORCH_LIBRARY_IMPL(_C, PrivateUse1, m) {
  m.impl("my_kernel", &my_kernel_npu);
}
```

MKB `ascendc_direct_launch` uses pybind11 (not `TORCH_LIBRARY`) because it `exec()`s `ModelNew.py` and imports the built `.so` directly.

## CMake Link Libraries

```cmake
target_link_libraries(pybind11_lib PRIVATE
  ${Python3_LIBRARIES}
  torch torch_cpu torch_npu
  ascendcl platform register tiling_api ascendc_runtime runtime profapi m dl
)
target_link_directories(pybind11_lib PRIVATE
  ${TORCH_PATH}/lib
  ${TORCH_NPU_PATH}/lib
  ${ASCEND_CANN_PACKAGE_PATH}/${SYSTEM_PREFIX}/lib64
  ${ASCEND_CANN_PACKAGE_PATH}/lib64
)
set_target_properties(pybind11_lib PROPERTIES
  BUILD_RPATH "${TORCH_PATH}/lib;${TORCH_NPU_PATH}/lib;..."
)
```

## dtype Dispatch Pattern

```cpp
#define DISPATCH_DTYPE(SCALAR_TYPE, NAME, ...)                          \
  [&]() {                                                               \
    switch (SCALAR_TYPE) {                                              \
      case torch::kFloat32: { using scalar_t = float; return __VA_ARGS__(); } \
      case torch::kFloat16: { using scalar_t = half; return __VA_ARGS__(); }  \
      case torch::kBFloat16: { using scalar_t = bfloat16; return __VA_ARGS__(); } \
      default: TORCH_CHECK(false, NAME " unsupported dtype");         \
    }                                                                   \
  }()

torch::Tensor op(const torch::Tensor& x) {
  return DISPATCH_DTYPE(x.scalar_type(), "op", [&] {
    launch_kernel<scalar_t>(/* ... */);
    return y;
  });
}
```

See **technique-ascendc-multi-dtype** for Cube/Vector behavior per dtype.

## Common Integration Pitfalls

| Symptom | Cause | Fix |
|---------|-------|-----|
| Segfault on first call | Wrong stream or null `data_ptr` | Use `getCurrentNPUStream().stream(false)` |
| Output all zeros | Kernel not launched on NPU stream | Add `OptionalDeviceGuard` |
| `PrivateUse1` vs `npu` confusion | Dispatch key naming | Both refer to NPU backend |
| Import error for extension | `sys.path` missing build dir | ModelNew.py inserts `kernel/build` |
| ABI mismatch | `_GLIBCXX_USE_CXX11_ABI` | Set `-D_GLIBCXX_USE_CXX11_ABI=1` to match torch build |

## Related Pages

- **lang-ascendc-direct-launch-project** — full project skeleton
- **lang-mkb-integration-rules** — what Python forward() may contain
- **lang-pytorch-npu-guide** — Python torch_npu surface
- **migration-pytorch-custom-op** — TORCH_LIBRARY production path
