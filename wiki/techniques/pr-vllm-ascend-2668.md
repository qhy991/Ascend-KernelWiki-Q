---
id: technique-pr-vllm-ascend-2668
title: "PR Insight: vllm-project/vllm-ascend #2668"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - spec-decode
  - refactor
  - modularity
  - eagle-proposer
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2668"
---

# PR Insight: vllm-project/vllm-ascend #2668

**Title:** [Refactor] Refactor Spec Decode

## Overview
This PR refactors the spec decode implementation to reduce coupling between spec decode and model runner components. The refactoring clarifies and separates responsibilities, creating a more modular design with focused component roles.

## Technical Significance
The refactoring significantly improves code maintainability by reducing interdependence between spec decode and model runner. Key changes include moving proposer implementations to dedicated modules (eagle_proposer.py: 642 new lines, mtp_proposer.py: 209 new lines), creating clear interfaces, and removing 400 lines from model_runner_v1.py. This enhances modularity and long-term maintainability.

## Related
- `technique-spec-decode`
- `technique-eagle-proposer`
- `technique-refactor`