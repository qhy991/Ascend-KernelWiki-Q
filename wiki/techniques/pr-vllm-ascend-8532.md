---
id: technique-pr-vllm-ascend-8532
title: "PR Insight: vllm-project/vllm-ascend #8532"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - moe
  - bugfix
  - tensor-parallel
  - expert-parallel
  - initialization
  - alltoall
  - tp-only
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8532"
---

# PR Insight: vllm-project/vllm-ascend #8532

**Title:** [Ops][BugFix] : NPU MoE layers support TP only.

## Overview
This PR fixes MoE (Mixture of Experts) initialization failure on Ascend NPU when only Tensor Parallelism is enabled without Expert Parallelism. The fix ensures that self.moe_config.ep_group = get_ep_group() is only assigned when ep_size > 1, and AlltoAllCommImpl is only registered in setup_moe_comm_method() when ep_size > 1. This aligns with vLLM upstream's convention where ep_size == 1 means no EP.

## Technical Significance
This fix is critical for TP-only MoE inference, which is a common deployment scenario. The previous assumption that EP was always configured caused crashes during worker initialization. The PR demonstrates proper handling of mixed parallelism configurations and aligns with upstream vLLM conventions for MoE parallelism modes.

## Related
- `technique-moe-optimization`
- `technique-tensor-parallel`
- `technique-expert-parallel`