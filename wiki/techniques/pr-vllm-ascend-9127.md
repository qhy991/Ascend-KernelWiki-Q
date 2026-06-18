---
id: technique-pr-vllm-ascend-9127
title: "PR Insight: vllm-project/vllm-ascend #9127"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - eagle
  - copy-operator
  - 910c
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9127"
---

# PR Insight: vllm-project/vllm-ascend #9127

**Title:** [Feature] adapt copy_and_expand_eagle_input op to 910c and fix shift bug

## Overview
This PR adapts the `copy_and_expand_eagle_input` operator to the Ascend 910c architecture for use in unified parallel speculative decoding methods like Pard and P-eagle. It also fixes a shift bug in the operator implementation.

## Technical Significance
The adaptation to 910c extends speculative decoding support to a new Ascend architecture, enabling efficient token expansion for parallel speculative decoding approaches. The shift bug fix ensures correct token positioning and expansion logic, which is critical for maintaining numerical accuracy and preventing incorrect predictions in speculative decoding workflows.

## Related
- `technique-speculative-decoding`, `kernel-attention-ascendc`, `kernel-moe-ascendc`