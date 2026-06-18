---
id: technique-pr-vllm-ascend-7631
title: "PR Insight: vllm-project/vllm-ascend #7631"
type: wiki-technique
architectures:
  - ascend910b
tags:
  - mxfp8
  - verl
  - rl
  - weight-restore
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7631"
---

# PR Insight: vllm-project/vllm-ascend #7631

**Title:** [Feat] Support MXFP8 rollout for veRL on Ascend 950

## Overview
This PR enables MXFP8 rollout in veRL v0.8.0 when using Ascend 950 devices (DV100 and DV120). Key changes include implementing restore_weights_for_rl_loading method, adding _mxfp8_transformed flag for correct sequential execution of process_weights_after_loading, and protecting w13 and w2 weight attributes from being reset when quantization is enabled.

## Technical Significance
This feature matters for RL training efficiency on Ascend 950. veRL requires specific weight loading patterns for RL scenarios. The implementation ensures MXFP8 quantized weights are correctly restored and processed during RL training loops, enabling efficient RLHF and other reinforcement learning workflows with quantized models.

## Related
- technique-mxfp8
- technique-rl-training
- technique-quantization