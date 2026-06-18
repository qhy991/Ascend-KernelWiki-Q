---
id: technique-pr-vllm-ascend-6340
title: "PR Insight: vllm-project/vllm-ascend #6340"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - bugfix
  - attention
  - chunkprefill
  - ascend310p
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6340"
---

# PR Insight: vllm-project/vllm-ascend #6340

**Title:** [Fixbugs]: fix refactor cause to 310p chunkprefill error

## Overview
This PR adapts model runner refactor changes to fix chunkprefill errors on Ascend 310P hardware. The fix was made in `vllm_ascend/_310p/attention/attention_v1.py` to maintain compatibility with the refactored codebase.

## Technical Significance
The model runner refactor introduced changes that broke chunkprefill functionality on 310P hardware. This fix ensures that Ascend 310P continues to support chunked prefill inference properly after upstream refactoring.

## Related
- `technique-chunkprefill`
- `technique-attention`
- `hw-ascend310p`