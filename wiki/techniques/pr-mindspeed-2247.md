---
id: technique-pr-mindspeed-2247
title: "PR Insight: Ascend/MindSpeed #2247"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mindspeed
  - enable-recompute
  - layers-per-pp-rank
  - refactor
  - parameter
confidence: inferred
sources:
  - "https://gitee.com/ascend/MindSpeed/pulls/2247"
---

# PR Insight: Ascend/MindSpeed #2247

**Title:** refactor: enable_recompute_layers_per_pp_rank 参数重构

## Overview
This PR refactors the enable_recompute_layers_per_pp_rank parameter. This parameter controls how many layers to recompute per Pipeline Parallelism (PP) rank, trading compute for memory efficiency.

## Technical Significance
Refactoring this parameter improves code clarity and configuration management. Proper recompute layer selection is crucial for memory optimization during pipeline parallel training. The refactor may include better validation, clearer naming, or improved integration with the configuration system.

## Related
- `technique-activation-recompute`
- `technique-pipeline-scheduling`
- `pattern-configuration-management`
- `pattern-parameter-refactoring`