---
title: 'The Apple that Never Lands'
date: "2023-11-17"
tags: ["Economy", "Statistics", "SciPop"]
draft: false
---
{{< katex >}}
### 永不落地的苹果

（更多关于民科的了解可以查看“其他收录”中的民科小传一篇，其末尾还有本人的一些讨论）

我在想一个

$$
\text{Scipop Paradox}:\\\
\frac{PseudoPaper\_i}{Population\_i} = \sum\limits\_{t\in T} \beta\_t \frac{ScipopWork\_{i,t}}{Population\_{i,t}} + \gamma^\prime\mathcal{X}\_{i} + \alpha\_i + u
$$

$Scipop$ 指的是 science popularization，科普的一种翻译。但国外 scientific literacy 科学素养使用的更多（用此关键词搜索文章也与科普更为相关）。

这里采用省截面数据（$i$），$ScipopWork$ 指各省发行出版或流通的科普性质的作品量，$PseudoPaper$ 指民科的生产量——这从哪里来呢？把时间背景（$T$）放到上世纪80-90年代左右，中科院研究所每天都要收到大量信件宣称自己造出了永动机或解决了哥德巴赫猜想之类的……可以统计其寄件人的省份分布得到。（当然还有不少自费出版的民科书籍可以统计；再不济还能看新闻里的主人公来自哪里……）$\mathcal{X}$ 为控制变量，可能包含人均产出、城市化水平、科教院所数量等。我的 prediction 为：$\beta\_t$ 在1978年“科学的春天”后的十余年里显著为正。亦即一个看上去像是悖论的命题：当时的科普风气越盛，民科数量反而越多。

进一步的 endogeneity concern or robustness 暂且略去。比如寻找 $ScipopWork$ 可能的工具变量；考虑 $ScipopAuthor$ 科普作者的地区分布；回归 $\frac{TruePaper}{Population}\_i$ ，也许存在着负向关联放大悖论。

科普历来是争论的话题。在我眼里，就像 scientific literacy 一样，科普本身即应该定义为科学的末端，无非是让不了解此领域的人能以科学的视角和方法正式的纳入一些有关此领域的基础知识罢了。可这是需要基本的教育去提供基本的理性素养的。

而当下的科普不是去关注苹果落地后发生的事，却只着重宣传苹果掉落的瞬间。科学理论本身是理性且严肃的，其宣传却夹杂着浪漫与造神主义；美其名曰加入科学史和人文元素，却只剩下了科学史和人文元素。思而不学，不接受真正的科学普及而仅仅凭着一些类科普提供的模糊面貌和一些内心的激情与偏执大肆幻想，便成为了民科。

（虽然还没实证确定呢！）我想说的只是，这个看起来就很伪的悖论告诉大家：科普何以存在？没有坚实的教育和素质基础，没有合格的传播和内容关注，科普便会永远停留在伪命题上，apples will never on the ground。