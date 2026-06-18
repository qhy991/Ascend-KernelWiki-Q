---
id: technique-pr-vllm-ascend-10646
title: "PR Insight: vllm-project/vllm-ascend #10646"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - doc
  - release
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10646"
---

# PR Insight: vllm-project/vllm-ascend #10646 - [Doc][Misc] Update release config for v0.21.0rc1

## Overview

This pull request updates the documentation configuration metadata and version substitutions in `docs/source/conf.py` specifically for the `v0.21.0rc1` release candidate of `vllm-ascend`.

## Changes

- **Documentation Configuration**: Modifies `docs/source/conf.py` to correctly reflect the `v0.21.0rc1` version in the release metadata.
- **Version Substitutions**: Updates version numbers used within the Sphinx documentation generation to align with the new release candidate.

## Architectural & User Impact

- **User-Facing Changes**: None. This is strictly a documentation configuration update and does not impact the vLLM engine's runtime behavior, hardware architecture usage (such as Ascend 910/910B), or user-facing APIs.
- **Testing**: No test runs were required, as the change only updates static documentation metadata.
- **Base Versioning**: This PR is built around the `v0.21.0` release lineage, syncing with upstream vLLM core commit `9090368b650896bf5fc990c921df7eb4c20355a5`.
