---
id: technique-pr-modellink-2767
title: "PR Insight: Ascend/ModelLink #2767"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - bugfix
  - dualpipe
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2767"
---

# PR Insight: Ascend/ModelLink #2767

**Title:** ms_dualpipe_bugfix

## Overview
This PR fixes a bug in the MindSpore dualpipe implementation. The dualpipe mechanism is a performance optimization that overlaps computation and communication, and this fix addresses a specific issue that was causing incorrect behavior during training.

## Technical Significance
This bugfix ensures the dualpipe optimization works correctly for MindSpore workloads on Ascend hardware. Dualpipe is crucial for hiding communication latency during training, so this fix directly impacts training efficiency and stability.

## Related
- technique-pipeline-scheduling
- technique-cube-vector-overlap