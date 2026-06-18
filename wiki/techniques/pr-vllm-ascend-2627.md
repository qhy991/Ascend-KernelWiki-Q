---
id: technique-pr-vllm-ascend-2627
title: "PR Insight: vllm-project/vllm-ascend #2627"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - quantization
  - moe
  - bugfix
  - mixed-precision
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/2627"
---

# PR Insight: vllm-project/vllm-ascend #2627

**Title:** [main] [bugfix] Fix misjudging quantized/unquantized scenarios

## Overview
This PR fixes a bug where quantized computation was incorrectly used in mixed-precision scenarios when MoE needed to perform unquantized computation. The issue occurred because `quant_config` being non-None didn't necessarily mean quantized computation should be used.

## Technical Significance
The fix moves `with_quant` logic into the forward function to prevent misjudgment in mixed-precision scenarios. By ensuring MoE operations use the correct computation mode based on actual requirements rather than configuration presence, the PR resolves correctness issues in mixed-precision inference workflows.

## Related
- `technique-quantization`
- `technique-moe`
- `technique-mixed-precision`