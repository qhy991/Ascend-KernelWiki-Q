---
id: technique-pr-modellink-2753
title: "PR Insight: Ascend/ModelLink #2753"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - modellink
  - communication
  - performance
  - training
confidence: inferred
sources:
  - "https://gitee.com/ascend/ModelLink/pulls/2753"
---

# PR Insight: Ascend/ModelLink #2753

**Title:** 【master】mindspeed-llm支持零冗余通信

## Overview
This PR adds support for zero-redundancy communication in mindspeed-llm. This communication optimization reduces data movement overhead during distributed training by eliminating unnecessary data transfers between devices.

## Technical Significance
Zero-redundancy communication is a key optimization for distributed training on Ascend NPUs. It reduces HCCL communication overhead, enabling better scaling for large model training across multiple devices and improving overall training throughput.

## Related
- technique-hccl-optimization