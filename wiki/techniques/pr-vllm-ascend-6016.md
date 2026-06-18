---
id: technique-pr-vllm-ascend-6016
title: "PR Insight: vllm-project/vllm-ascend #6016"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - hccl
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6016"
---

# PR Insight: vllm-project/vllm-ascend #6016

**Title:** [EPLB][Bugfix] Dispatch Allgather use log2phy if enable eplb (#5933)

## Overview
This is a cherry-pick combining PRs #5817 and #5933 for the main branch. It fixes EPLB expert mapping by moving logic forward and disabling expert map updates, ensuring Dispatch Allgather uses logical-to-physical (log2phy) mapping when EPLB is enabled.

## Technical Significance
This fix ensures the main branch has the same EPLB improvements as the release branch. Moving expert mapping logic forward prevents scattered changes and inconsistencies. Disabling expert map updates after initialization ensures stable mappings. Using log2phy in Allgather correctly handles expert parallelism by translating logical expert indices to physical device locations. Testing shows improved accuracy with EPLB.

## Related
- `technique-pr-vllm-ascend-5933`, `technique-pr-vllm-ascend-5817`, `technique-eplb`, `technique-hccl`