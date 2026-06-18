---
id: technique-pr-vllm-ascend-1271
title: "PR Insight: vllm-project/vllm-ascend #1271"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - vllm
  - inference
  - spec-decode
  - acl
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/1271"
---

# PR Insight: vllm-project/vllm-ascend #1271

**Title:** [Bugfix][Spec Decode][0.9.1] Enable `ACL_OP_INIT_MODE=1` directly only when using V0 spec decode

## Overview
This PR backports the speculative decode fix from #1258 to the v0.9.1 branch, ensuring `ACL_OP_INIT_MODE=1` is only enabled during V0 spec decode rather than globally.

## Technical Significance
Maintains consistency between main and maintenance branches for speculative decoding. The fix prevents ACL operator initialization mode from interfering with standard inference by restricting `ACL_OP_INIT_MODE=1` activation to V0 spec decode code paths only. This ensures correct behavior for both speculative and non-speculative decoding in the v0.9.1 release.

## Related
- `technique-spec-decode`
- `technique-operator-fusion`