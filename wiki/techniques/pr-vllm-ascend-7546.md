---
id: technique-pr-vllm-ascend-7546
title: "PR Insight: vllm-project/vllm-ascend #7546"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - sharded-state
  - vl-models
  - quantization
  - 310p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7546"
---

# PR Insight: vllm-project/vllm-ascend #7546

**Title:** [BugFix][310p]Handle null quantization config in ShardedStateLoader310

## Overview
This PR fixes 310P sharded-state saving and weight-compression metadata handling. VL models often expose quant_config only on language_model, not the multimodal root, so inferring from root model was wrong. The fix passes vllm_config.quant_config from NPUWorker310 and handles None as FLOAT.

## Technical Significance
This fix matters for 310P VL model quantization support. The previous implementation incorrectly tried to access quant_config from the multimodal root model, which doesn't exist. By properly passing quant_config from the correct location and handling null cases, it enables correct weight compression and sharded-state saving for quantized VL models on 310P.

## Related
- pattern-310p-compatibility
- technique-quantization
- technique-sharded-state