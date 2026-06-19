---
id: pattern-manifest-driven-kernel-autotune
title: "Manifest-Driven Kernel Autotune — Separate Kernel Inventory from Shape Selection"
type: wiki-pattern
architectures: [ascend910, ascend910b]
tags: [catlass, autotune, manifest, tiling, gemm, tooling, pattern]
confidence: source-reported
sources: [pr-catlass-266]
symptoms: ["best GEMM tile differs by shape", "manual tile selection does not scale", "benchmark results cannot be traced back to kernel policy"]
techniques: [tiling-strategy, workspace-management]
hardware_features: [cube-unit, l1-buffer, l0-buffer]
kernel_types: [gemm, matmul, grouped-gemm]
related: [technique-tiling-strategy, technique-workspace-management]
---

# Manifest-Driven Kernel Autotune — Separate Kernel Inventory from Shape Selection

## Problem

Template GEMM libraries can generate many valid kernels. For one shape, a large L1 tile may win; for another, a different L0 tile or swizzle policy may be better. If kernel inventory and benchmark selection are mixed together, tuning becomes ad hoc and hard to reproduce.

## Pattern

Use a generated manifest as the boundary between kernel generation and runtime selection:

```text
search-space config -> generated operation registrations -> Manifest
Manifest + problem config -> filtered candidate pool
candidate + workspace -> launch/profile
metrics -> selected kernel policy
```

## Design Rules

- Encode operation metadata in a uniform `OperationDescription`.
- Register all generated candidates into a `Manifest` before tuning.
- Keep problem-specific filtering in `OpConfig`, not inside generated kernels.
- Allocate and pass per-candidate workspace through a common launcher.
- Record metrics with stable kernel names and policy parameters.
- Reset or control cache state when comparing candidates.

## Ascend-Specific Notes

CATLASS candidates differ in Cube-facing tile shapes, L1/L0 data residency, and grouped-GEMM segmentation. A tuner must therefore validate not only mathematical shape compatibility but also workspace and memory hierarchy constraints.

## Evidence

- `pr-catlass-266` — adds `mstuner_catlass`, generated `Manifest`/`Operation` registration, GEMM/grouped-GEMM search-space configuration, runtime launcher, profiler, metrics, and L2-clear support.
