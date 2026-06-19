---
id: pattern-workspace-offset-underallocation
title: "Workspace Offset Under-allocation — Host Tiling and Kernel Path Mismatch"
type: wiki-pattern
architectures: [ascend910b]
tags: [workspace, tiling, mte, long-context, debugging, pattern]
confidence: source-reported
sources: [pr-vllm-ascend-10041]
symptoms: ["MTE DDR address out-of-range", "long-context failure while short sequence passes", "architecture-specific attention path fails"]
techniques: [workspace-management, tiling-strategy]
hardware_features: [mte, global-memory]
kernel_types: [attention]
related: [technique-workspace-management, technique-tiling-strategy, kernel-flash-attention-npu]
---

# Workspace Offset Under-allocation — Host Tiling and Kernel Path Mismatch

## Symptom

A long-context or architecture-specific attention path fails with an MTE DDR address out-of-range error. Short sequences pass, and the same operator may work on other architectures.

In `pr-vllm-ascend-10041`, `QuantLightningIndexer` failed for DeepSeek-V4-Flash long-context serving on Ascend 950 when sequence length exceeded 300K.

## Root Cause

Host-side workspace sizing did not match the actual kernel path. The allocated workspace was too small or the offset was applied on the wrong path, so the MTE/data-movement path accessed beyond the allocated region.

This class of bug often lives in host tiling, not in the device copy loop itself.

## Why Short Tests Miss It

Short sequences may never reach the under-allocated workspace range. The failing offset can be tail-only, architecture-only, or alignment-only. A generic unit test with small sequence length can therefore pass while production long-context serving fails.

## Fix Pattern

- Split workspace allocation size from offset application.
- Gate host tiling formulas by the same architecture/path condition as the kernel.
- Use aligned dimensions in the workspace formula.
- Apply offsets only in the path that consumes that workspace.
- Add long-context tests that hit the largest workspace offsets.

## Validation Checklist

- Does host tiling know which architecture path is active?
- Are alignment constants documented and tested?
- Is every workspace offset inside the allocated size?
- Does the kernel path that applies an offset actually consume that buffer?
- Do tests cover tail sequence lengths and architecture-specific paths?

## Evidence

- `pr-vllm-ascend-10041` — Ascend 950 QLI workspace sizing: aligned `s2Size`, `s1Base=4`, `s2Base=128`, and AIV-only score workspace offset application.
