---
id: technique-pr-samples-2718
title: "PR Insight: Ascend/samples #2718"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - memory-management
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/2718"
---

# PR Insight: Ascend/samples #2718

**Title:** add workspace * add workspace

## Overview
This PR adds workspace samples demonstrating how to manage temporary memory allocations on Ascend. Workspaces are used for intermediate results in complex operations.

## Technical Significance
Workspace management is critical for memory-intensive operations. Proper workspace allocation and reuse reduces memory pressure and improves performance for complex kernels.

## Related
- `technique-data-reuse`, `memory-management-patterns`