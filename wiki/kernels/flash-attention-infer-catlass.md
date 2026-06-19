---
id: kernel-flash-attention-infer-catlass
title: "Flash Attention Infer in CATLASS"
type: wiki-kernel
architectures: [ascend910, ascend910b]
tags: [catlass, attention, flash-attention, inference, online-softmax, cube-unit, vector-unit]
confidence: source-reported
sources: [pr-catlass-200, pr-catlass-237]
techniques: [online-softmax, tiling-strategy, workspace-management, pipeline-scheduling]
hardware_features: [cube-unit, vector-unit, unified-buffer, l1-buffer, l0-buffer, event-sync]
kernel_types: [attention, flash-attention, softmax, matmul]
languages: [ascendc, cpp]
related: [technique-tiling-strategy, technique-workspace-management, pattern-online-softmax-wait-boundary]
---

# Flash Attention Infer in CATLASS

CATLASS Flash Attention Infer is a compact example of how an Ascend attention kernel is split between Cube matrix products, Vector reductions, host tiling, and epilogue state management. PR !200 introduces the base FAI example; PR !237 shows how a small online-softmax wait boundary can still affect correctness.

## Kernel Decomposition

The forward inference path is not just one GEMM:

1. **QK block MMAD** computes score tiles using Cube resources.
2. **Online softmax epilogue** keeps row-wise max and sum state in a streamed form.
3. **PV block MMAD** multiplies normalized probability tiles with V tiles.
4. **Output rescale epilogue** converts the streamed softmax state into final O.
5. **Host tiling** defines block shapes, stride metadata, and workspace requirements.

This decomposition lets CATLASS reuse GEMM-like block policies while keeping attention-specific state in epilogues.

## Why Online Softmax Changes the Kernel Contract

Online softmax avoids materializing the full score matrix, but it creates a stricter state contract:

- row max/sum state must advance in the same order as score tiles;
- rescale must be applied when a later tile changes the running max;
- epilogue waits must match the active row/block shape;
- workspace and temporary state are part of correctness.

The `rowNum = 1` fix in PR !237 is a warning: even when QK/PV math is correct, a wait rule in the Vector epilogue can fail on a tail row shape.

## Ascend Mapping

| Component | Primary Ascend resource | Why it matters |
| --- | --- | --- |
| QK/PV MMAD | Cube + L0/L1 | matrix throughput and layout policy |
| Online softmax | Vector + UB | row max/sum reductions and rescale |
| Copy/tiling | MTE + UB/L1 | streamed K/V movement and tile residency |
| Wait policy | event sync / queues | producer-consumer ordering between score and epilogue stages |

## Design Rules

1. Keep QK and PV block policies separate; they have different operands and reuse patterns.
2. Treat online-softmax state as a first-class kernel state, not an epilogue detail.
3. Test row/block tail shapes such as `rowNum = 1` and nonuniform final blocks.
4. Validate host tiling with the same score/PV tile order used by the kernel.
5. Isolate no-mask assumptions before extending to causal, paged, or variable-length attention.

## Evidence

- `pr-catlass-200` — adds the FAI example, QK/PV block MMAD headers, online-softmax epilogue, and host tiling files.
- `pr-catlass-237` — fixes an online-softmax no-mask wait boundary when only one row is active.
