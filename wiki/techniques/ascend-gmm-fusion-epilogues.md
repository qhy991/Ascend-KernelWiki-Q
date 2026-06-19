---
id: technique-ascend-gmm-fusion-epilogues
title: "GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues"
type: wiki-technique
architectures: [ascend910, ascend910b]
tags: [gmm-fusion, grouped-matmul, grouped-gemm, moe, swiglu, quantization, add-fusion, nz-format]
confidence: inferred
techniques: [cube-vector-overlap, tiling-strategy, nz-tiling, quantization-int8]
hardware_features: [cube-unit, vector-unit, unified-buffer, nz-format]
kernel_types: [moe, grouped-gemm, matmul, elementwise, quant-matmul, activation]
related: [kernel-moe-ascendc, kernel-grouped-gemm-ascendc, kernel-swiglu-ascendc, technique-cube-vector-overlap]
sources:
  - "pr-cann-ops-adv-140"
  - "pr-cann-ops-adv-001"
reproducibility: concept
---

# GMM Fusion for Ascend MoE — Add, SwiGLU, and Quant Epilogues

Grouped matmul (GMM) is the core compute shape for MoE expert layers. On Ascend, the most valuable GMM optimizations often happen immediately after the Cube matmul: add, activation, dequant, quant, and routing/finalize steps that would otherwise become separate launches and Global Memory round-trips.

This page is a cross-PR map of the fusion ladder rather than a duplicate of individual operator source pages.

## Problem Framing

A MoE expert block often looks like:

```text
tokens -> grouped matmul -> epilogue -> next grouped matmul / routing
```

If the epilogue is small but separate, it still costs:

- one or more extra framework/operator launches;
- writing GMM output to Global Memory;
- reading it back for activation/add/quant;
- more places for layout and scale metadata to drift.

GMM epilogue fusion tries to keep the post-matmul work close to the Cube output, usually in UB and Vector stages.

## Fusion Ladder

| Fusion Level | Evidence | What Is Fused | Main Benefit |
| --- | --- | --- | --- |
| GMM + Add | `pr-cann-ops-adv-140` | grouped matmul plus post-add epilogue | removes a small standalone add and its GM traffic |
| GMM + SwiGLU + Quant | `pr-cann-ops-adv-001` | Cube GMM, Vector SwiGLU, per-token quant | turns MoE FFN up-projection into one fused epilogue path |
| Runtime integrations | vLLM / MindSpeed PR pages | route model MoE calls into fused ops | makes fused kernels reachable from serving/training stacks |

The ladder matters because each rung has different risk. Add fusion is mostly shape/broadcast correctness. SwiGLU+Quant fusion adds activation precision, scale layout, and output dtype contracts.

## Operator Boundary

Not everything around GMM belongs inside the GMM operator:

- **Good epilogue candidates:** bias/add, activation, cast, quant/dequant, scale generation.
- **Usually separate concerns:** expert routing, token permutation, all-to-all, final combine across ranks.
- **Boundary cases:** `moe_finalize_routing_v2` coupling in `pr-cann-ops-adv-140` shows that even a GMM Add operator can require routing/finalize interface adjustments.

The rule is to fuse work that consumes the immediate GMM output and has stable shape/scale semantics. Keep distributed routing and rank-level communication explicit unless the fused op owns that full contract.

## Data and Layout Constraints

Ascend GMM fusion is constrained by hardware layout:

- **Cube stage:** grouped matmul should feed the Cube unit with the expected weight layout, often NZ for high-throughput matmul.
- **Vector stage:** add, SwiGLU, and quant are Vector/UB-friendly epilogues.
- **UB footprint:** fusion increases resident intermediates; too-large token tiles can spill or force split workspace paths.
- **Barriers:** Cube→Vector transitions need explicit synchronization when Vector consumes Cube output.
- **Scale layout:** quant/dequant scale shapes must match the next operator's expectations.

## Choosing a Fusion

Use **GMM + Add** when:

- the post-matmul add is deterministic and shape-compatible;
- the add otherwise creates a separate memory-bound launch;
- routing/finalize APIs can absorb the fused output contract.

Use **GMM + SwiGLU + Quant** when:

- the GMM is the gate/up projection of a quantized MoE FFN;
- the next down-projection expects int8 plus per-token scale;
- UB budget can hold the activation/quant intermediates;
- weight layout and scale conventions are fixed at load time.

Avoid fusion when:

- tile sizes are too small and barrier/launch overhead dominates;
- scale or broadcast semantics vary by caller;
- downstream routing needs unfused intermediate tensors.

## Pitfalls

- **Duplicate format conversion:** late ND↔NZ conversion can erase fusion benefits.
- **Scale mismatch:** per-token and per-channel scales are not interchangeable.
- **Broadcast ambiguity:** post-add semantics must match grouped expert segment shapes.
- **Routing coupling:** MoE finalize/routing changes can be required even when the visible op is “just add.”
- **Over-fusion:** fusing across communication or routing boundaries can make correctness harder to validate.

## Evidence Map

- `pr-cann-ops-adv-140` — `GroupedMatmulAdd`, examples, tiling/ophost, UT, and `moe_finalize_routing_v2` coupling.
- `pr-cann-ops-adv-001` — `grouped_matmul_swiglu_quant`, Cube→Vector MoE FFN up-projection fusion with NZ weights and quant output.
- `kernel-moe-ascendc` — MoE execution context.
- `kernel-grouped-gemm-ascendc` — grouped GEMM base pattern.
- `kernel-swiglu-ascendc` — SwiGLU activation context.
- `technique-cube-vector-overlap` — generic fusion principles.
