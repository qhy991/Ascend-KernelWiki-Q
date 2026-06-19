---
id: doc-torch-npu-get-current-npu-stream
title: "c10_npu::getCurrentNPUStream — torch_npu C++ Stream API"
type: source-doc
architectures: [ascend910, ascend910b, ascend310p]
tags: [torch-npu, cpp, operator]
date: '2026-06-19'
url: https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/apilist/ptaoplist_001029.html
languages: [cpp]
confidence: verified
---

# c10_npu::getCurrentNPUStream

Official Ascend Extension for PyTorch custom C++ API for NPU stream management.

## Source

- Ascend Extension for PyTorch 6.0.0 API Reference — `(beta) c10_npu::getCurrentNPUStream`
- URL: https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/apilist/ptaoplist_001029.html
- Header: `torch_npu/csrc/core/npu/NPUStream.h`

## Function Signature

```cpp
c10_npu::NPUStream c10_npu::getCurrentNPUStream(c10::DeviceIndex device_index = -1)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `device_index` | `c10::DeviceIndex` | NPU device ID; default `-1` = current device |

Returns `c10_npu::NPUStream` — analogous to `c10::cuda::getCurrentCUDAStream()`.

## Extracting aclrtStream for Kernel Launch

From `NPUStream` class (ptaoplist_000325):

```cpp
aclrtStream c10_npu::NPUStream::stream(const bool need_empty)
```

- `stream(false)` — return current stream directly (used in AscendC `<<<>>>` launch)
- `stream(true)` / default overload — may return empty stream depending on overload

Official AscendC integration pattern:

```cpp
auto aclStream = c10_npu::getCurrentNPUStream().stream(false);
my_kernel<<<numBlocks, nullptr, aclStream>>>(...);
```

## Supported Hardware (Official)

- Atlas 训练系列产品
- Atlas A2 训练系列产品 (910B)
- Atlas A3 训练系列产品
- Atlas 推理系列产品

## Related APIs

- `c10_npu::NPUStream::query()` — non-blocking completion check
- `c10_npu::NPUStream::stream()` — aclrtStream without need_empty parameter
