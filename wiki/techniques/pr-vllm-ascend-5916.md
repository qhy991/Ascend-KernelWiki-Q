---
id: technique-pr-vllm-ascend-5916
title: "PR Insight: vllm-project/vllm-ascend #5916"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - refactor
  - mla
  - sfa
  - code-quality
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5916"
---

# PR Insight: vllm-project/vllm-ascend #5916

**Title:** [Refactor] AttentionBuilder inherit from base class in vllm

## Overview
This PR makes AscendMLAMetadataBuilder and AscendSFAMetadataBuilder properly inherit from the vllm base class by adding super().__init__() calls. It also extracts ascend_chunked_prefill_workspace_size() to avoid code duplication and overrides determine_chunked_prefill_workspace_size() for Ascend-specific 128k token support.

## Technical Significance
Proper Python inheritance with super().__init__() calls ensures parent class initialization logic is executed, reducing code duplication and improving maintainability. The refactor extracts shared functionality and allows Ascend to support 128k token workspace size (vs 64k in the parent class) for chunked prefill. This is part of issue #5463 item 10 and ensures better alignment with vllm's architecture.

## Related
- `technique-mla`, `technique-sfa`, `technique-chunked-prefill`, `technique-code-refactor`