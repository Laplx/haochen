---
title: 'Theory of Theory'
date: "2023-10-20"
tags: ["Model", "Information", "Notion"]
draft: false
---
{{< katex >}}
### 理论的理论

我要讲的是“学科的学科”——虽然高中课本里哲学似乎便这么宣称——但这里讲的是言之有物的理论构建，而非关乎世界本质的基础支撑。

广义的理论（Theory）可以等同为知识（Knowledge），而知识被我分为 Experience、Analysis、Science 三种层级。Experience 指经验性的总结 Synthesize 和解释 Explain，例如我们可以对厕所的规划和使用形成学问，对什么样的音乐是好听的形成学问，但其来源都是已有事物的 Application，类似一个经验丰富的老技工。Analysis 指在一定抽象程度上建立的统一分析框架 Analytical Frame，大家在平常能见到的“XX学”都已经达到了这样的标准；但 Analysis 在现实中仍然有可能只能做解释或归纳性的预测。Science 被定义为 Modeling 模型化现实，给出考察对象之间的作用关联，其目的是预测 Predict 和控制 Control。我们这里的理论 Theory 便是狭义的理论，特指科学学科 Science。我给出的范式是：

$$
\mathcal{X} \rightarrow X \rightarrow \boxed{\mathbb{T}} \rightarrow Y \rightarrow \mathcal{Y}
$$

$\mathcal{X} \rightarrow X$ 和 $\mathcal{Y} \rightarrow Y$ 都是概念化 Conceptualize 的过程。$\mathcal{X}$ 和 $\mathcal{Y}$ 是现实世界的对象或情形，$X$ 和 $Y$ 是我们理论的输入和输出。（注意$X$可以不仅仅是某个数值变量“政府年度固定投资额”，还可以是“财政政策不变”这样更为抽象的输入或问询。）科学理论的核心是相关与因果。仅相关的关联性可以做到预测，而因果性（并不是一个容易论断的东西）可以做控制和应用。中间的模型机制 Laws or Theorems $T$ 和概念 Concepts $C$ 组成了一个完整的理论 $\mathbb{T}=\\{T\_1,\cdots,T\_i,C\_1,\cdots,C\_j\\}$ 。每个定理（或定理的一部分）都可以写成 $c = T(c\_1,\cdots,c\_n)$，其中 $c$ 是 $C$ 的具象输入。我们这里缺少了几个理论里常见的模块，但其实已经纳入机制 $T$ 内了，包括假设 Assumption 和公理 Axiom ——一种未经验证的假定的$C$之间的关联性；引理 Lemma 和推论 Corollary ——也是定理们特定的同义重复。

利用不变性定理，当把 $\mathbb{T}$ 视作通用图灵机，我们给出其 Kolmogorov 复杂度 $K(T)$（注意是对其中定律和定理部分 $T$ 的描述，准确来说特定的模型下应记 $K(T|c)$），表示了理论的复杂度或丰富程度。这样避免了推论不推论的问题——可惜存在不可计算性。

理论的另一组成部分是概念化（以及我想 $K(\mathbb{T}) \approx K(C) + K(T)$，不过 $K(C)$ 的价值有待商榷），我们用描述度 $R(C)$ 表示概念化映射 $C: \mathcal{X} \rightarrow c\_X$ 的定义域，等于理论的适用范围 $R(T)$。参照柯氏复杂度的上界，我们有 **Theory Inequality** 

$$
K(T) \le K(T|R(T)) +  S(T) + c\_0 \tag{1}
$$

其中 $S(T) = log(R(T))$ 为理论熵 Theory Entropy。这说明即使我们明晰了理论在现实中的适用范围，它的复杂度仍然存在一个下界。

定义理论的质量 $Q(T) = \frac{S(T)}{K(T)}$，由此不难料想物理学的理论 $Q(Physics)$ 会很高。

我们利用链式法则

$$
K(T\_1,T\_2) = K(T\_1) + K(T\_2|T\_1) + O(logK(T\_1,T\_2))
$$

考虑一个理论的泛化。由于 $K(T\_2|T\_1) \le K(T\_2)$ ，则

$$
Q(\sum T) \ge \frac{\sum S(T)}{\sum K(T)} \tag{2}
$$

等号在理论满足可加性（即异质建模）时成立，否则抽象化能够提高理论的质量。

考虑一个理论的修正。应有 $Q(T,\delta T) \ge Q(T)$，利用 $O(\frac{logK}{K}) \rightarrow 0$ 得到 **Revision Inequality**

$$
K(T) \frac{\delta S}{S} \ge K(\delta T|T) \tag{3}
$$

修正理论真正的内禀复杂度存在由其延拓范围控制的上界。

然后关于理论的质量，通过类似 Godel 不完备性的手段，我来指出一个可能存在的理论的质量上界 **Theory Quality Bound**

$$
Q(T) \le \frac{S(\mathcal{T})}{K\_0},\ \forall T \in R(\mathcal{T}) \tag{4}
$$

（$\mathcal{T}$ 为全部理论的理论，没错就是今天我们的主角；$K\_0$ 是通用图灵机执行该不等式的固定的最短长度。）

鉴于不可计算性，我们可能永远无法得知一门学问的极限究竟在哪里——学无止境，但我们将趋近它。

（其实还有很多可以继续写，暂时到这里吧！）