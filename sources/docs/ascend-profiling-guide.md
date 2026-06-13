---
id: doc-ascend-profiling-guide
title: "Ascend Profiling with msprof"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [profiling, msprof, performance, debugging]
date: '2026-01-15'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/devg/aolapig/aolapi_0032.html
hardware_features: [cube-unit, vector-unit, mte, unified-buffer]
techniques: [pipeline-scheduling, cube-vector-overlap]
confidence: verified
---

# Ascend Profiling with msprof

## Overview

msprof is Ascend's primary profiling and performance analysis tool, equivalent to NVIDIA's Nsight Systems/Compute. It provides detailed visibility into AICore execution, memory transfers, and hardware unit utilization.

## Key Capabilities

### AICore Timeline View
Visual timeline of AICore execution showing:
- Cube unit activity (matrix operations)
- Vector unit activity (element-wise operations)
- MTE (Memory Transfer Engine) operations
- Scalar unit control flow
- Pipeline bubbles and stalls

### Hardware Unit Utilization
Real-time utilization metrics for each unit:
- **Cube FLOPS utilization**: Percentage of theoretical FLOPS achieved
- **Vector throughput**: Operations per cycle on Vector unit
- **MTE bandwidth**: GM↔UB transfer bandwidth usage
- **UB occupancy**: Memory usage in Unified Buffer

### Memory Bandwidth Monitoring
Track memory system performance:
- GM bandwidth utilization
- UB transfer rates
- Memory access patterns and hotspots

### Hotspot Identification
Automatically identify performance bottlenecks:
- Kernels with longest execution time
- Functions with highest CPU overhead
- Memory transfer stalls
- Pipeline inefficiencies

## Key Metrics

### Cube Utilization
- **Target**: >80% for compute-bound kernels
- **Warning**: <50% indicates under-utilization (small tiles, poor batching)

### Vector Utilization
- **Target**: >70% for vector-heavy operations
- **Warning**: <40% suggests inefficient element-wise operations

### GM Bandwidth
- **Target**: <90% for compute-bound kernels
- **Warning**: >90% indicates memory-bound (need data reuse, larger tiles)

### Pipeline Overlap
- **Target**: Cube and Vector queues both active concurrently
- **Warning**: Sequential execution leaves one unit idle

## Command Line Usage

### Basic Profiling

```bash
# Profile an application
msprof --application=./my_operator --output=./prof_data

# Profile with kernel-level detail
msprof --application=./my_op --level=1 --output=./prof_data

# Profile with trace-level detail
msprof --application=./my_op --level=2 --output=./prof_data
```

### Analysis Options

```bash
# Generate summary report
msprof --analysis=input_dir --output=output_dir

# Compare two profiling runs
msprof --analysis=input_dir1 --analysis=input_dir2 --compare

# Export timeline for visualization
msprof --trace=input_dir --format=json
```

## Diagnostic Workflow

### 1. Identify Slow Kernels
Use msprof to list kernels by execution time. Focus on top 10% that consume 90% of time.

### 2. Analyze Hardware Utilization
Check Cube/Vector/MTE metrics:
- **Low Cube + high GM bandwidth**: Memory-bound, need data reuse
- **Low Cube + idle Vector**: Sequential execution, need pipeline overlap
- **High Cube stalls**: Check NZ format, tile sizes

### 3. Examine Timeline
View AICore timeline to visualize:
- Pipeline bubbles between operations
- MTE idle periods during compute
- Contention between queues

### 4. Memory Analysis
Check UB usage:
- **Underutilized UB**: Can increase tile sizes
- **Overutilized UB**: Risk of out-of-memory errors

## Performance Patterns

### Memory-Bound Pattern
```
GM Bandwidth: 95% (WARNING)
Cube Utilization: 15% (WARNING)
Vector Utilization: 10% (WARNING)
Dominant operation: DataCopy (GM ↔ UB)
```
**Solution**: Increase tile size, implement double buffering, add data reuse.

### Compute-Bound Pattern
```
GM Bandwidth: 45%
Cube Utilization: 85%
Vector Utilization: 5% (IDLE)
Dominant operation: Matmul::Compute
```
**Solution**: Good Cube utilization. Overlap Vector operations if available.

### Sequential Execution Pattern
```
Timeline: [Cube op] → [wait] → [Vector op] → [wait] → [Cube op]
Cube/Vector overlap: 0% (WARNING)
```
**Solution**: Use independent queues to overlap Cube with Vector.

## Integration with Development Workflow

### During Development
```bash
# Quick profile after kernel changes
msprof --app=./test_op --output=./quick_profile
```

### Performance Regression Testing
```bash
# Automated profiling in CI/CD
msprof --app=./bench_op --output=./regression_profile
msprof --analysis=./regression_profile --threshold=10%
```

### Production Debugging
```bash
# Full trace production issues
msprof --app=./production_bin --level=2 --output=./full_trace
```

## Best Practices

1. **Profile early and often**: Don't wait for performance issues
2. **Use appropriate profiling level**: Level 0 for quick checks, Level 2 for deep analysis
3. **Compare baselines**: Always profile against a known-good version
4. **Focus on hotspots**: 80% of time spent in 20% of kernels
5. **Validate hardware utilization**: Check all units (Cube, Vector, MTE) are working

## Learning Resources

- Official documentation: [msprof API Reference](https://www.hiascend.com/document/detail/en/canncommercial/800/devg/aolapig/aolapi_0032.html)
- Tutorial: CANN Training Camp profiling module
- Case studies: Huawei developer community profiling examples

## Status

Verified against CANN 8.0. Acts as the official profiling tool for Ascend NPUs.
