---
id: technique-pr-mindspeed-1722
title: "PR Insight: Ascend/MindSpeed #1722"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - bugfix
  - all-to-all
  - distributed
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/1722"
---

# PR Insight: Ascend/MindSpeed #1722

**Title:** fix: all_to_all consistency in mapping.py

## Overview
This PR fixes a consistency issue in all_to_all operations within the mapping.py module. The bug likely affects how data is mapped or distributed across devices during all-to-all communication.

## Technical Significance
Consistency in all_to_all operations is critical for correct data distribution in MoE and other distributed workloads. Fixing this bug ensures proper token-to-expert mapping and prevents data corruption or incorrect computation on Ascend NPUs.

## Related
- all-to-all communication
- distributed training
- data-mapping