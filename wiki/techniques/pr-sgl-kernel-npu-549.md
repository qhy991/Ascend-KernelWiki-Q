---
id: technique-mxfp8-low-latency-dispatch
title: "MXFP8 Support in DeepEP Low Latency Dispatch"
type: wiki-technique
architectures:
  - ascend910b
kernel_types:
  - moe
tags:
  - mxfp8
  - low-latency-dispatch
  - deepep
sources:
  - pr-sgl-kernel-npu-549
confidence: verified
---

# MXFP8 Support in DeepEP Low Latency Dispatch

## Overview
Optimizing memory footprints during the dispatch phase of Mixture-of-Experts (MoE) is critical. This technique introduces the use of micro-scaling formats like `MXFP8` (`Float8_e4m3fn` and `Float8_e8m0fnu` scales) directly within the MoE buffer distribution kernel `moe_distribute_dispatch_v2`.

## Implementation Details
The `MoeDistributeDispatchV2` operator on Ascend 910B supports direct intake of MXFP8 inputs. By configuring `use_fp8` and `use_ue8m0` under the `__DAV_C310__` architecture flags, the `low_latency_dispatch` buffer allocates `at::kFloat8_e4m3fn` storage natively, reducing the transport volume significantly.

## Trade-offs
- **Pros**: Reduces cross-node or intra-node HBM/communication bandwidth requirements by at least 50% compared to BF16 for expert token routing.
- **Cons**: Requires explicit handling of block scales (`at::kFloat8_e8m0fnu`), which requires additional indexing offsets.
