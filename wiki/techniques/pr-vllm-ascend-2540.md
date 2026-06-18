---
id: technique-pr-vllm-ascend-2540
title: "PR Insight: vllm-project/vllm-ascend #2540"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - compilation-config
  - cudagraph-mode
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2540"
---

# PR Insight: vllm-project/vllm-ascend #2540

**Title:** [Aclgraph] Update compilation config in `check_and_update_config`

## Overview
This PR updates compilation configuration logic in `check_and_update_config` by using `compilation_config.level` to update `compilation_config.cudagraph_mode` to ensure correct configuration. It also adds `compilation_config.cudagraph_num_of_warmups = 1` when V1 is enabled, fixing issue #2523 and ensuring the `aclgraphmode` is properly set during forward execution.

## Technical Significance
This fix ensures proper ACL Graph mode configuration by correctly deriving cudagraph_mode from the compilation config level. The addition of warmup count for V1 scheduler ensures compatibility with torchair graph mode requirements, preventing configuration-related runtime errors.

## Related
- `technique-aclgraph-integration`, `technique-configuration-management`, `technique-compilation-config`, `kernel-mla-v1`