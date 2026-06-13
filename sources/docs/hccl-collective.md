---
id: doc-hccl-collective
title: "HCCL Collective Communication Library"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [hccl, communication, collective, distributed]
date: '2026-01-20'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/devg/aolapig/aolapi_0026.html
hardware_features: [hccs]
techniques: [hccl-optimization]
confidence: verified
---

HCCL (Huawei Collective Communication Library) provides efficient collective communication primitives for distributed training across multiple Ascend NPUs. The library is optimized for Ascend's custom interconnect hierarchy and integrates seamlessly with the CANN software stack.

**Supported Operations**:
- **AllReduce**: Combine data from all ranks with sum/prod/max/min reduction
- **AllGather**: Gather data from all ranks and distribute the complete set
- **Broadcast**: Distribute data from root rank to all participating ranks
- **ReduceScatter**: Combine data from all ranks and distribute chunks

**Interconnect Support**: HCCL automatically detects and optimizes for the available physical interconnects:
- **HCCS**: High-speed chip-to-chip links for intra-server communication (up to 100 GB/s)
- **PCIe**: Standard PCIe interconnect for cross-server communication
- **RDMA**: Remote Direct Memory Access for network-attached devices

**Topology-Aware Optimization**: The library implements:
- Ring-based algorithms for linear topology with balanced bandwidth utilization
- Tree-based reduction for hierarchical interconnect structures
- Hardware topology discovery for automatic route optimization
- Multi-path routing for maximum aggregate bandwidth

**Performance Features**:
- Overlapping computation with communication through async APIs
- Pipeline support for hiding transfer latency
- Memory registration and pinning for zero-copy transfers
- Automatic chunk sizing based on network characteristics

HCCL provides compatibility layers with NCCL and supports common deep learning frameworks through standard API bindings.
