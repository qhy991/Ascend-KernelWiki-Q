---
id: technique-pr-samples-1499
title: "PR Insight: Ascend/samples #1499"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - samples
  - gaze-estimation
  - edge-inference
  - atlas200dk
  - university-contribution
  - northwestern-polytechnical-university
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1499"
---

# PR Insight: Ascend/samples #1499

**Title:** 【西北工业大学】基于Atlas200DK的视线估计项目

## Overview
This PR adds a gaze estimation project for the Atlas 200DK edge device contributed by Northwestern Polytechnical University. Gaze estimation predicts where a person is looking from face/eye images.

## Technical Significance
Gaze estimation is a key computer vision task for human-computer interaction, driver monitoring, and accessibility applications. Deploying on Atlas 200DK (edge device) demonstrates optimization techniques for constrained compute/memory environments, relevant to real-time edge inference scenarios.

## Related
- `technique-edge-inference`
- `technique-gaze-estimation`
- `technique-model-optimization`
- `hw-unified-buffer`
- `hw-l1-buffer`