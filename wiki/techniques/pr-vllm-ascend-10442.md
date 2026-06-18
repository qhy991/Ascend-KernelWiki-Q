---
id: technique-pr-vllm-ascend-10442
title: "PR Insight: vllm-project/vllm-ascend #10442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - context-parallel
  - kv-cache
  - qwen
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10442"
---

# PR Insight: vllm-project/vllm-ascend #10442

**Title:** [BugFix] fix qwen3.5 accuracy bug when sett cp-kv-cache-interleave-si…

## Overview
This PR fixes an accuracy bug in Qwen3.5 when the `cp-kv-cache-interleave-size` setting is configured to 1024. When block_size > 1024, the block_size in the block_table was set to the kernel block size, causing incorrect slot mapping calculations. This resulted in uneven allocation across cards and precision problems. The fix corrects the block table logic to properly handle cases where the configured interleave size differs from the kernel block size.

## Technical Significance
This is a critical correctness fix for context parallelism with KV cache interleaving. The issue demonstrates the complexity of managing block sizes across different layers of the system: configuration, block table, and kernel interfaces. The mismatch between configured interleave size and kernel block size caused incorrect slot mapping, leading to uneven distribution and precision degradation. The fix ensures proper alignment between these different block size concepts, maintaining correctness across distributed KV cache management.

## Related
- `technique-context-parallel`
- `technique-kv-cache-paging`
- `technique-qwen`