---
id: technique-pr-vllm-ascend-6849
title: "PR Insight: vllm-project/vllm-ascend #6849"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
  - ascend310p
tags:
  - aclgraph
  - decode
  - attention
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6849"
---

# PR Insight: vllm-project/vllm-ascend #6849

**Title:** [300I] support decode-only aclgraph mode

## Overview
Adds decode-only ACL graph mode support for Ascend 310P hardware. The implementation modifies attention components in the 310P-specific code path and utility functions to enable ACL graph execution for decode-only scenarios.

## Technical Significance
Enables efficient decode-only inference on Ascend 310P devices by leveraging ACL graph mode for attention operations. This optimization reduces overhead for generation-heavy workloads where prefill phase is not present or is handled separately.

## Related
- `technique-aclgraph`, `technique-attention`, `technique-decode-optimization`