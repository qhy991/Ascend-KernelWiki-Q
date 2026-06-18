---
id: technique-pr-vllm-ascend-6164
title: "PR Insight: vllm-project/vllm-ascend #6164"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mooncake
  - pd-colocation
  - dependency
  - revert
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/6164"
---

# PR Insight: vllm-project/vllm-ascend #6164

**Title:** [Misc] Revert "[Misc] Bump mooncake version to v0.3.8.post1 (#6110)"

## Overview
This PR reverts PR #6110 which bumped the Mooncake version to v0.3.8.post1. The revert was necessary because the new Mooncake version caused Docker image build failures in CI pipelines.

## Technical Significance
Dependency version changes in distributed inference systems like Mooncake can cause build or runtime failures due to API incompatibilities, missing dependencies, or build configuration issues. This revert restores stability by rolling back to a known-good Mooncake version while the build issues are investigated and resolved.

## Related
- `technique-pd-colocation`, `technique-mooncake`, `technique-dependency-management`