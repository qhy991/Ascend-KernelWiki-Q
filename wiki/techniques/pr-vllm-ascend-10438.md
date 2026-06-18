---
id: pr-vllm-ascend-10438
title: "PR Insight: vllm-project/vllm-ascend #10438"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - bugfix
  - kv-cache
  - logging
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10438"
---

# [20.2][BugFix][KV Pool] Avoid logging KV store keys at error level

**Repository:** `vllm-project/vllm-ascend`  
**PR:** [#10438](https://github.com/vllm-project/vllm-ascend/pull/10438)

## Overview

Demotes KV store key logging from ERROR to DEBUG level, preventing log pollution during normal distributed KV pool operations and reducing false alarm noise in production Ascend deployments.

## Technical Details

This PR targets the `vllm-project/vllm-ascend` project within the Ascend ecosystem. The change tagged as `bugfix` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Bugfix
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
