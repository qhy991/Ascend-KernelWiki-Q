# Index: By Problem


Symptom → Pattern → Technique → Solution


### Format-Conversion Overhead — Excess ND<->NZ Transposes

- ID: `pattern-format-conversion-overhead`
- Path: `wiki/patterns/format-conversion-overhead.md`
- Tags: repeated ND->NZ conversion every step, Vector unit busy transposing not computing, weights re-converted each forward pass, high MTE traffic for layout change
- Related: `technique-format-conversion`, `hw-nz-format`, `pattern-nz-format-traps`

### Host-Dispatch-Bound Kernel — Launch Overhead Dominates

- ID: `pattern-host-dispatch-bound`
- Path: `wiki/patterns/host-dispatch-bound.md`
- Tags: NPU idle gaps between kernels in msprof timeline, small per-op device time but high end-to-end latency, high aclrt host API time, throughput barely improves with larger batch
- Related: `lang-ascendcl-host-guide`, `technique-tiling-strategy`, `pattern-pipeline-stall`

### Low Cube Utilization — Diagnosis and Resolution

- ID: `pattern-low-cube-utilization`
- Path: `wiki/patterns/low-cube-utilization.md`
- Tags: Cube utilization <50%, Vector/MTE queues idle, small matrix dimensions, frequent Cube stalls
- Related: `hw-cube-unit`, `technique-cube-vector-overlap`, `technique-nz-tiling`

### Memory-Bound Kernel — Diagnosis and Resolution

- ID: `pattern-memory-bound`
- Path: `wiki/patterns/memory-bound.md`
- Tags: GM bandwidth >90% utilized, Cube/Vector utilization <30%, kernel time dominated by DataCopy, low arithmetic intensity
- Related: `technique-double-buffering`, `technique-data-reuse`, `hw-unified-buffer`

### MTE (Memory Transfer Engine) Saturation

- ID: `pattern-mte-saturation`
- Path: `wiki/patterns/mte-saturation.md`
- Tags: dma

### FRACTAL_NZ Format Traps — Common Pitfalls and Solutions

- ID: `pattern-nz-format-traps`
- Path: `wiki/patterns/nz-format-traps.md`
- Tags: Cube produces garbage output, Matrix dimensions not aligned to 16, Unexpected format conversion overhead >15%, NZ reshape errors
- Related: `technique-nz-tiling`, `technique-format-conversion`, `hw-cube-unit`

### Pipeline Stall — Queue Dependency Bottleneck

- ID: `pattern-pipeline-stall`
- Path: `wiki/patterns/pipeline-stall.md`
- Tags: MTE queue idle while Vector waits, Cube queue has gaps between operations, PipeBarrier taking >10% of kernel time, Low overall AICore utilization
- Related: `hw-instruction-queue`, `technique-pipeline-scheduling`, `technique-double-buffering`

### Precision Loss & NaN Debugging

- ID: `pattern-precision-nan-debugging`
- Path: `wiki/patterns/precision-nan-debugging.md`
- Tags: accuracy

### Scalar Unit Bottleneck

- ID: `pattern-scalar-bottleneck`
- Path: `wiki/patterns/scalar-bottleneck.md`
- Tags: pipeline

### Tiling Too Small — Under-Utilized Cube and MTE

- ID: `pattern-tiling-too-small`
- Path: `wiki/patterns/tiling-too-small.md`
- Tags: Cube utilization low despite a compute-bound shape, many short MTE transfers, tile dims below the 16x16 fractal, kernel time dominated by loop and sync overhead
- Related: `pattern-low-cube-utilization`, `technique-tiling-strategy`, `hw-cube-unit`

### UB OOM (Unified Buffer Overflow)

- ID: `pattern-ub-oom`
- Path: `wiki/patterns/ub-oom.md`
- Tags: memory-bound

### TQue Deadlock Pattern in Ascend C

- ID: `wiki-pattern-tque-deadlock`
- Path: `wiki/patterns/tque-deadlock.md`
- Tags: instruction-queue, pipeline-scheduling, ascendc