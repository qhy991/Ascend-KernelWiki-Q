---
id: technique-pr-mindspeed-swap-attention-cpu
title: "PR Insight: Swap-Attention CPU Affinity"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - memory-optimization
  - training
  - mindspeed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2829"
---

# PR Insight: Swap-Attention CPU Affinity

**Source:** [MindSpeed PR #2829](https://gitee.com/ascend/MindSpeed/pulls/2829)

During massive long-context training, even the 64GB or 96GB HBM of an Ascend NPU is insufficient to hold the full KV cache alongside model weights and gradients. To survive, frameworks use "Swap-Attention," eagerly offloading KV tensors to the host CPU's DRAM over PCIe/CXL.

## The Host-Side Bottleneck
When Swap-Attention is active, the bottleneck frequently shifts from the NPU to the host CPU. If the memory copy threads are running on CPU cores that belong to a different NUMA (Non-Uniform Memory Access) node than the PCIe slot where the NPU is attached, the bandwidth collapses.

## CPU Affinity Optimization

This PR updates the crucial `swap-attention` documentation for MindSpeed, highlighting the mandatory use of **CPU Affinity binding** for training.

### How to Tune:
To maximize Host-to-Device (H2D) and Device-to-Host (D2H) bandwidth:
1. **Identify the NUMA Node**: Developers must use `lscpu` or `numactl --hardware` to identify which CPU socket the target Ascend NPU is connected to.
2. **Bind the Swapper Threads**: The PyTorch dataloader and the Swap-Attention asynchronous offload threads must be explicitly bound to the specific logical cores of that NUMA node using `taskset` or internal MindSpeed affinitization flags.
3. **Result**: Forcing CPU affinity prevents the Linux scheduler from bouncing the memory-intensive swap threads across QPI/UPI links, unlocking the full PCIe Gen4/Gen5 line rate necessary to keep the NPU fed during long-context backpropagation.
