---
id: technique-pr-vllm-ascend-7442
title: "PR Insight: vllm-project/vllm-ascend #7442"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - cudagraph
  - performance
  - python-optimization
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7442"
---

# PR Insight: vllm-project/vllm-ascend #7442

**Title:** [Bugfix] Fix slow hasattr in ACLGraphWrapper.__getattr__

## Overview
This PR fixes a performance issue where hasattr(self.model, "flush_pending_metadata") cost ~6ms per decode step. The problem was that CUDAGraphWrapper.__getattr__ raised an AttributeError that triggered __repr__() on the underlying model, recursively traversing the entire nn.Module tree to generate an 18,000+ character string.

## Technical Significance
This fix matters for Ascend inference latency. The 6ms overhead per decode step severely impacted audio inter-chunk latency in multimodal models like Qwen3 Omni. By fixing the hasattr implementation, it eliminates unnecessary string generation overhead, significantly improving decode performance for models with frequent attribute checks.

## Related
- technique-graph-mode
- pattern-performance-optimization