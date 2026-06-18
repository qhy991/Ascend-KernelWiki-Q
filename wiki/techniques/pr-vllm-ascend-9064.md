---
id: technique-pr-vllm-ascend-9064
title: "PR Insight: vllm-project/vllm-ascend #9064"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - configuration
  - environment-variables
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9064"
---

# PR Insight: vllm-project/vllm-ascend #9064

**Title:** [Refactor]: migrate env vars to AscendConfig

## Overview
This PR migrates vllm-ascend environment variables from direct environment access to the `AscendConfig`/`additional_config` configuration path. It covers 10 key environment variables including `VLLM_ASCEND_BALANCE_SCHEDULING`, `VLLM_ASCEND_ENABLE_FLASHCOMM1`, `VLLM_ASCEND_ENABLE_MATMUL_ALLREDUCE`, `VLLM_ASCEND_FLASHCOMM2_PARALLEL_SIZE`, `MSMONITOR_USE_DAEMON`, `VLLM_ASCEND_ENABLE_MLAPO`, `VLLM_ASCEND_ENABLE_NZ`, `VLLM_ASCEND_ENABLE_CONTEXT_PARALLEL`, `VLLM_ASCEND_ENABLE_FUSED_MC2`, and `VLLM_ASCEND_FUSION_OP_TRANSPOSE_KV_CACHE_BY_BLOCK`.

## Technical Significance
This refactoring improves configuration management by providing a unified configuration interface while maintaining backward compatibility through environment variable fallbacks. The migration follows a clear precedence: `additional_config` explicit value > deprecated environment variable fallback > default value. This enables users to configure options through `--additional-config` while existing deployments continue to work during the transition period.

## Related
- `technique-hccl-optimization`, `technique-format-conversion`, `technique-operator-fusion`