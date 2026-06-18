---
id: kernel-ring-attention-ascendc
title: "Ring Attention (AscendC)"
type: wiki-kernel
architectures:
  - ascend910b
tags:
  - llm
  - context-parallelism
confidence: inferred
kernel_types:
  - attention
languages:
  - ascendc
sources: []
---

# Ring Attention (AscendC)

Ring Attention is a critical algorithm for scaling Sequence Length (Context Parallelism) beyond the memory capacity of a single NPU. It distributes the sequence across multiple NPUs and passes Key/Value (KV) blocks in a ring topology.

## HCCL and Computation Overlap

The core of Ring Attention is hiding the communication latency of passing KV blocks to the next NPU behind the computation of the current KV blocks. On Ascend, this requires careful orchestration between the AI Core (which runs the AscendC kernel) and the HCCL (Huawei Collective Communication Library) engine.

### Single-Operator vs Multi-Stream Approach
Traditionally, Ring Attention is implemented at the framework level (e.g., PyTorch) using multiple streams: one stream runs `flash_attention`, while another runs `hccl.send` and `hccl.recv`.

On Ascend 910B, relying on the host CPU to launch asynchronous HCCL calls between Flash Attention blocks incurs severe dispatch overhead, destroying the overlap. 

### In-Kernel HCCL (Future Capability) or Graph-Level Fusion
For optimal performance, the HCCL primitives must be tightly coupled with the computation.
1. **Graph Engine (GE) Scheduling**: The CANN Graph Engine can schedule HCCL Send/Recv nodes to run on the communication engines strictly parallel to the Flash Attention computation nodes on the AI Core.
2. **Buffer Ping-Pong**: Allocate two KV buffers in Global Memory. 
   - Buffer A is used by the AI Core for `Q @ K^T`.
   - Buffer B is simultaneously being written to by the HCCL Recv engine (receiving the next block from NPU $i-1$) and read by the HCCL Send engine (sending to NPU $i+1$).
   - Synchronize using Ascend `EVENT` primitives.

### Memory Optimization
Because the context is distributed, the local NPU only holds a slice of the Queries, but it will eventually observe the entire sequence of Keys and Values. The local Unified Buffer (UB) must maintain the running `max` and `sum` for the Online Softmax state across the entire ring pass.

## Real-World Integration: MindSpeed & vLLM

In real-world Ascend deployments, Ring Attention is typically orchestrated using Huawei's **MindSpeed** library or vLLM-Ascend. 
- **Configuration**: Developers configure the `context_parallel_size` (CP size) parameter, which dictates how many NPUs participate in the Ring.
- **HCCL Grouping**: The framework automatically creates dedicated HCCL communication groups (e.g., `All-Gather` or `Reduce-Scatter` rings) mapped specifically to the devices in the Context Parallelism group, ensuring that Ring Attention traffic does not collide with Tensor Parallelism (TP) or Pipeline Parallelism (PP) traffic over the HCCS links.
