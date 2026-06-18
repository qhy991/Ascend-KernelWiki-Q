---
id: pattern-precision-nan-debugging
title: "Precision & NaN Debugging"
type: wiki-pattern
architectures:
  - ascend910
  - ascend910b
tags:
  - debugging
  - accuracy
confidence: inferred
sources: []
---

# Precision & NaN Debugging

`NaN` (Not a Number) or `Inf` values are a common headache when porting PyTorch or CUDA models to the Ascend NPU, especially when using mixed precision (`fp16`).

## Common Causes on Ascend

1. **FP16 Overflow in Accumulation**: The dynamic range of `fp16` maxes out at 65504. In operations like `ReduceSum` over large dimensions (e.g., Softmax denominator) or `Matmul` with large K dimensions, intermediate values easily exceed this.
2. **Division by Zero**: Common in LayerNorm/RMSNorm if the epsilon value is rounded to zero in `fp16`.
3. **Invalid Operations**: Applying `Log` to negative numbers or `Sqrt` to negative numbers.

## Diagnosis Tools

### 1. `torch_npu.npu_format_cast`
When debugging PyTorch-NPU code, isolate the operator failing and enforce `fp32` execution using `tensor.npu_format_cast()` or running under `torch.autocast("npu", enabled=false)`. If the `NaN` disappears, it is a precision overflow issue.

### 2. Printf in Camodel (Simulator)
Compile the AscendC kernel for CPU simulation (`Camodel`). Insert `printf` statements in the Vector computation loops to check intermediate UB values.
```cpp
// Works in CPU simulation mode
printf("Value at index %d: %f\n", idx, static_cast<float>(tensor.GetValue(idx)));
```

### 3. MindStudio Dump Tools
Use the Ascend `msaccucmp.py` (Accuracy Comparator) tool. 
- Enable data dumping in the PyTorch execution environment.
- The tool will dump the input/output tensors of every operator and compare them against a CPU or GPU golden reference, isolating the exact operator that introduced the `NaN`.

## Mitigation

- **Use `bfloat16`**: If on 910B hardware, migrate from `fp16` to `bf16`.
- **Upcast critical paths**: Perform `Exp`, `Sum`, and `Div` inside the Vector unit using `fp32` local tensors.
- **Scale inputs**: For Attention, ensure the queries are scaled by $1 / \sqrt{d}$ *before* the Cube unit multiplication, rather than after, to keep the $QK^T$ matrix within `fp16` bounds.
