---
title: 大模型与统计力学
date: "2025-11-18"
weight: 2
tags: ["AI", "Math", "Model", "Statistical Mechanics"]
draft: false
---
{{< katex >}}

> 我希望把平衡态和非平衡态统计力学的一些思路和结论平移到大模型的训练上，以解释 Scaling Law、涌现等现象，会持续补充内容。

假设外界环境由数据集定义，样本量对应温度，在此温度下的动力学由训练方法确定，平衡态为经该样本量训练得到的最佳模型。

$$
\arg\min_{\theta\in \Theta}\int L(x,\theta)d\hat{F}(x) \triangleq \hat{\theta}\\\
\int L(x,\hat{\theta})dF(x) \triangleq \mathcal{L}
$$

其中 $\hat{F}$ 为采样 cdf，样本量记 $m$。定义 $S(\theta,x)\triangleq \frac{\partial L(x,\theta)}{\partial \theta},\ S(\theta)\triangleq \mathbb{E}S(\theta,x)$.

由 CLT 有
$$
\frac{1}{m}\sum\lim_{i=1}^m S(\theta,x_i) \overset{\text{a.}}{\sim} \mathcal{N}(S(\theta_0),\frac{1}{m}V(S(\theta_0,x)))
$$

同时将损失 Taylor 展开
$$
\mathcal{L} -\mathcal{L}_{\min} \overset{\text{a.}}{\sim} \frac{\mathbb{E}\frac{\partial^2 L(x,\theta)}{\partial \theta^2}}{2} (\theta-\theta_0)^2
$$

可以得到**损失服从一个 Gamma 分布** $\mathcal{L} -\mathcal{L}_{\min} \overset{\text{a.}}{\sim} \text{Gamma}(\frac{1}{2},\beta)$，其中
$$
\beta = m \frac{\mathbb{E}\frac{\partial^2 L(x,\theta)}{\partial \theta^2}}{\mathbb{E}(\frac{\partial L(x,\theta)}{\partial \theta})^2}
$$

（可将 $m$ 类比为 $\frac{1}{T}$，第二项为 $\frac{1}{k}$）

由此得到配分函数等一众性质：

$$
Z(\beta)=\sqrt{\frac{\pi}{\beta}}\\\
<\mathcal{L}> = \frac{1}{2\beta},\ <\Delta \mathcal{L}^2>=\frac{1}{2\beta^2}\\\
C_T=\frac{k}{2},\ S=\frac{k}{2}\ln \frac{\pi e}{\beta},\ F=-\frac{1}{2\beta}\ln \frac{\pi}{\beta}
$$

下面讨论近平衡态下的涨落耗散定理。
