---
title: Meta RL
date: "2026-01-13"
tags: []
draft: false
---
{{< katex >}}

> 部分内容亦可参考[强化学习笔记](../../notes/reinforce-learn/#7-meta-rl)

标准的 RL 针对于特定的 MDP 环境利用学习算法求解一个策略。Meta-RL 则希望能够迅速适应不同新任务并得到相应的最优策略，即我们要确定（学习）一个良好的学习算法（learn to learn）。

当然，从形式逻辑上我们还是可以将 Meta-RL 放入 RL 的框架，后面各类求解方式确实与 RL 无异，但这一概念主要强调了在直观上的短时学习性，这也是现在 AGI 非常关注的能力。另一个有些类似的是上下文学习 ICL，但注意到 ICL 更多需要模型自行思考给定任务，而不能通过交互的方式探索和在线学习策略。

Meta-RL 的基本假设是用于 meta-training 的老任务与 meta-testing 的新任务服从同一任务分布 $p(\mathcal{T})$，基本问题可以表述如下：
$$
\min \_{\boldsymbol{\theta}, \psi} \mathbb{E}\_{\mathcal{T} \sim \rho(\mathcal{T})}\left[\mathcal{L}\left(\mathcal{D}\_{\mathcal{T}}^{\text {test }}, \theta^{\prime}\right)\right] \quad \text { s.t. } \quad \theta^{\prime}=u\_{\psi}\left(\mathcal{D}\_{\mathcal{T}}^{\text {tr }}, \theta\right)
$$

其中 $\mathcal{D}\_{\mathcal{T}}^{\text{tr}}, \mathcal{D}\_{\mathcal{T}}^{\text{test}}$ 为某采样任务得到的训练集和测试集。s.t. 的部分就是利用较小的数据（$\mathcal{D}^{\text{tr}}\_{\mathcal{T}}$）即时适应该任务的过程，称作 **inner loop**；在各任务上实行学习算法，得到最终的平均损失（用以更新 Meta-RL 参数）的过程称作 **outer loop**。（还有一对文章爱用的词是 'fast' and 'slow'。）

（ICL 也可被这样刻画，不过如前所述，Meta-RL 多为交互得到数据，考察每个 inner loop 的平均损失，因此不区分 $\mathcal{D}\_{\mathcal{T}}^{\text{tr}}$ 和 $\mathcal{D}\_{\mathcal{T}}^{\text{test}}$。）

不同 Meta-RL 算法的区别自然在于内学习过程 $\theta'=\mu_{\psi}(\mathcal{D}^{\text{tr}}_{\mathcal{T}},\theta)$ 的具体实施形式。当前的 Meta-RL 算法大致可以分为两大类，第一类基于 gradient，第二类是基于 context。**gradient-based** 以策略梯度为基础，内学习过程为梯度上升的类型；**context-based**(recurrence-based) 基本暗含了对任务进行推断的过程，$\theta$ 常包含从历史样本中推断得到的 latent variables 用于表示对具体哪个任务的推断信息，因此许多算法都采用如 RNN 或 VAE 结构来编码历史经验。

## Gradient-based
### MAML


### MAESN


## Context-based
### RL^2


### PEARL


### PEARL


### VariBAD


### MQL


### FOCAL


## Offline and Off-Policy in Meta-RL

