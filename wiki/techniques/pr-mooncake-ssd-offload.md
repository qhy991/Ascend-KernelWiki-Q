---
id: technique-pr-mooncake-ssd-offload
title: "PR Insight: KV Cache SSD Offload (Mooncake)"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-cache
  - offloading
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10617"
---

# PR Insight: KV Cache SSD Offload (Mooncake)

**Source:** [vLLM-Ascend PR #10617](https://github.com/vllm-project/vllm-ascend/pull/10617)

Managing the KV Cache for long-context LLMs often exceeds the physical HBM capacity of the Ascend NPU and even the host CPU DRAM. This PR updates the documentation and implementation for **Mooncake**, a specialized KV Pool backend that supports SSD offloading.

## The Multi-Tier Architecture

To support massive context windows, the Ascend vLLM ecosystem implements a 3-tier cache:
1. **Tier 1 (HBM)**: Active KV cache blocks currently being computed on the NPU.
2. **Tier 2 (CPU DRAM)**: FabricMem/Memcache buffer pool for warm blocks that recently swapped out.
3. **Tier 3 (NVMe SSD)**: Cold blocks offloaded via the Mooncake backend.

## Mooncake Master Flow

The PR clarifies that SSD offloading is an *optional parameter* appended to the existing Mooncake master flow. 
- When an NPU runs out of HBM, the block is evacuated to the `FabricMem` pool. 
- If `FabricMem` is full, Mooncake asynchronously streams the lowest-priority blocks down to the PCIe-attached SSDs.

### Troubleshooting Put/Get Failures
A common issue during massive concurrent generation is Mooncake `Put/Get` failures. The PR highlights that these are usually caused by:
- **Memcache exhaustion**: The transitional buffer between DRAM and SSD fills up if the SSD write speed (IOPS) cannot keep up with the NPU's eviction rate.
- **Buffer Pool Fallback**: Developers must configure appropriate fallback limits so the system pauses generation rather than dropping KV blocks entirely when the storage fabric saturates.
