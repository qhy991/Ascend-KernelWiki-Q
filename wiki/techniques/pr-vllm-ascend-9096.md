---
id: technique-pr-vllm-ascend-9096
title: "PR Insight: vllm-project/vllm-ascend #9096"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - build-system
  - ffn
  - cann-9.0
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9096"
---

# PR Insight: vllm-project/vllm-ascend #9096

**Title:** [BugFix]Fix compile error in dispatch_ffn_combine kernel

## Overview
This PR fixes a build error with CANN 9.0 for the dispatch_ffn_combine kernel by removing header copying and struct patching logic from `csrc/build_aclnn.sh`. The issue was caused by changes in CANN 9.0 that made the previous header manipulation approach incompatible.

## Technical Significance
The fix addresses a critical build system issue that prevented compilation of FFN (Feed-Forward Network) combine operators with CANN 9.0. By removing the problematic header copying and struct patching logic, the build process now works correctly with the updated CANN toolchain, enabling users to build and deploy vllm-ascend with the latest CANN version.

## Related
- `kernel-ffn-ascendc`, `technique-operator-fusion`