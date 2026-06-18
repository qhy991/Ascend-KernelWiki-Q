---
id: technique-pr-vllm-ascend-9843
title: "PR Insight: vllm-project/vllm-ascend #9843"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - chunked-pipeline
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9843"
---

# PR Insight: vllm-project/vllm-ascend #9843

**Title:** [BugFix] update discard_request_mask to fix stuck chunked pipeline parallelism

## Overview
This PR fixes stuck chunked pipeline parallelism by updating the discard_request_mask logic. The issue caused requests to get stuck in the pipeline due to incorrect mask handling during request completion and pipeline progression.

## Technical Significance
Fixes pipeline deadlock issues in chunked pipeline parallelism by ensuring correct request mask updates during request discard operations. Enables smooth pipeline progression and prevents request stalling, improving system reliability.

## Related
- `technique-context-parallel`, `pattern-chunking`, `pattern-scheduler`