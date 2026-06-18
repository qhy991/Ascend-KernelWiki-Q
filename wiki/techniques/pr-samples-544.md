---
id: technique-pr-samples-544
title: "PR Insight: Ascend/samples #544"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - presenter-agent
  - arm
  - build-system
  - samples
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/544"
---

# PR Insight: Ascend/samples #544

**Title:** 更新presenter agent的make file 支持arm架构

## Overview
This PR updates the Makefile for the presenter agent to support ARM architecture compilation, enabling the samples to run on ARM-based Ascend hardware platforms.

## Technical Significance
Extends cross-platform compatibility by enabling ARM architecture support, which is important for deploying samples on a wider range of Ascend devices including ARM-based variants.

## Related
- `pattern-cross-platform`
- `pattern-build-system`