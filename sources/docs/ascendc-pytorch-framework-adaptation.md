---
id: doc-ascendc-pytorch-framework-adaptation
title: "AscendC PyTorch Framework Adaptation — torch.library & Pybind"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [ascendc, torch-npu, pytorch, pybind, cpp, operator]
date: '2026-06-19'
url: https://www.hiascend.com/document/detail/zh/canncommercial/900/programug/Ascendcopdevg/atlas_ascendc_10_0057.html
hardware_features: [cube-unit, vector-unit]
techniques: [pipeline-scheduling]
languages: [ascendc, cpp, python]
confidence: verified
---

# AscendC PyTorch Framework Adaptation

Official CANN 9.0 programming guide appendix: integrating custom AscendC kernels into PyTorch via **Kernel直调** (direct launch).

## Source

- CANN Commercial 9.0.0 — Ascend C Programming Guide → Appendix → AI Framework Operator Adaptation → PyTorch Framework
- URL: https://www.hiascend.com/document/detail/zh/canncommercial/900/programug/Ascendcopdevg/atlas_ascendc_10_0057.html

## Integration Paths

| Path | Mechanism | torch.compile | Use when |
|------|-----------|---------------|----------|
| Kernel直调 + torch.library | `TORCH_LIBRARY` + `TORCH_LIBRARY_IMPL(..., PrivateUse1, ...)` | Supported | Production; graph tracing needed |
| Kernel直调 + Pybind | `PYBIND11_MODULE` | **Not supported** | Quick binding; MKB-style eval |
| OpPlugin | op_plugin adapter | Via dispatcher | Standard fused ops |
| TorchAir graph | Custom op入图 | Graph mode | Inference compilation |

Official guidance: **Pybind** is for fast C++→Python binding but lacks schema/graph tracing; **torch.library** is required for `torch.compile`.

## Environment Dependencies

- CANN toolkit installed
- PyTorch
- torch_npu plugin
- Pybind path additionally requires: `pip3 install pybind11 expecttest`

## Host Binding Pattern (Official Add Example)

Required headers:

```cpp
#include <pybind11/pybind11.h>
#include <torch/extension.h>
#include "torch_npu/csrc/core/npu/NPUStream.h"
#include "kernel_operator.h"
```

Host function:

```cpp
namespace ascendc_ops {
at::Tensor ascendc_add(const at::Tensor& x, const at::Tensor& y)
{
    auto aclStream = c10_npu::getCurrentNPUStream().stream(false);
    at::Tensor z = at::empty_like(x);
    uint32_t numBlocks = 8;
    uint32_t totalLength = 1;
    for (uint32_t size : x.sizes()) {
        totalLength *= size;
    }
    add_custom<<<numBlocks, nullptr, aclStream>>>(
        (uint8_t*)(x.mutable_data_ptr()),
        (uint8_t*)(y.mutable_data_ptr()),
        (uint8_t*)(z.mutable_data_ptr()),
        totalLength);
    return z;
}
}
```

Key official notes:
- Input tensor memory is allocated in the **Python caller** (`at::empty_like` only for output).
- Stream via `c10_npu::getCurrentNPUStream().stream(false)` — see doc-torch-npu-get-current-npu-stream.
- Kernel launch uses `<<<numBlocks, nullptr, aclStream>>>` syntax.

## torch.library Registration (Official)

```cpp
TORCH_LIBRARY(ascendc_ops, m) {
    m.def("ascendc_add(Tensor x, Tensor y) -> Tensor");
}
TORCH_LIBRARY_IMPL(ascendc_ops, PrivateUse1, m) {
    m.impl("ascendc_add", TORCH_FN(ascendc_ops::ascendc_add));
}
```

Python: `torch.ops.ascendc_ops.ascendc_add(x, y)` after `torch.ops.load_library(...)`.

## Pybind Registration (Official)

```cpp
PYBIND11_MODULE(ascendc_ops, m) {
    m.doc() = "add_custom pybind11 interfaces";
    m.def("ascendc_add", &ascendc_ops::ascendc_add, "");
}
```

Python: `import ascendc_ops; ascendc_ops.ascendc_add(x, y)`.

## Related Official Samples

- Ascend/samples PR #2815 — torch.library + pybind examples (Gitee)
- CANN Kernel Launch operator development guide (atlas_ascendc_10_0056)
