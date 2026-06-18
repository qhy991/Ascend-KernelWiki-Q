---
id: technique-pr-samples-593
title: "PR Insight: Ascend/samples #593"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - audio
  - speech
  - atlas.so
  - wav
  - inference
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/593"
---

# PR Insight: Ascend/samples #593

**Title:** modified WAV_to_word with atlas.so

## Overview
This PR modifies the WAV_to_word speech recognition sample to use atlas.so (Ascend dynamic library). The sample demonstrates converting WAV audio files to text using speech recognition models running on Ascend hardware.

## Technical Significance
Integrating with atlas.so demonstrates the proper way to link against Ascend runtime libraries in speech recognition applications. This is important for users building production audio AI systems that need efficient library loading and symbol resolution.

## Related
- Speech recognition
- Audio processing
- atlas.so integration
- Dynamic linking
- WAV processing