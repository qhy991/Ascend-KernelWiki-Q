---
id: technique-pr-modellink-2504
title: "PR Insight: Ascend/ModelLink #2504"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - internlm2
  - oom
  - bugfix
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2504"
---

# PR Insight: Ascend/ModelLink #2504

**Title:** fix oom of internlm2

## Overview
This PR fixes out-of-memory (OOM) issues when training InternLM2 models. OOM fixes are critical for enabling large model training within available Ascend NPU memory constraints.

## Technical Significance
OOM fixes enable training of InternLM2 models on Ascend hardware by optimizing memory usage through techniques like activation checkpointing, gradient accumulation, or memory-efficient attention.

## Related
- memory optimization
- InternLM2
- OOM prevention