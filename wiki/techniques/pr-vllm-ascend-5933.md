---
id: technique-pr-vllm-ascend-5933
title: "PR Insight: vllm-project/vllm-ascend #5933"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - hccl
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5933"
---

# PR Insight: vllm-project/vllm-ascend #5933

**Title:** [EPLB][Bugfix] Dispatch Allgather use log2phy if enable eplb

## Overview
This PR fixes EPLB expert mapping logic by moving it forward to prevent shotgun changes and disabling expert map updates. It also ensures Dispatch Allgather uses logical-to-physical (log2phy) mapping when EPLB is enabled.

## Technical Significance
Expert mapping needs to be consistent across EPLB operations. Moving the logic forward prevents scattered updates that could cause inconsistencies. Disabling expert map updates after initialization ensures stable mappings. Using log2phy mapping in Allgather operations correctly handles expert parallelism by translating logical expert indices to physical device locations. Testing shows A2: GPQA_diamond 73.23% accuracy, A3: AIME2024 83.33% accuracy with EPLB.

## Related
- `technique-eplb`, `technique-hccl`, `technique-expert-parallel`