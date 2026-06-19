---
id: pattern-online-softmax-wait-boundary
title: "Online Softmax Wait Boundary — Tail Row Synchronization Drift"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [catlass, attention, flash-attention, online-softmax, preload, synchronization, bugfix, pattern]
confidence: source-reported
sources: [pr-catlass-237, pr-catlass-200]
symptoms: ["attention forward fails only on row tail shapes", "rowNum=1 path hangs or reads stale softmax state", "QK/PV matmul tests pass but full attention fails"]
techniques: [online-softmax, pipeline-scheduling]
hardware_features: [vector-unit, unified-buffer, instruction-queue, event-sync]
kernel_types: [attention, flash-attention, softmax]
related: [kernel-flash-attention-infer-catlass, technique-pipeline-scheduling]
---

# Online Softmax Wait Boundary — Tail Row Synchronization Drift

## Symptom

A streaming attention kernel works for normal row blocks but fails, stalls, or reads stale state when the active row count is one or otherwise smaller than the nominal block shape. Standalone QK or PV matrix multiply checks may pass.

## Root Cause

Online softmax epilogues are producer-consumer pipelines. Score production, row max/sum reduction, and probability/value consumption must agree on when data is ready. A wait rule written for normal multi-row progress can be wrong for tail row shapes, because the producer dependency may be absent or shifted.

## Failure Shape

```text
normal row block: QK tile -> wait -> softmax row state -> PV
tail row block:   QK tile shape changes
                  stale wait rule still assumes normal progress
                  epilogue waits incorrectly or observes wrong state
```

## Fix Pattern

- Branch wait policy on the actual active row/block shape, not only template constants.
- Keep row max/sum state advancement explicit in the epilogue.
- Test `rowNum = 1`, final-row blocks, and nonuniform sequence tails.
- Compare full attention output, not just QK/PV subcomponents.

## Evidence

- `pr-catlass-237` — focused fix in `block_epilogue_online_softmax_no_mask.hpp` for the `rowNum = 1` wait boundary.
- `pr-catlass-200` — base Flash Attention Infer implementation that provides the QK/PV + online-softmax context.
