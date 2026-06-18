---
id: technique-pr-vllm-ascend-3770
title: "PR Insight: vllm-project/vllm-ascend #3770"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - mtp
  - documentation
  - developer-guide
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/3770"
---

# PR Insight: vllm-project/vllm-ascend #3770

**Title:** add mtp doc

## Overview
This PR adds developer documentation for MTP (Multi-Token Prediction), creating a new 112-line file `docs/source/developer_guide/feature_guide/Multi_Token_Prediction.md` and updating the feature guide index. The documentation covers MTP development usage and implementation details.

## Technical Significance
Comprehensive documentation is essential for enabling developers to understand and use advanced features like MTP. This guide provides the necessary information for implementing MTP in custom models or understanding how the spec decode mechanism works with multi-token prediction, improving community adoption and contribution quality.

## Related
- `technique-mtp`
- `technique-spec-decode`
- `technique-documentation`