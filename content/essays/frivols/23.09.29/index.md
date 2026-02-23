---
title: 'The Limit of Handwritting'
date: "2023-09-29"
tags: ["Model", "Information"]
draft: false
---
{{< katex >}}
### 书写有极限吗

作为速记爱好者，我开发过不止一套自己的速记符号，期间的考虑无非是平衡简化程度与易学易辨的程度。本周突然想来思考一下手写本身的 physical bound 在哪里。

$$
\begin{align}
\text{Systematic Process}:\\\
1.\ infor&mation\ flow\ (sounds\ etc.)\\\
& \downarrow compiling\ (handwritting\ system)\\\
2.\ gra&phic\ symbols\\\
& \downarrow handwritting\\\
3.\ &notes\\\
& \downarrow interpreting\\\
4.\ recov&ered\ information
\end{align}
$$

$$
\begin{align}
& \text{Assumption}:\\\
& 1.\ Fluency: A\ constant\ speed\ \mathbf{v}\ of\ writting\ lines\ or\ curves.\\\
& 2.\ Smoothness: There\ is\ no\ sharp\ angles\ and\ writter^\primes\ acceleration\ can\ be\ infinity.
\end{align}
$$

那么总时间可以被分为两部分（充分效率，即没有空闲时间）：

$$
time \left\{
\begin{align}
& drawing\ lines\ and\ curves\ \ \ \ \mathbf{t_L = \frac{L}{v}} \\\
& real/unreal\ lines\ changing\ (lifting\ up\ and\ down\ the\ pen)\ \ \ \ \mathbf{t_S}
\end{align}
\right.
$$

从一个符号到另一个符号中间笔尖的移动可以视为写一条unreal line，这个提落笔的转换需要时间（由于手部的摩擦等）。

书写符号系统将语段的信息流划分为一个个 info element ，每个信息元对应一个符号来记录。$l$ 表示信息元的平均长度；我们在第四步解读的过程中，部分多义或偏误的符号可以通过上下文判断，即 $revision\ rate\ \mathbf{c = c(l)}，\mathbf{c^\prime(l) \le0}$ ，有一定概率 $c$ 的内容可以被矫正，其与元长成负相关。符号的压缩密度 $\eta$ 表征了记号的简洁程度；随着 $\mathbf{v}$ 的提高，书写的 deviation 上升，如果压缩率高，最终偏误的可能性越大。

如同平衡投资的风险与收益一样，我们用一个效用函数平衡速度与失误率 $U(k,e)$ ，其中 $k$ 为信息流速率，即总信息量 $I = kT$ 。一种 unexamined and nearly impossible 的情况：

$$
\left\{
\begin{align}
& maximize\ \ U=k(1-\frac{e}{T})\\\
& I = kT\\\
& n = \frac{I}{I_l}\\\
& I_l = l \ln \frac{1}{\eta}\\\
& 2nt_S + n \frac{l}{v} = T\\\
& e = n(1-f(\eta,v))(1-c(l))\\\
& f(\eta,v) = \frac{v}{\eta}, c(l) = \frac{c}{l}
\end{align}
\right.
$$

上面的假设都还没怎么用，还可以再详细一点，比如从解析几何的角度，斜椭圆曲线任一点斜率的一定概率范围的偏差有多大可能使得整条线变入另一个符号的范围？从信息论的角度，这个高斯信道（准确说是这两个）的容量香农已经告诉我们了，而 Yury, 2010 指出，在有限码长和一定错误概率下的最大码率

$$
Max\ rate\ achivable\ R \approx C − \sqrt{\frac{V}{n}}Q^{−1}(ϵ)
$$

where $n$ is the blocklength, $C$ is the capacity, $\epsilon$ is the error probability, $V$ is a characteristic of the channel referred to as *channel dispersion* and $Q$ is the complementary Gaussian cumulative distribution function.

(This guy has almost killed my problem.)

**Reference**

[1] Y. Polyanskiy, H. V. Poor and S. Verdu, "Channel Coding Rate in the Finite Blocklength Regime," in IEEE Transactions on Information Theory, vol. 56, no. 5, pp. 2307-2359, May 2010, doi: 10.1109/TIT.2010.2043769.