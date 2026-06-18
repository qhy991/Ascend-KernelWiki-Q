---
id: pr-vllm-ascend-10632
title: "PR Insight: vllm-project/vllm-ascend #10632"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - infrastructure
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10632"
---

# [CI] Move from github runner to self-host runner to speed up CI

**Repository:** `vllm-project/vllm-ascend`  
**PR:** [#10632](https://github.com/vllm-project/vllm-ascend/pull/10632)

## Overview

Migrates CI from GitHub-hosted runners to self-hosted runners to reduce job queue times and improve build/test throughput for the Ascend NPU CI pipeline.

## Technical Details

This PR targets the `vllm-project/vllm-ascend` project within the Ascend ecosystem. The change tagged as `ci` improves the overall reliability and usability of the NPU software stack.

## Impact

- **Scope:** Ci
- **Risk:** Low
- **Architectures:** Ascend 910, Ascend 910B
