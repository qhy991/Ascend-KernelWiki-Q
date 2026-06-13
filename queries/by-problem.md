# Index: By Problem


Symptom → Pattern → Technique → Solution


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