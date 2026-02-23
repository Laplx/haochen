---
title: "Attempts at Symmetry in Game Theory"
date: "2024-08-02"
weight: 6
tags: ["Game", "Math", "Galois"]
draft: false
---
{{< katex >}}
### 关于对称性的类比尝试

讨论的对象仍然是博弈。起因是我看到国自然基金的 Fundamental Research 发了一篇用群论研究博弈论当中对称性的文章[^1]，小吃一惊，原来已经有一少部分人关注这个想法了，于是连忙把自己许久以前想过的冷饭翻出来硬炒。

我将引入准则 $C(G,\tau): \mathbb{S} \rightarrow 2^{\mathbb{S}}$，为一集值函数，以表示在给定某一策略下在某节点该参与者认可的最优策略集合（常见有 $(r)$、$(rB)$ 等，具体前摇可参考我的 Game Theory 笔记）。其在策略空间 $\mathbb{S}$ 上作用的稳定集 equilirium 即 $\Pi\_C=\\{S\in \mathbb{S}|S\in C(G,\tau;S),\forall \tau \in \mathscr{T}\\}$。我们还可以对准则函数进行一系列变换，以方便各方面如对动态博弈的研究；常用的算子包括均衡算子 $\Pi/\text{Eq}$、上/下序贯算子（分别向下/上节点至支付/根节点取交集）$\text{S}^\text{q}\_iC(G,\tau)=\bigcup\limits\_{\tau^\prime\in\tilde{\tau},\rho(\tau^\prime)=i}C(G,\tau^\prime),\text{S}\_{\text{q}i}C(G,\tau)=\bigcup\limits\_{\tau\in\tilde{\tau^\prime},\rho(\tau^\prime)=i}C(G,\tau^\prime)$、一致算子（严格序贯）$\zeta\_i=\text{S}^\text{q}\_i \text{S}\_{\text{q}i}, \zeta=\zeta\_1\cdots\zeta\_m$、排除算子 $\delta$（剔去某些选择最优的可能性）、边缘算子 $\partial$（取像单纯复形的边界）。$\zeta C$ 一定是序贯/一致准则。特别提及一致反应准则（总准则） $\mathscr{R}C=\bigoplus\limits\_{i\in\\{1,\cdots,m\\}}p\_i\cdot\zeta C$（$p\_i$ 为对参与者 $i$ 策略子空间的投影），接下来的 $C$ 均指总准则。依照其像的关系和操作我们还可称 $C\_1\subset C\_2$ 若 $\forall S, C\_1(G,S)\subset C\_2(G,S)$，即 $C\_1$ 是 $C\_2$ 的精炼；合并（且/或）准则 $C\_1\cup C\_2$、$C\_1\cap C\_2$（或写 $C\_1C\_2$），且有 $\Pi\_{C\_1\cap C\_2}=\Pi\_{C\_1}\cap \Pi\_{C\_2}$ 等；同胚准则 $C\_1(G\_1)\cong C\_2(G\_2)$ 若 $\exists \text{ homeo. }\phi :\mathbb{S}\_1\rightarrow \mathbb{S}\_2$$\text{ s.t. }\forall S\_1,\phi|\_{C\_1(G\_1,S\_1)}\text{ is a homeo. onto }C\_2(G\_2,\phi(S\_1))$。注意准则同样可被视为算子，作用于平凡算子 $(1)$ 上（$\Pi\_1=\mathbb{S}$），再如 $rC$ 即表示对原本的 $C$ 取符合纳什理性选择的交集。

众所周知，域扩张的 Galois 理论和覆叠空间有着良好的对应；这里同样希望类比使用这一成果，定义某准则 $C$ 的策略空间 $\Pi\_c$-自同构组成的群 $\text{Aut}\_C(\mathbb{S})$（注意到 $\sigma \Pi\_C=\Pi\_C$，均衡集为轨道类的集合），当 $\text{Stab}(\text{Aut}\_C)=\Pi\_C$ 时称其为 Galois 准则/算子或正规算子 $\psi$，记 $\text{Gal}(C/1)$。于是有这一对应：

$$
\text{\\{ intermediate criteria of }C\text{ \\}} \underset{\text{Stab}}{\overset{\text{Deck}}{\rightleftarrows}} \text{\\{ subgroups of }G\_C\text{ \\}}
$$

$C$ 为 Galois 准则，中间准则 $\Pi\_{C^\prime}\supset \Pi\_C$ 有 $G\_{C^\prime}<G\_C$；$G\_{C^\prime}\triangleleft G\_C$ 时 $C$ 亦为 $C^\prime$ 的 Galois 精炼/收缩；$C\_1\triangleleft C\_2,|\text{Gal}(C\_1/C\_2)|=[\Pi\_{C\_2}:\Pi\_{C\_1}]$。

$\text{Stab}\circ\text{Deck}=\text{id}$ 要求 $C^\prime$ 正规；$\text{Deck}\circ\text{Stab}=\text{id}$ 鉴于连通空间下两个群作用有公共点可推出两者相同，故自动成立，而离散 $\mathbb{S}$（如只分析纯策略或玩家集合）还需要该子群满足一些“充分/完全”或者说“极大”的条件，即 $H<G\curvearrowright X, \text{each group member } g\in G$$\text{ satisfying } g(x) \sim\_H x, \forall x\in X \text{ is a membe of }H$。（例如点阵的平移可以对每个点实现镜面对称的效果，但这个操作理应纳入子群中。）这便是 FR 那篇 paper 中给到的 "covering group" 的概念。

该篇作者在前期研究[^2]中定义了三类对称博弈，称作（逐步变广）ordinary symmetric games、renaming symmetric games (newly defined by the author)、name-irrelevant symmetric games（显然 $(r)$ 在某些博弈里是正规的，而另外一些不是）。

其文核心就是利用 “covering group”（但这个概念是由 Peleg et al. 的两篇博弈对称性研究率先使用[^3]）给出这几种对称在玩家和动作空间群作用的等价表示。（里面大部分证明都算非常 trivial 的工作）一方面这个工作的本质上面已经阐述过了，同时仅对玩家集合或各玩家行动空间的对称性研究可完全被上面对整个策略空间的讨论所包含。文中所展望的非完全信息在这里几乎没什么新鲜，借助序贯性等性质辅助在 $\mathbb{S}$ 上讨论即可，如果需要关注先验自然手的行为则可以在 $\mathbb{S}\_r$ 上展开。

接下来我给出一个 Nash 准则的基本**分解定理**：

$$
r\cong (\bigcup\limits\_i \partial^{n\_i}\psi\_i)\delta
$$

即（$\forall G,\exists G^\prime$）理性准则总是剔除某些战略并分解为若干正规准则的边缘化。证明需要使用奇数定理，可能还有一些技术性的细节。此领域研究一个重要的逻辑本是众人认为对称性高的结果越容易形成；故以上或许对于我们理解完全理性的实现有所帮助。

这篇内容几乎不含有任何 substantial 的考察。


[^1]: Cao, Zhigang and Li, Guopeng and Tan, Zhibin and Yang, Xiaoguang, On Group Structures of Strategic-Form Games (June 28, 2022). Fundamental Research, Available at SSRN: https://ssrn.com/abstract=4148397
[^2]: Cao, Zhigang and Yang, Xiaoguang, Symmetric Games Revisited (June 17, 2018). Mathematical Social Sciences, Forthcoming, Available at SSRN: https://ssrn.com/abstract=2637225
[^3]: Peleg, Bezalel & Sudholter, Peter & Rosenmuller, Joachim. (1996). The Canonical Extensive Form of a Game Form - Part I - Symmetries. Bielefeld University, Institute of Mathematical Economics, Working Papers. 8. 10.1007/978-3-662-03750-8\_22. 