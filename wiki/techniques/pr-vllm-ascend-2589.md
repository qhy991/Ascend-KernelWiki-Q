---
id: technique-pr-vllm-ascend-2589
title: "PR Insight: vllm-project/vllm-ascend #2589"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - aclgraph
  - ray
  - tensor-parallel
  - pipeline-parallel
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2589"
---

# PR Insight: vllm-project/vllm-ascend #2589

**Title:** [Feat] allow using aclgraph in ray backend

## Overview
This PR enables the use of ACL Graph in the Ray backend, allowing for tensor parallel + pipeline parallel + ACL Graph configurations in multi-machine deployments. The changes remove platform restrictions that previously prevented this combination.

## Technical Significance
The feature enables advanced distributed inference scenarios by allowing ACL Graph compilation and execution within Ray-based multi-machine deployments. This removal of platform restrictions enables more flexible parallel strategies combining tensor parallelism, pipeline parallelism, and ACL Graph optimization across multiple machines, improving scalability for large model inference.

## Related
- `technique-aclgraph`
- `technique-tensor-parallel`
- `technique-pipeline-parallel`