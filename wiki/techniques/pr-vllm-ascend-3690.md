---
id: technique-pr-vllm-ascend-3690
title: "PR Insight: vllm-project/vllm-ascend #3690"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - kv-pool
  - configuration
  - input-formatting
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3690"
---

# PR Insight: vllm-project/vllm-ascend #3690

**Title:** [Feat](Mooncake) Supports multiple input suffixes for global_segment_size

## Overview
This PR enhances Mooncake KV pool configuration by supporting multiple input suffixes (GB, MB, KB, B) for global_segment_size and local_buffer_size parameters. It unifies management using constants and maintains backward compatibility with existing input methods. Changes were made to `vllm_ascend/distributed/mooncake/config_data.py`, test files, and documentation.

## Technical Significance
Flexible input formats improve user experience by allowing intuitive size specifications (e.g., "1GB" instead of 1073741824 bytes). This enhancement makes Mooncake KV pool configuration more user-friendly while maintaining backward compatibility, reducing configuration errors and improving documentation clarity.

## Related
- `technique-kv-pool`
- `technique-mooncake`
- `technique-configuration`