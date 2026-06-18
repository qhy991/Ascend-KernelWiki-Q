---
id: hw-ascend-910b-evolution
title: "Ascend 910B Architecture Evolution"
type: wiki-hardware
architectures:
  - ascend910b
tags:
  - hardware-overview
confidence: inferred
sources: []
---

# Ascend 910B Architecture Evolution

The Ascend 910B represents a significant architectural leap from the original 910A, specifically tailored for Large Language Model (LLM) training and inference.

## Key Improvements

1. **Enhanced AI Core Architecture**:
   - The Da Vinci architecture in 910B introduces a more balanced ratio of Cube (Matrix) to Vector (SIMD) units compared to 910A.
   - Vector Unit throughput has been significantly increased to handle complex non-linear operations (like Softmax and SwiGLU) faster, which are prevalent in Transformer architectures.

2. **Native Bfloat16 Support**:
   - 910B adds native support for the `bfloat16` data type in both the Cube and Vector units, eliminating the need to cast from FP32 or use FP16 (which risks overflow during training and long-context inference).

3. **Memory Subsystem**:
   - HBM (High Bandwidth Memory) bandwidth has been substantially increased, moving from HBM2 to faster HBM stacks.
   - The Unified Buffer (UB) and L1/L0 cache sizes have been expanded, reducing Global Memory roundtrips and allowing for larger tile sizes.

4. **Multi-Node Scaling (HCCS)**:
   - The inter-chip communication links (HCCS) offer higher bandwidth, accelerating Tensor Parallelism (TP) and Pipeline Parallelism (PP) in distributed setups.
