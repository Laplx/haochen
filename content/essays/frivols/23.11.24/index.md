---
title: "Model for the Nations"
date: "2023-11-24"
tags: ["Model", "Society", "Economy"]
draft: false
---
{{< katex >}}
### 国际关系模型

我想依葫芦画瓢构建一个类似于凯恩斯框架下的简单模型去描述国际关系，方法就是把最原始的宏观经济模型稍作无厘头的扩展。$r\_{ij}$ 表示国家 $i$ 和国家 $j$ 的国际出清关系（International Clearing Relationship，ICR），$r$ 越大（姑且作一标量）关系越正面。（这也许可以计量，比如通过文本分析和情感分析，可以构造并量化国家之间官方媒体互相报道或高层互动事件的一个关系指数）

我们要多引入一些将被考虑的内生和外生变量，它们有一些类似于模块化拼装，可以纳入也可能在考察后认为不足轻重而舍去。除了熟知的 $Y$ 产出、$A$ 技术（这里将科教研究水平与技术合一视之了）、$C$ 消费、$P$ 价格水平、$T$ 税收（及其它强制扭曲）等总量以外，我们还有 $D$ 文化富合度（Cultural Affluence）（正面反映了闲暇和文娱时间；同时负向描述了种族、宗教冲突的程度）、$W$ 民众福利（Welfare）、$M$ 武装力量（Millitary Power）、$U$ 意识介度（Consciousness Dissemination）（指出社会意见和思想的传播程度或多元程度；同时一定的反映政权或宣传机器的把控力量）等。还要介绍的有 $ID$ 政治位移（Ideology），不称意识形态的原因是它可以不仅仅是衡量左右，而是一个可以在设定的多个意识评价标准下的多维空间里移动的一个矢量，其决定了政治和经济制度，特别反映在产权组织 $PI(ID)$ 上（跟政府架构等有关，但核心归于 $ID$）。$PI$（Property Inequality）将政治光谱（空间）划分开来（或连续化），表示了“生产关系”（比如可以粗分为资本主义、社会主义等）及其导致的分配关系。再如 $U$ 应该也与 $ID$ 有关。

模型的假设（缺陷）包括：

- 市场化（may not be free markets but there must exists an adjusting power not controlling）
- 不考虑预期，且无理性预期（no long-term expectation）
- 仅宏观政策（macroscopic open actions 即没有微观或暗面的操作，如针对个别企业的制裁或间谍行为）
- 无随机扰动（no stochastic terms 不包含概率成分，没有影响国际关系的黑天鹅事件）
- 不考虑能源、移民、生态环境等其他重要因素（only has political interest and economic interest / no key mesoscopic factors 不考虑关键中观领域的作用）
- 无阶层分化（no hierarchy 尽管有 PI 且纳入了分配结构，但并未分群体建模）

影响国家决策的无非是两个方面：一边讲发展，一边要安全（就像投资决策的 $\mu$ 和 $\sigma$ 那样）。或者说，国际关系无非是 Benefit 和 Security 的综合作用（Inner & Outer）。不过我们这里要把原来的 IS-LM-BP model 说的详细一些，把 $NX$ 拆开写为 $NX\_{ij}(e\_{ij},Y\_i,Y\_j,r\_{ij})$ 表示 $i$ 国向 $j$ 国的净出口。即有 $NX\_{ij}(e\_{ij},Y\_i,Y\_j,r\_{ij})$ $=$ $KF\_{ij}(i\_i,i\_j,K\_i,K\_j,r\_{ij})$。注意实际上我们应分写进口 $IM$ 和出口 $EX$ 函数，鉴于双向大量贸易和几乎不贸易在净值上无法区别。总而言之：

$$
Y(L,K,A) = C(Y,\dot{Y},i,T,PI) + I(i,T) + G + NX \tag{IB}
$$

$$
NX(e,Y,r,T) = KF(i,K) \tag{OB}
$$

$$
PO(U,D,W,G\_{S},ID) = RE(T,G,Y) \tag{IS}
$$

$$
DT(M,\epsilon,r,ID) = M(G\_M,A) \tag{OS}
$$


其中政府开支（外生，但准确来说应受到 $PI$ 制约）$G = G\_N + G\_M + G\_A + G\_D + G\_{S} + G\_O$ ，包括民生、军备、科技、文化、治安及其他不纳入模型的经常性开支 $G\_O$（建设性投资等资本积累已计入 $I$ 中）。$DT$ 即 Deterrence 他国的威慑作为外部安全的需求函数；$\epsilon\_{ij}$ 为地缘因子 Geographic factor，表示相互军事力量的威胁程度（当有海外军事基地部署时，$\epsilon\_{ij} \neq \epsilon\_{ji}$）（“一切政治首先是地缘政治”）；$\lVert ID\_i-ID\_j \rVert$ 为可能存在的非主要影响因素。$PO$ 即 Public Order 为内部安全供给，受到包括群众福利在内的多变量影响；$RE$ 即 Regime Exertion 公权力的行使，准确来说应写为各不同部分收支的函数（拆分 $G$、$T$，如转移支付、价格管制等），表示内部安全需求。


ICR 需要各国的利益与安全同时出清。

当然，我们还可以纳入增长，要为其他几个变量刻画动态，完善方程组：

$$
\frac{MS}{P} = LQ(i,Y,e,\dot{P}) \tag{LM}
$$

$$
W(C,U,D) = WA(Y,PI,G\_N) \tag{SW}
$$

分别代表了流动性均衡与社会福利均衡。（$MS$ 为货币供给。$WA$ 为 Wealth Allocation 财富分配，以提供福利；同时我们默认储蓄对福利的增量很小）其实应设计要素均衡 $(PF)$，如劳动力所有者收入。

$$
\begin{equation}
\tag{XG}
    \begin{split}
    & \dot{L} = \dot{L}(\dot{Y},\dot{P},L,N,D)\\\
    & \dot{K} = I + KF - \delta\_K K\\\
    & \dot{A} = \dot{A}(G\_A,I,L,A)\\\
    & \dot{N} = \dot{N}(\dot{W},N,\delta\_N)\\\
    & \dot{D} = \dot{D}(G\_D,I,N,D,U)
    \end{split}
\end{equation}
$$

（其中 $\delta\_K$ 为资本折旧率，$\delta\_N$ 为死亡率。$(XG)$ 增长部分等式并未严谨考量变量）

以上各函数关于各变量偏导的符号自行推断（因此可假设一些简单的数学形式）。篇幅有限（欢迎来讨论 $D$ 和 $U$ 这些变量的问题），就不介绍实例了。（不妨看看朝鲜半岛？这个模型告诉我们会出现南北分立的 buffer contries 吗）

如果你愿意的话，可以叫它 “Chen Model” 或者 BIOS（笑）。

### 国际关系续论

模型的基本假设在前一篇已经尽力列举过了。

先来补充说明一个 Scenario：Garrison \& Blocs。我们假设最简单的形式 $DT\_i = \sum \limits\_j \epsilon\_{ij} M\_j f(R\_{ij})$，一般情况 $f^\prime(R\_{ij}) < 0$。而对于海外驻军的情况，$\epsilon\_{ij} < 0$ 且 $\frac{\partial DT\_i}{\partial M\_j} < 0$，$- f^\prime(R\_{ij}) = \frac{\partial^2 DT\_i}{\partial M\_j \partial R\_{ij}} < 0$。注意我们这里有一个未提及的假设：战略威胁可以被视作点对点，不考虑军队在国土空间的分布（比如俄罗斯西线和远东）。

我们把 $\epsilon f(R)$ 合并为一项系数，并把多国作为一个向量，则有 $\mathcal{E} M = M$。可见最终的 $M$ 位于地缘关系矩阵 $\mathcal{E}$ 的特征方向。 如果威慑可分（$\mathcal{E}$ 各列加和等于1），那么 $\mathcal{E}$ 为马尔可夫矩阵。$(OS)$ 式的动态演进（$M\_{n+1} = \mathcal{E} M\_{n}$）将会收敛到该矩阵最大（$\lambda = 1$）的特征向量上。

驻军往往是国际间阵营的体现，应纳入这一安全的延拓性。即 $DT\_i(M\_j,\epsilon\_{ij},r\_{ij},DT\_j,ID\_i,ID\_j)$，本国的外部安全供给会受到他国 $DT$ 的影响。同样，内部安全供给也会受到本国（甚至外国）$DT$ 的影响（攘外安内，危机或战时领导人支持率通常会飙升；当然，避战、反战等主流民意下应为负相关 $\frac{\partial PO\_i}{\partial DT\_i} < 0$）。

接下来让我阐明完整的国际关系模型：

国际出清关系 $R\_{icr}$ 满足 $(IB)\ (OB)\ (IS)\ (OS)$ 四式，且可附加 $(LM)\ (SW)\ (PF)$ $+$ $(XG)$ 各组件的均衡和增长关系。$R\_{icr}$ 是一个对称矩阵，而我们“观测”到的实际国际关系 $R$ 不一定满足 $R\_{ij} \neq R\_{ji}$。

真实的国际关系围绕国际出清关系 ICR 粘性地波动。

大跨度来看国际关系的走势反映了出清关系的调整（长期趋势分析），小跨度下的周期性或非周期性变动反映了国际环境里不确定性的冲击。

记 $r = R - R\_{icr}$。放开无随机的假设，IOBS 方程组参数的扰动将带来 $r$ 的随机波动。粘性来源于诸如反对派、民族主义、右翼势力的声音，我们将其反映为一摩擦项 $\eta \dot{r}$。仿照 Langevin 方程有

$$
\ddot{r} + \eta \dot{r} + \Omega^2 r = \delta(t)
$$

其中 $\delta(t)$ 为无规力。涨落耗散定理（Fluctuation-Dissipation Theorem）告诉我们（$\langle \rangle$ 表示时间平均）

$$
\langle \delta^2(t) \rangle = \eta \langle \dot{r}^2 \rangle
$$

类似 Einstein 的手法换元 $\langle r^2 \rangle$，可以得到 $\Omega^2 \langle r^2 \rangle = \langle \dot{r}^2 \rangle$，即

$$
\langle \delta^2(t) \rangle = \eta \Omega^2 \langle r^2 \rangle
$$

（事实是二战后的世界经历了 $(XG)$ 式所描述的指数的增长，同时政治格局和地区战争动荡不止——我们不敢确信一定存在可趋近的平衡分布，很可能没有足够的摩擦来抑制这些噪声的加热。但作为一个谐振子，我们确信存在了成立的稳态解（形式类似正则系综），那么其满足涨落耗散定理。）

我们把这个首一式子乘回来，右边仍然称作 $\delta(t)$：

$$
\frac{1}{\gamma}\ddot{r} + \zeta \dot{r} + \rho r = \delta(t)
$$

其中 $\gamma$ 称作 $implementary$ $factor$ 执行度；$\zeta$ 称作 $conservative$ $factor$ 保守度；$\rho$ 称作 $progamatic$ $factor$ 务实度。（自行揣摩意义）

这里有一个 scale 可以由 $\delta$ 来敲定。那么如何计量随机冲击的大小呢？我提一种可能的方式：利用舆情分析、文本分析，比较两国主流媒体（鉴于官方与民间存在分别，可以考察媒体的资方或实控方以判断是否接近官方的态度）对同一件事（必须为不改变利益和安全逻辑的非重大事件）报道的相似度（内容、情感倾向等），并按双方的传播热度进行加权。相似度接近1的有正向冲击，接近0的有负向冲击。

代入 $\eta$、$\Omega^2$，前式可写为

$$
\sigma^2 = \frac{T}{\zeta \rho}
$$

$\sigma^2$ 即 $\sigma^2\_r = \langle r^2 \rangle$ 国际关系变动的方差。$T = \langle \delta^2(t) \rangle$ 称作 Heat 热度（温度也可以啦），表征世界格局波动的强度。$\zeta \rho$ 体现了政党的 Stability 稳定性，由保守程度、实用主义而不由执行力决定。

（有人肯定要感到困惑——保守显然不带有很好的色彩。注意我们这里是在 ICR 不变下推导的，仅关注其维稳的能力。当国际形势变化之时，式子的右边将会出现外力平移项——我不再叙述，但显然一些类似受迫振动或共振的东西会冒出来……）

再强调一遍，定理所讲述的实质不过是：国际关系平衡态下的涨落冲击，与远离非平衡态的世界大变局下变动的耗散，本质上是一回事。我们愈想一个和平稳定的世界，这个世界也许就愈难回到和平。

（关于这个国际关系模型，提几个待改进的地方：1. 政治和文化光谱仍不明确，只能就事论事的设定而非统一框架；2. 生产要素市场应该予以重视；3. 财富储蓄、生命周期和预期对人的行为有重要影响；4. 某些产业、石油、移民等忽略的议题恰恰非常关键。）
