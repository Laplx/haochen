---
title: 生成模型
date: "2026-01-22"
weight: 8
tags: ["AI", "CS", "Math", "Stochastic", "Algorithm"]
draft: false
---
{{< katex >}}
## VAE

### Settings and Loss

$$
x \underset{q\_\phi(z|x)}{\xrightarrow{\text{enc.}}} z \underset{p\_\theta(x|z)}{\xrightarrow{\text{dec.}}} \hat{x}
$$

Encoder (approximate posterior): $q\_{\phi}(z\mid x)$\
Decoder (likelihood model): $p\_{\theta}(x\mid z)$

AE: deterministic in $z, \hat{x}$, $f\_\theta$ acts like a corset, $\mathcal{L}\_{\text{recons.}} = \|x - \hat{x}\|^2$

$$
\mathcal{L}=-\mathbb{E}\_{z \sim q\_{\phi}(z\mid x)}\left[\log p\_{\theta}(x\mid z)\right]+\beta \cdot \mathrm{KL}\bigl(q\_{\phi}(z\mid x)\|p(z)\bigr)
$$

(If we do not have this KL term, it becomes stochastic AE.)

The first term is reconstruction negative log-likelihood, e.g. *Cross Entropy* for *Softmax*, *MSE* for *Gaussian*.

Prior:
$
p(z)=\mathcal{N}(0,I)
$

Reparameterized posterior:
$
q\_{\phi}(z\mid x) = \mu\_{\phi}(x) + \sigma\_{\phi}(x)\varepsilon,
\quad
\varepsilon \sim \mathcal{N}(0,I)
$

Thus recons. term can be written as
$$
\mathcal{L}\_{\text{recons.}}=\mathbb{E}\_{\varepsilon}\left[\log p\_{\theta}\bigl(x \mid \mu\_{\phi}(x)+\sigma\_{\phi}(x)\varepsilon\bigr)\right]
$$

The second term:
$$
\beta > 1:
\quad
\text{information bottleneck } I(x;z),
\ \text{(i.e. disentangle)}.
$$

$$
\beta < 1:
\quad
\text{relieve posterior collapse } (q\_{\phi}(z\mid x)\approx p(z)).
$$

### Generative view

Goal:
$$
\begin{aligned}
\max\_{\theta}& \log p\_{\theta}(x)\\\
& =\log \int p\_{\theta}(x\mid z)p(z)dz\\\
& =\log \int\frac{p\_{\theta}(x\mid z)p(z)}{q\_{\phi}(z\mid x)}q\_{\phi}(z\mid x)dz\\\
& \overset{\text{Jensen}}{\ge}\mathbb{E}\_{z\sim q\_{\phi}(z\mid x)}\left[\log p\_{\theta}(x\mid z)\right]-\mathrm{KL}\bigl(q\_{\phi}(z\mid x)\|p(z)\bigr) \triangleq \text{ELBO}
\end{aligned}
$$

Note there is a equation
$$
\log p\_{\theta}(x) = \text{ELBO} + \mathrm{KL}\bigl(q\_{\phi}(z\mid x)\|p(z\mid x)\bigr)
$$

Maximizing ELBO is equivalent to minimizing $\mathrm{KL}\bigl(q\_{\phi}(z\mid x)\|p(z\mid x)\bigr)$.

Because $p\_{\theta}(z\mid x)$ is difficult to compute deu to $\frac{1}{Z}$(by Bayes, $Z \approx p\_{\theta}(x)$), so we use
$q\_{\phi}(z\mid x)$ to approximate it.

### Intuition

$$
\begin{aligned}
\nabla\_{\theta}\log p\_{\theta}(x) & =
\nabla\_{\theta}\log \int p(z) p\_{\theta}(x\mid z)\\\
& = \frac{\int p(z)\nabla\_{\theta}p\_{\theta}(x\mid z)dz}{\bm{p\_{\theta}(x)}}\\\
& = \int p\_{\theta}(z\mid x)\nabla\_{\theta}\log p\_{\theta}(x\mid z)dz
\end{aligned}
$$

Note $\nabla\_{\theta}\log \int p(z) p\_{\theta}(x\mid z)\ge \mathbb{E}\_{z\sim p(z)}\left[\nabla\_{\theta}\log p\_{\theta}(x\mid z)\right]$.

Without an encoder we still cannot obtain $p\_{\theta}(z\mid x)$, then introduce $q\_{\phi}(z\mid x)$.

The gap is two KL terms: $\mathrm{KL}\bigl(q\_{\phi}\|p\_{\theta}(z\mid x)\bigr)-\mathrm{KL}\bigl(q\_{\phi}\|p(z)\bigr)$.
