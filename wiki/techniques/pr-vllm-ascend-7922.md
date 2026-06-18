---
id: technique-pr-vllm-ascend-7922
title: "PR Insight: vllm-project/vllm-ascend #7922"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - model-runner-v2
  - inference
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7922"
---

# PR Insight: vllm-project/vllm-ascend #7922

**Title:** [MRv2][Feature] Add initial MoE models support for MRv2

## Overview
This PR enables MoE model execution for Model Runner v2 (MRv2) on Ascend. Previously, MRv2 MoE would fail during startup or warmup due to missing required forward-context fields and MC2 runtime state. The fix wires up the Ascend MoE path by aligning `in_profile_run`, initializing MC2 runtime state, and populating forward-context fields while preserving fail-fast behavior for unsupported features.

## Technical Significance
MRv2 is the new model execution architecture in vLLM. Supporting MoE on MRv2 is critical for leveraging modern execution paths with MoE models like Qwen3. The fix addresses missing state initialization and context handling, allowing MoE models to run with `VLLM_USE_V2_MODEL_RUNNER=1` on Ascend while still explicitly failing for unwired features like DCP/PCP and dynamic EPLB.

## Related
- `kernel-moe`
- `pattern-moe-dispatch`
- `technique-inference-optimization`