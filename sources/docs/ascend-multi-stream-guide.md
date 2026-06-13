---
id: doc-ascend-multi-stream-guide
title: "Multi-Stream Execution on Ascend NPU"
type: source-doc
architectures: [ascend910, ascend910b]
tags: [multi-stream, concurrent, pipeline, cann]
date: '2026-01-25'
url: https://www.hiascend.com/document/detail/en/canncommercial/800/devg/aolapig/aolapi_0014.html
techniques: [pipeline-scheduling, hccl-optimization]
confidence: verified
---

# Ascend Multi-Stream Execution Guide

CANN API documentation for managing multiple execution streams on Ascend NPUs, enabling concurrent kernel execution and communication-compute overlap.

## Stream Concept

Each stream represents an independent task queue on AICore. Streams execute concurrently when resources are available, enabling:
- Overlapping compute with communication
- Pipelining data preprocessing with inference
- Concurrent execution of independent operators

## Core APIs

```c
// Stream lifecycle
aclrtCreateStream(&stream);
aclrtLaunchKernel(kernel_func, stream, args...);
aclrtSynchronizeStream(stream);
aclrtDestroyStream(stream);

// Event-based synchronization
aclrtCreateEvent(&event);
aclrtRecordEvent(event, stream);
aclrtWaitEvent(event, wait_stream);
aclrtDestroyEvent(event);
```

## Use Cases

### 1. Compute-Communication Overlap

```c
// Stream 0: Compute
aclrtLaunchKernel(matmul_kernel, stream0, A_local, B_local, C_local);
aclrtLaunchKernel(matmul_kernel, stream0, A_local, B_local, C_local);

// Stream 1: Communication (concurrent with compute)
aclrtWaitEvent(stream1, compute_done_event);  // Wait for first matmul
HcclAllReduce(C_local, C_global, stream1);   // AllReduce while second matmul runs
aclrtRecordEvent(comm_done_event, stream1);
```

**Benefit**: 30-40% reduction in step time for training

### 2. Preprocessing Inference Pipeline

```c
// Stream 0: Input preprocessing
aclrtLaunchKernel(preprocess_kernel, stream0, raw_data, processed_data);

// Stream 1: Model inference (waits for preprocessing)
aclrtWaitEvent(stream1, preprocess_done);
aclrtLaunchKernel(inference_kernel, stream1, processed_data, output);

// Stream 2: Postprocessing (concurrent with next inference)
aclrtLaunchKernel(postprocess_kernel, stream2, output, final_result);
```

**Benefit**: Hides preprocessing latency

### 3. Concurrent Operator Execution

```c
// Stream 0: LayerNorm on sequence 0
aclrtLaunchKernel(layernorm_kernel, stream0, seq0_data);

// Stream 1: LayerNorm on sequence 1 (concurrent)
aclrtLaunchKernel(layernorm_kernel, stream1, seq1_data);

// Stream 2: Attention on sequence 0 (concurrent with seq1 LN)
aclrtLaunchKernel(attention_kernel, stream2, seq0_data);
```

**Benefit**: Better AICore utilization for batch processing

## Resource Constraints

**AICore Limitation**: Total concurrent streams limited by AICore count
- Ascend 910: 56 AICores → max ~56 concurrent kernel instances
- Ascend 910B: 64 AICores → max ~64 concurrent kernel instances

**Memory Bandwidth**: Too many concurrent streams can saturate GM bandwidth

**Synchronization**: Excessive cross-stream synchronization can serialize execution

## Performance Guidelines

1. **Profile before optimizing**: Use msprof to identify compute-comm overlap opportunities
2. **Limit active streams**: 2-4 streams typically optimal; more adds overhead
3. **Use events, not barriers**: Event-based sync more efficient than stream synchronization
4. **Batch-dependent kernels**: Group independent operations to same stream

## Hardware Features

- **HCCS**: High-speed inter-NPU communication for multi-stream distributed training
- **Unified Buffer**: Each AICore has independent UB, enabling true concurrent execution
- **Queue Architecture**: Separate MTE/Vector/Cube queues per stream

## Related Patterns

- [Pipeline Scheduling](technique-pipeline-scheduling) — intra-stream overlap
- [HCCL Optimization](technique-hccl-optimization) — multi-NPU communication patterns
- [Double Buffering](technique-double-buffering) — data management in pipelines
