---
id: technique-pr-sgl-kernel-npu-540
title: "PR Insight: sgl-project/sgl-kernel-npu #540"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - deepep
  - moe
  - code-refactoring
  - pattern-abstraction
confidence: inferred
sources:
  - "https://github.com/sgl-project/sgl-kernel-npu/pull/540"
---

# PR Insight: sgl-project/sgl-kernel-npu #540

**Title:** [DeepEP] refactors Buffer to use strategy abstraction

## Overview
This PR refactors the DeepEP Buffer class to use a strategy pattern abstraction, separating different operational modes into distinct strategy implementations. The normal mode now supports default and all-to-all strategies, while low-latency mode supports default and CANN kernel operations strategies. The refactoring significantly simplifies the core Buffer implementation and improves code maintainability.

## Technical Significance
Applying the strategy pattern to Buffer management improves code organization and makes it easier to add new operational modes or communication strategies. The abstraction layer enables cleaner separation of concerns and reduces code duplication across different DeepEP modes. This refactoring sets a solid foundation for future enhancements and makes the codebase more maintainable and extensible.

## Related
- `pattern-design-patterns`
- `technique-deepep`
- `pattern-code-organization`
- `technique-moe-dispatch`