---
id: technique-pr-vllm-ascend-5958
title: "PR Insight: vllm-project/vllm-ascend #5958"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v32
  - mtp
  - spec-decode
  - cherry-pick
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5958"
---

# PR Insight: vllm-project/vllm-ascend #5958

**Title:** [0.13.0][Bugfix] Fix setting of `speculative_config.enforce_eager` for dsv32

## Overview
This is a cherry-pick of PR #5945 for the v0.13.0 release branch. It fixes the setting of speculative_config.enforce_eager for DeepSeek V3.2 with MTP by ignoring vLLM's enforce_eager requirement since Ascend supports graph mode.

## Technical Significance
This fix ensures the v0.13.0 branch enables graph mode for DeepSeek V3.2 with MTP on Ascend, providing better performance than eager execution. The cherry-pick only includes changes to platform.py, maintaining the fix's scope. By ignoring the enforce_eager setting, Ascend can use its optimized graph implementation while the community falls back to eager mode.

## Related
- `technique-pr-vllm-ascend-5945`, `technique-spec-decode`, `technique-mtp`