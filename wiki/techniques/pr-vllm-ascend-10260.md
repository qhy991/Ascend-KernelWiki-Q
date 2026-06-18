---
id: technique-pr-vllm-ascend-10260
title: "PR Insight: vllm-project/vllm-ascend #10260"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - testing
  - configuration
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/10260"
---

# PR Insight: vllm-project/vllm-ascend #10260

**Title:** [EPLB][Test] Change mooncake port

## Overview
This PR changes the Mooncake backend test port from 36000 to 30000 to avoid port occupation issues. The change is made in the EPLB (external pull request long benchmarks) test configuration for the Qwen3-235B-W8A8 model to remain consistent with other use cases and prevent conflicts when the port is already in use.

## Technical Significance
While this is a simple configuration change, it addresses an important testing reliability issue. Port conflicts can cause test flakiness and false failures, especially in continuous integration environments. Standardizing on port 30000 across different test scenarios reduces the likelihood of such conflicts and improves test infrastructure reliability. This is part of maintaining robust testing infrastructure for large-scale inference scenarios on Ascend.

## Related
- `technique-testing`
- `technique-eplb`