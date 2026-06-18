---
id: technique-pr-vllm-ascend-5945
title: "PR Insight: vllm-project/vllm-ascend #5945"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepseek-v32
  - mtp
  - spec-decode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5945"
---

# PR Insight: vllm-project/vllm-ascend #5945

**Title:** [Bugfix] Fix setting of `speculative_config.enforce_eager` for dsv32

## Overview
This PR fixes the setting of speculative_config.enforce_eager for DeepSeek V3.2 with MTP. vLLM sets enforce_eager to True for deepseek_v32 with MTP, but Ascend supports graph mode, so the fix ignores this setting.

## Technical Significance
vLLM enforces eager mode for DeepSeek V3.2 with MTP due to community constraints, but Ascend's graph implementation works correctly. The fix ignores the enforce_eager setting to allow graph mode on Ascend. However, this also ignores user settings of speculative_config.enforce_eager, which needs to be addressed once vLLM supports this feature. The fix enables better performance on Ascend by using graph mode instead of falling back to eager execution.

## Related
- `technique-spec-decode`, `technique-mtp`, `technique-deepseek-v32`