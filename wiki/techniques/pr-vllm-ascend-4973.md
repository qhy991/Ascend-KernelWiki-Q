---
id: technique-pr-vllm-ascend-4973
title: "PR Insight: vllm-project/vllm-ascend #4973"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - pipeline-parallelism
  - async-scheduling
  - kv-transfer
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4973"
---

# PR Insight: vllm-project/vllm-ascend #4973

**Title:** [Bugfix] fix pipeline parallelism bug introduced by async-scheduling refactor work

## Overview
This PR fixes a pipeline parallelism bug where model_runner returned None on non-last-PP-rank stages in sample_tokens, causing assert errors in vllm's KVOutputAggregator. The fix follows gpu_model_runner pattern by passing kv_connector_output in sample_tokens so all ranks return a ModelRunnerOutput (EMPTY_MODEL_RUNNER_OUTPUT with kv_connector_output for non-last-PP-rank workers).

## Technical Significance
Ensures proper KV transfer aggregation across pipeline parallel stages, allowing the scheduler to confirm all KV transfers are finished before releasing cache. Follows upstream vLLM patterns for consistency.

## Related
- `technique-pipeline-parallelism`
- `technique-async-scheduling`
- `technique-kv-transfer`
- `kernel-model-runner`