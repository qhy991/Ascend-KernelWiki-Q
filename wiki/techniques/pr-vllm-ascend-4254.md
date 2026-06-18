---
id: technique-pr-vllm-ascend-4254
title: "PR Insight: vllm-project/vllm-ascend #4254"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - tensor-parallel
  - non-blocking
  - bugfix
  - vllm
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/4254"
---

# PR Insight: vllm-project/vllm-ascend #4254

**Title:** [Bugfix] Resolve MTP > 1 issue when lm head tp > 1

## Overview
This PR fixes a bug where MTP dummy run executed compute_logits only once regardless of num_speculative_tokens, causing execute_model to hang on compute_logits when lm head tensor parallelism exceeded 1. The fix ensures compute_logits executes correctly during dummy run, matching num_speculative_tokens. The `non_blocking` argument is set to False when moving `exceeds_max_model_len` to CPU to prevent accuracy issues.

## Technical Significance
The hang bug reveals synchronization issues between MTP dummy run and lm_head tensor parallelism. Setting non_blocking=False for CPU transfers prevents race conditions that cause accuracy problems. Proper dummy run execution is critical for correct graph capture and initialization.

## Related
- `technique-mtp`, `technique-tensor-parallel`, `pattern-synchronization`, `technique-non-blocking`, `technique-graph-capture`