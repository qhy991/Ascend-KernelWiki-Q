---
id: technique-pr-modellink-2481
title: "PR Insight: Ascend/ModelLink #2481"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - dskv3
  - long-stability
  - performance
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2481"
---

# PR Insight: Ascend/ModelLink #2481

**Title:** [core-llm][dskv3]调整长稳脚本，添加性能脚本

## Overview
This PR adjusts long-stability testing scripts and adds performance scripts for DeepSeek V3. Long-stability testing ensures models can train for extended periods without degradation, and performance scripts measure training throughput.

## Technical Significance
Long-stability scripts validate training reliability on Ascend hardware over extended durations. Performance scripts enable benchmarking and optimization of training throughput for DeepSeek V3.

## Related
- long-stability testing
- performance benchmarking