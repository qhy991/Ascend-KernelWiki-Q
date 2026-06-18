---
id: technique-pr-vllm-ascend-7518
title: "PR Insight: vllm-project/vllm-ascend #7518"
type: wiki-technique
architectures:
  - ascend310p
tags:
  - vl-models
  - mm-encoder
  - 310p-fallback
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/7518"
---

# PR Insight: vllm-project/vllm-ascend #7518

**Title:** [Bugfix][310p] the new A5 mmencoder op donot support 310p

## Overview
This PR fixes an issue where the new A5 MMEncoder operator prevented 310P from running any VL models. The fix adds conditional logic to disable the new MMEncoder operator on 310P, maintaining backward compatibility.

## Technical Significance
This fix matters for 310P VL model support. The new A5 MMEncoder operator wasn't compatible with 310P hardware, breaking all VL model inference. By detecting hardware and falling back to the previous implementation, it ensures 310P can continue running VL models while 910/910B benefit from the optimized operator.

## Related
- pattern-310p-compatibility
- technique-vl-inference