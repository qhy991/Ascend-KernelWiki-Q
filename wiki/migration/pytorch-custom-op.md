---
id: migration-pytorch-custom-op
title: "PyTorch Custom Op (torch_npu)"
type: wiki-migration
tags:
  - framework
  - pytorch
confidence: inferred
sources: []
---

# PyTorch Custom Op (torch_npu)

Writing a custom AscendC kernel is only half the battle; integrating it into PyTorch so it can be called as a standard Python function (and participate in `autograd`) is the second half.

## The Integration Stack
Unlike CUDA's `pybind11` or `torch.utils.cpp_extension` which can directly compile and link `.cu` files, Ascend uses a slightly more involved toolchain:
1. **AscendC Kernel**: The `.cpp` device code.
2. **Host Wrapper**: A C++ file that sets up the `aclTensor` metadata and launches the kernel via `KernelLaunch`.
3. **PyTorch Dispatcher**: The `pybind11` bridge connecting Python arguments to the Host Wrapper.

## Using `op-compiler`
The modern way to build custom ops for PyTorch on Ascend is using the Ascend operator compilation toolchain.

### Step 1: Define the Kernel
Write your standard AscendC kernel (e.g., `add_custom.cpp`).

### Step 2: Write the PyTorch Binding (Host)
```cpp
#include "torch_npu/csrc/core/npu/NPUStream.h"
#include "torch_npu/csrc/framework/OpCommand.h"

at::Tensor add_custom(const at::Tensor& a, const at::Tensor& b) {
    auto result = at::empty_like(a);
    
    // Convert ATen tensors to ACL tensors
    // Calculate grid/block dims
    uint32_t blockDim = 8;
    
    // Launch
    ACL_APP_LOG(ACL_INFO, "Launching custom AscendC kernel");
    // (Pseudocode for dispatch)
    // MyCustomKernelLaunch(blockDim, stream, a.data_ptr(), b.data_ptr(), result.data_ptr());
    
    return result;
}

// Bind to PyTorch
TORCH_LIBRARY(my_ops, m) {
    m.def("add_custom(Tensor a, Tensor b) -> Tensor");
}
TORCH_LIBRARY_IMPL(my_ops, PrivateUse1, m) {
    m.impl("add_custom", &add_custom);
}
```
Note the use of `PrivateUse1`. `torch_npu` currently registers the NPU backend under PyTorch's `PrivateUse1` dispatch key.

### Step 3: Autograd (Optional)
If your operator requires backpropagation, you must define the `Backward` kernel and register it using standard PyTorch `torch.autograd.Function` in Python, invoking your forward and backward custom C++ calls.
