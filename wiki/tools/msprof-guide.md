---
id: tool-msprof-guide
title: "MindStudio Profiling (msprof) Deep Dive"
type: wiki-tool
tags:
  - profiling
confidence: verified
sources: []
---

# MindStudio Profiling (msprof) Deep Dive

The `msprof` tool is the primary CLI application for profiling Ascend NPU workloads. It allows you to collect detailed performance metrics, trace execution timelines, and identify bottlenecks in your AscendC kernels.

## Basic Usage

To profile an executable or Python script, use the `msprof` command with the `--application` flag:

```bash
msprof --application="python3 train.py" --output=./prof_dir
```

## Profiling Modes

1. **Task-Level Profiling**: Focuses on task scheduling, execution time, and AI Core utilization. Good for identifying host-dispatch overhead.
2. **AI Core Metrics**: Collects detailed hardware performance counters for the Cube and Vector units. Use `--aic-metrics=PipeUtilization` to see if MTE or Compute is the bottleneck.
3. **Memory Analysis**: Tracks global memory bandwidth (HBM) and Unified Buffer (UB) read/write traffic.

## Reading the Timeline

The generated trace files can be visualized in MindStudio or Chrome Trace Viewer (`chrome://tracing`):
- **Task Timeline**: Shows operator execution on the AI Cores. Look for gaps between tasks, indicating CPU dispatch bottlenecks.
- **Data Transfer**: MTE1 (GM to L1) and MTE2 (L1/GM to UB) operations. Overlap these with Cube/Vector tasks to hide latency.
- **Synchronization**: Analyze event wait times to identify pipeline stalls.
