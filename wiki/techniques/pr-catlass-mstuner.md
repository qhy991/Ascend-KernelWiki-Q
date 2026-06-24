---
id: technique-pr-catlass-mstuner
title: 'PR Insight: MSTuner Automated Tiling Search'
type: wiki-technique
architectures:
- ascend910
- ascend910b
tags:
- catlass
- tuning
- profiling
confidence: inferred
sources:
- pr-catlass-266
---

# PR Insight: MSTuner Automated Tiling Search

**Source:** [Catlass PR #266](https://gitee.com/ascend/catlass/pulls/266)

The performance of an AscendC matrix multiply kernel is almost entirely dictated by its **Tiling Shape**—the exact $m, n, k$ dimensions used to slice the matrices so they perfectly fit into the L1, L0A, L0B, and Unified Buffers.

## The Problem with Manual Tiling

Finding the absolute optimal tiling shape for a specific matrix size requires balancing:
1. Cube Unit utilization rates.
2. MTE2 (Memory Transfer Engine from L1 to L0) bandwidth.
3. MTE1 (GM to L1) bandwidth.

Developers historically spent hours manually tweaking these `baseM`, `baseN`, and `baseK` variables in Catlass to squeeze out maximum TFLOPS.

## The `mstuner_catlass` Tool

This PR introduces a revolutionary utility: `mstuner_catlass`.

### Features:
1. **One-Click Search Space Generation**: Given an input shape, the tool auto-generates a vast search space of valid Tiling shapes that respect the hardware's strict memory alignment constraints (e.g., 32-byte alignment for float16).
2. **Automated Profiling Compilation**: Using a single command (`bash scripts/build.sh ... mstuner_catlass`), it compiles hundreds of distinct Catlass kernel variants.
3. **Execution and Ranking**: The tool iterates through the compiled binaries on the NPU, records the exact execution latency via hardware performance counters, and spits out the mathematical optimum.

By automating the "Dark Art" of tiling shape configuration, `mstuner_catlass` guarantees that developers are running at the absolute physical limit of the Ascend Cube unit.
