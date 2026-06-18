---
id: technique-pr-vllm-ascend-8501
title: "PR Insight: vllm-project/vllm-ascend #8501"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - eplb
  - moe
  - expert-selection
  - topk-ids
  - bugfix
  - load-balancing
  - quantization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/8501"
---

# PR Insight: vllm-project/vllm-ascend #8501

**Title:** [EPLB][BugFix] The construction of topk_ids uses the number of logical experts

## Overview
This PR fixes an issue in expert load balancing where global_num_experts was incorrectly used instead of num_experts (logical experts) for expert selection and forced load balancing. The fix changes the apply function to use num_experts and updates forced eplb to use logical expert numbers for constructing fake topk_ids. This ensures correct expert selection before log2phy mapping.

## Technical Significance
This fix is critical for correct expert selection in quantized MoE models with load balancing. Using the wrong expert count caused incorrect topk_ids values that exceeded the valid range, leading to the same expert being selected multiple times. The PR demonstrates the importance of maintaining consistent expert numbering throughout the MoE pipeline for correct load balancing.

## Related
- `technique-expert-parallel`
- `technique-load-balancing`
- `technique-quantization`