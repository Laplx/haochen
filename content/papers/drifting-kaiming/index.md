---
title: Drifting Models Performing Single-Step Generation
date: "2026-02-14"
tags: []
draft: true
---
{{< katex >}}

## Generative Modeling via Drifting

Mingyang Deng, He Li, Tianhong Li, Yilun Du, Kaiming He 2026.2

> Generative modeling can be formulated as learning a mapping $f$ such that its pushforward distribution matches the data distribution. The pushforward behavior can be carried out iteratively at inference time, for example in diffusion and flow-based models. In this paper, we propose a new paradigm called Drifting Models, which evolve the pushforward distribution during training and naturally admit one-step inference. We introduce a drifting field that governs the sample movement and achieves equilibrium when the distributions match. This leads to a training objective that allows the neural network optimizer to evolve the distribution. In experiments, our one-step generator achieves state-of-the-art results on ImageNet at 256$\times$256 resolution, with an FID of 1.54 in latent space and 1.61 in pixel space. We hope that our work opens up new opportunities for high-quality one-step generation.

### Question


### Method


### Key-Idea


### Comments

