---
id: technique-pr-vllm-ascend-7926
title: "PR Insight: vllm-project/vllm-ascend #7926"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - 310p
  - ascendc
  - custom-operator
  - fla
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7926"
---

# PR Insight: vllm-project/vllm-ascend #7926

**Title:** [Feature] [310p] Add recurrent_gated_delta_rule_310 AscendC Custom Op

## Overview
This PR adds a new AscendC custom operator `recurrent_gated_delta_rule_v310` to support recurrent gated delta rule calculations on Ascend 310P devices. The implementation includes operator integration into the build system, PyTorch bindings, tiling logic, and the AscendC kernel with support for dynamic block dimensions and optimized memory management.

## Technical Significance
The recurrent gated delta rule is a key operation for Flash Linear Attention (FLA) on 310P devices. Implementing it as an AscendC custom operator enables hardware-optimized execution on 310P rather than relying on generic implementations. The comprehensive tiling infrastructure and end-to-end test suite ensure correctness and enable efficient FLA inference on 310P hardware.

## Related
- `kernel-attention`
- `pattern-fla`
- `technique-ascendc-custom-ops`