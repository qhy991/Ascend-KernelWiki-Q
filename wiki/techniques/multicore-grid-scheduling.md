---
id: technique-multicore-grid-scheduling
title: "Multi-Core Grid Scheduling"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - performance
confidence: inferred
sources: []
---

# Multi-Core Grid Scheduling

Unlike CUDA's highly flexible grid/block dynamic scheduling, Ascend NPUs use a slightly more rigid, core-affinity model. Understanding how to partition workloads across AI Cores is vital for maximizing utilization (Occupancy).

## BlockDim and Core Mapping
When launching an AscendC kernel via `KernelLaunch`, the `blockDim` parameter defines the number of concurrent thread blocks.

```cpp
// Launching 32 blocks
MyKernel<<<32, nullptr, stream>>>(...);
```

- **Ascend 910A**: Has 32 AI Cores.
- **Ascend 910B**: Has 20 to 24 AI Cores (depending on the exact bin/model).

If your `blockDim` exactly matches the physical AI Core count (e.g., 20), each AI Core receives exactly one block. This 1:1 mapping is often ideal for persistent kernels or large tiled matrices.

## Over-subscription (Tail Effects)
If `blockDim` is larger than the number of physical cores (e.g., `blockDim = 30` on a 20-core NPU):
1. **Wave 1**: 20 blocks are dispatched to the 20 cores.
2. **Wave 2**: The remaining 10 blocks wait until cores become available.
This creates a "Tail Effect" where 10 cores are doing work in the final wave, while the other 10 sit idle, reducing overall TFLOPS.

**Optimization Strategy**: Tune your Tiling Strategy so that `blockDim` is a strict multiple of the physical AI Core count. If the workload size doesn't divide cleanly, handle the remainder inside the kernel (padding or partial tile logic) rather than creating a partial wave of blocks.

## Core Affinity
By default, the CANN task scheduler assigns blocks to cores automatically. For advanced workloads (e.g., Ring Attention), you may need to force specific blocks to specific cores to optimize HCCS routing or L2 Cache hits, though this requires lower-level ACL APIs.
