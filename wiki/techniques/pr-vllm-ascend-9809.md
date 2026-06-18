---
id: technique-pr-vllm-ascend-9809
title: "PR Insight: vllm-project/vllm-ascend #9809"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - kv-transfer
  - mooncake
  - hybrid-connector
  - qwen3.5
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/9809"
---

# PR Insight: vllm-project/vllm-ascend #9809

**Title:** [Feature][P/D] Mooncake Connector Support Hybrid PCP/DCP for QWen3.5

## Overview
This PR adds hybrid PCP/DCP support for QWen3.5 models through the Mooncake Connector. It enables flexible context parallel strategies combining prefill and decode context parallelism for QWen3.5 inference.

## Technical Significance
Enables hybrid context parallel strategies (PCP/DCP) for QWen3.5 models via Mooncake Connector, improving resource utilization and performance. Supports both prefill and decode context parallelism in a unified framework, optimized for QWen3.5 architecture.

## Related
- `technique-context-parallel`, `technique-mooncake`, `pattern-hybrid-parallel`