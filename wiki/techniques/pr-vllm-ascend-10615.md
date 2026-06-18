---
id: technique-pr-vllm-ascend-10615
title: "PR Insight: vllm-ascend #10615"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - ci
  - automation
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10615"
---

# PR Insight: vllm-ascend #10615 - [CI] Remove github action schedule job for image and nightly

## Overview
Pull Request #10615 in the `vllm-ascend` repository addresses an issue with unreliable continuous integration (CI) scheduling for building images and running nightly tests. 

## Context and Changes
The vllm-ascend repository relies on nightly tests and regular image builds to ensure the stability of the Ascend NPU backend. Historically, these processes were triggered via GitHub Actions scheduled jobs.

However, the team observed that GitHub Actions scheduled jobs do not always run reliably or punctually, often causing delays or unpredictable behavior during the CI lifecycle.

To resolve this issue, this PR completely removes the GitHub Action scheduling triggers for:
1. **Image Builds**
2. **Nightly Tests**

Instead of relying on native GitHub Actions scheduling, the team has opted for an alternative, more reliable approach to trigger these scheduled jobs. While the exact alternative external system isn't explicitly detailed in the PR description, the primary change within the repository is the removal of the unstable cron-based triggers from the GitHub Actions YAML workflows.

## Technical Implications
Although this is an infrastructure-focused PR that does not alter any core Ascend operator kernels or vLLM inference logic, it ensures a more predictable and robust CI/CD pipeline. Stable continuous integration workflows are vital for Ascend910/910B environments to consistently test nightly builds and prevent regressions without the unpredictable latency introduced by native GitHub Actions cron delays.
