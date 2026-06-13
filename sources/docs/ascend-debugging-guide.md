---
id: doc-ascend-debugging-guide
title: "Ascend Kernel Debugging — Twin Debug Mode and Log Analysis"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [debugging, logging, twin-debug, cann]
date: '2026-02-01'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0074.html
confidence: verified
---

# Ascend Kernel Debugging Guide

## Overview

Ascend provides multiple debugging mechanisms for kernel development, ranging from CPU-based simulation to hardware-level profiling. This guide covers the primary debugging tools and workflows.

## Debugging Tools

### 1. Twin Debug Mode (CPU Simulator)

**Purpose**: Run AscendC kernels on a CPU simulator for step-by-step debugging before deploying to actual NPU hardware.

**How it works**:
- Simulates AICore execution on x86 CPU
- Enables standard debugging tools (gdb, lldb)
- Supports single-stepping through kernel code
- Validates algorithmic correctness without hardware access

**Usage**:
```bash
# Compile with debug flags
python3 build.py --debug=cpu

# Run with simulator
./build/cpu_simulator --kernel=my_kernel --input=./test_data

# Debug with gdb
gdb --args ./build/cpu_simulator --kernel=my_kernel --input=./test_data
```

**Limitations**:
- Performance is not representative of NPU hardware
- Some hardware-specific features may not be fully simulated
- Memory hierarchy (UB, GM) is emulated, not exact

### 2. AscendC Log Output

**Purpose**: Runtime logging for debugging kernel execution flow and intermediate values.

**API**: `AscendCLog(level, format, ...)`

**Example**:
```cpp
class DebugKernel {
public:
    __aicore__ void Process(GM_ADDR input, GM_ADDR output) {
        LocalTensor<half> x = ub.Alloc();

        // Debug: Log tensor shape
        AscendCLog(0, "Input tensor loaded, size: %d", x.GetSize());

        // Debug: Log intermediate values
        for (int i = 0; i < 10; ++i) {
            half val = x.GetValue(i);
            AscendCLog(0, "x[%d] = %f", i, val);
        }

        // Compute
        Add::Compute(x, bias, x);

        // Debug: Log result
        AscendCLog(0, "Add completed, result[0] = %f", x.GetValue(0));
    }
};
```

**Log levels**:
- `0`: Critical errors
- `1`: Warnings
- `2`: Informational
- `3`: Debug (verbose)

**Enable logging**:
```bash
# Set environment variable
export ASCENDC_LOG_LEVEL=3

# Run application
./my_application
```

### 3. Error Dump

**Purpose**: Automatic dump of kernel state on crashes or assertion failures.

**What gets dumped**:
- AICore register state
- UB memory contents
- GM memory regions accessed
- Call stack and instruction pointer
- Input/output tensor shapes

**Dump location**: `/var/log/npu/` or configured path

**Example analysis**:
```bash
# Find latest dump
ls -lt /var/log/npu/dump_*

# Analyze with cann tools
cann-analyzer --dump=/var/log/npu/dump_20260201_153022
```

### 4. msprof Analysis

**Purpose**: Performance debugging to identify bottlenecks, not functional correctness.

**For debugging**:
- Identify kernels that hang or timeout
- Find memory access violations (shows up as bandwidth spikes)
- Detect pipeline stalls (Cube/Vector idle time)

**Usage**:
```bash
# Profile with debug level
msprof --application=./my_app --level=2 --output=./debug_profile

# Check for anomalies
cann-analyzer --profile=./debug_profile --check-anomalies
```

## Recommended Debugging Workflow

### Phase 1: Algorithm Verification (Twin Debug)

1. Write kernel implementation
2. Compile with `--debug=cpu`
3. Run on CPU simulator with test inputs
4. Use gdb/lldb for step-through debugging
5. Verify algorithmic correctness

### Phase 2: Integration Testing

1. Compile for NPU hardware
2. Run with small input sizes
3. Enable `AscendCLog` for execution flow
4. Check error dumps if crashes occur
5. Verify outputs match CPU simulator

### Phase 3: Performance Validation

1. Profile with msprof
2. Check hardware unit utilization
3. Identify bottlenecks
4. Optimize pipeline overlap

### Phase 4: Production Deployment

1. Full-scale testing
2. Monitor error logs
3. Collect production profiles
4. Compare with baseline performance

## Common Debugging Scenarios

### Kernel Crash on NPU

**Symptoms**: Application exits with NPU error code

**Debugging steps**:
1. Check error dump for register state
2. Verify UB memory allocation (no overflow)
3. Check GM address calculations (no out-of-bounds)
4. Validate tensor shapes and strides

### Wrong Output Values

**Symptoms**: Kernel executes but produces incorrect results

**Debugging steps**:
1. Run in twin debug mode with known inputs
2. Add `AscendCLog` for intermediate values
3. Compare CPU simulator output with expected
4. Verify data format (NZ vs C1) is correct

### Performance Regression

**Symptoms**: Kernel slower than previous version

**Debugging steps**:
1. Profile both versions with msprof
2. Compare hardware unit utilization
3. Check for pipeline bubbles
4. Verify tile sizes haven't changed

### Memory Access Errors

**Symptoms**: Garbage output, crashes, or error dumps

**Debugging steps**:
1. Check GM address calculations
2. Verify UB allocation sizes
3. Use error dump to find offending instruction
4. Add bounds checks in twin debug mode

## Best Practices

1. **Always start with twin debug**: Validate algorithm before hardware testing
2. **Use assertions**: Add runtime checks in debug builds
3. **Log intermediate values**: Helps narrow down incorrect computations
4. **Profile regularly**: Performance regressions caught early are easier to fix
5. **Keep debug builds**: Don't strip debug symbols from production builds

## Integration with IDEs

### VS Code

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "AscendC Twin Debug",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/cpu_simulator",
            "args": ["--kernel=my_kernel", "--input=${workspaceFolder}/test_data"],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```

## Learning Resources

- Official debugging guide: [AscendC Debugging Documentation](https://www.hiascend.com/document/detail/en/canncommercial/800/opdevg/Ascendcopdevg/atlas_ascendc_10_0074.html)
- Twin debug tutorial: CANN Training Camp module 5
- Error dump reference: CANN Error Code Manual

## Status

Verified against CANN 8.0. Twin debug mode fully supported for AscendC kernels.
