---
id: technique-pr-vllm-ascend-4976
title: "PR Insight: vllm-project/vllm-ascend #4976"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - kvpool
  - accuracy
  - bugfix
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4976"
---

# PR Insight: vllm-project/vllm-ascend #4976

**Title:** [bugfix] Fix mooncake kvpool accuracy issue

## Overview
This PR fixes a KVPool accuracy issue (issue #4412) without impacting prefill performance. The fix addresses precision problems in Mooncake KV cache pooling. Note: Due to an ADXL bug where current_event.synchronize() may occasionally hang, users may need to manually build hixl from gitcode before CANN 8.5.RC1 release.

## Technical Significance
Resolves accuracy degradation in Mooncake KV cache pooling while maintaining prefill performance. The fix ensures correct KV cache retrieval and reuse across inference sessions.

## Related
- `kernel-mooncake-kvpool`
- `technique-kv-pooling`
- `technique-synchronization`