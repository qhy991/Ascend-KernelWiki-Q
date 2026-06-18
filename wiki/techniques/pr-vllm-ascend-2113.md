---
id: technique-pr-vllm-ascend-2113
title: "PR Insight: vllm-project/vllm-ascend #2113"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - custom-ops
  - torch.compile
  - meta-registration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2113"
---

# PR Insight: vllm-project/vllm-ascend #2113

**Title:** [core] Support capture custom ops into aclgraph

## Overview
This PR enables torch.compile to capture custom AscendC operations into ACL Graph by registering meta implementations for custom ops like rotary_embedding. The implementation adds meta registration in `vllm_ascend/meta_registration.py`, C++ bindings in `csrc/torch_binding_meta.cpp`, and tests in `tests/e2e/singlecard/ops/test_rotary_embedding.py`, allowing fx graph capture and natural insertion of custom ops into the Ascend runtime ACL graph.

## Technical Significance
This integration is significant for reducing host overhead during ACL Graph inference by allowing torch.compile (torch 2.x) to recognize and capture AscendC custom operations. The meta registration pattern enables the fx graph to understand operator shapes and types during graph capture, making it possible to insert custom ops into aclgraph seamlessly. This enables more efficient graph-mode execution by avoiding Python-level overhead.

## Related
- `technique-aclgraph-integration`, `technique-custom-ops`, `kernel-rotary-embedding-ascendc`