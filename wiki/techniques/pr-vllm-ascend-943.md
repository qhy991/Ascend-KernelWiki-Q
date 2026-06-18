---
id: technique-pr-vllm-ascend-943
title: "PR Insight: vllm-project/vllm-ascend #943"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - scheduler
  - mtp
  - spec-decode
  - disaggregate-prefill
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/943"
---

# PR Insight: vllm-project/vllm-ascend #943

**Title:** [Scheduler][MTP] Add support for speculative decoding in AsecendScheduler.

## Overview
This PR adds support for speculative decoding in AscendScheduler, including partial support for disaggregated prefill (full support in follow-up PR). The implementation enables advanced scheduling features for improved inference throughput.

## Technical Significance
AscendScheduler is the custom scheduler for vllm-ascend. Adding speculative decoding support enables MTP and other advanced scheduling features, while disaggregated prefill support allows separation of prefill and decode phases across different devices for better resource utilization.

## Related
- `kernel-scheduler`
- `technique-spec-decode`
- `technique-disaggregate-prefill`