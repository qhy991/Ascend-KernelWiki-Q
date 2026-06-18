---
id: technique-pr-vllm-ascend-5592
title: "PR Insight: vllm-project/vllm-ascend #5592"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - attention
  - cross-attention
  - whisper
  - encoder-decoder
confidence: inferred
sources:
  - "https://github.com/vllm-project/vllm-ascend/pull/5592"
---

# PR Insight: vllm-project/vllm-ascend #5592

**Title:** [Feature] Support for cross-attention and whisper model

## Overview
This PR adds support for cross-attention in encoder-decoder models and enables Whisper model inference. The implementation modifies attention, platform, and model runner components to handle the different attention patterns required for audio and multimodal tasks.

## Technical Significance
Cross-attention support enables vllm-ascend to handle encoder-decoder architectures like Whisper, expanding the model family support beyond decoder-only transformers. This capability is essential for audio transcription and multimodal tasks that require attending to encoder representations during decoding.

## Related
- `kernel-attention` (Cross-attention kernels)
- `technique-encoder-decoder` (Encoder-decoder architectures)
- `kernel-whisper` (Audio model support)
- `pattern-attention` (Attention pattern variations)