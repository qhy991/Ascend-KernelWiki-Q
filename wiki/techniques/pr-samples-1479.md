---
id: technique-pr-samples-1479
title: "PR Insight: Ascend/samples #1479"
type: wiki-technique
architectures:
  - ascend910
  - ascend910b
tags:
  - samples
  - stargan
  - generative-models
  - image-synthesis
confidence: inferred
sources:
  - "https://gitee.com/ascend/samples/pulls/1479"
---

# PR Insight: Ascend/samples #1479

**Title:** add new StarGAN sample

## Overview
This PR adds a StarGAN (Star Generative Adversarial Network) sample. StarGAN is a generative model for image-to-image translation tasks, capable of learning mappings between multiple domains.

## Technical Significance
Generative models like StarGAN are computationally intensive and benefit significantly from NPU acceleration. This sample demonstrates how to deploy GAN-based models on Ascend, including handling multiple domain mappings, conditional generation, and managing the generator and discriminator networks.

## Related
- `technique-generative-models`
- `technique-image-synthesis`
- `technique-gan`
- `kernel-convolution`
- `kernel-transposed-convolution`