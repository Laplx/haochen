---
title: 量子力学的形式理论
date: "2023-10-01"
weight: 9
tags: ["Physics", "Quantum"]
draft: false
---
{{< katex >}}
系统的运动状态**由 Hilbert 空间（所有平方可积函数构成的线性空间）中的一个矢量 $\ket{ \mathfrak{I} }$ 描述**。

> $\ket{ \mathfrak{I} } \in \mathcal{H}$ ， $\mathcal{H}$ 可以为分立维空间，也可以为连续维空间。 $\bra{I} \in \mathcal{H}^{ \* }$ 为其对偶矢量，把矢量映射为一个数。对分立维矢量，其对应的左矢看作其 Hermitian 的左乘；对连续维矢量（函数），看作一个对积分的指定 $\int f^{ \* }(x) [ \dots ] \mathrm{~d}^{3} x$ 。

**可测力学量与 Hermitian 算符一一对应**，对可测力学量的观测结果必为其对应算符的本征值之一。将态矢 $\ket{ \mathfrak{ I } }$ 按照其本征函数集做线性展开，得到的**系数取模方即为测得对应本征态的概率。测量过后态矢坍缩为对应本征态**。

> Hermitian 算符为 Hilbert 空间中的线性变换，且对应的矩阵为 Hermitian 矩阵（转置共轭等于自身）。由此可以证明，Hermitian 算符的本征值必为实数，属于不同本征值的本征函数必定正交。Dirac 取公理为，可测力学量对应的 Hermitian 算符必有一个正交完备的本征函数集。
> 
> 利用归一基 $\ket{a}$ 对应的算符 $\hat{P} = \ket{a} \bra{a}$ 可以求得态矢在其方向上的投影。类似地，可以将态矢按照本征函数集展开。
> 
> $$
\ket{ \mathfrak{I} } = \sum\_{a} \ket{a} \braket{ a | \mathfrak{I} }
  $$
> 
> 通过确定在每个基矢 $\ket{a}$ 上的系数，我们可以确定对应的态。这种描述的态矢称为可测力学量 $A$ 对应的表象中的波函数。**不同表象间可以相互变换**，例如坐标表象和动量表象
> 
> $$
 \begin{array}{l}
 \ket{ \mathfrak{I} } = \sum\_{r} \ket{r} \underbrace{ \braket{ r | \mathfrak{I} } }\_{ \psi(r) } = \sum \_{p} \ket{p} \underbrace{ \braket{ p | \mathfrak{I} } } \_{ \phi(p) } = \sum \_{p,r} \ket{p} \braket{ p | r} \braket{ r | \mathfrak{I} } \\\
 \phi(p) = \sum \_{r} \braket{ p | r } \psi(r)
 \end{array}
  $$
> 
> 考虑坐标表象中的动量本征函数 $\psi\_{p}(r,t) = A(t) e^{ i \frac{p \cdot r}{\hbar} }$ ，有 $\ket{p} = \sum\_{r} \ket{r} \psi\_{p}(r)$ ， 即
> 
> $$
 \braket{ r | p } = \psi\_{p}(r) = \frac{1}{(2 \pi \hbar)^{3/2}} e^{ i \frac{ p \cdot r }{ \hbar } }
  $$
> 
> 作为理论自洽性的考量，还要证明两个表象下态矢的演化规律等价。

由于实验上测得的都是可测力学量的概率分布，即 Hilbert 空间中态矢与可测力学量归一基底的内积模方。因而态矢的演化有两种视角，一种是认为力学量对应的算符及其特征矢量不随时间演化，而是态矢与能量本征矢量随时间演化（Schrodinger 绘景）；另一种是认为态矢与能量本征函数不随时间演化，而是力学量算符随时间演化（Heisenberg 绘景）。（为什么能量本征函数上的系数不变？）

**Schrodinger 绘景下，态矢的运动方程为**

$$
\begin{array}{l}
i \hbar \frac{d}{dt} \ket{\psi} = \hat{H} \ket{\psi} \\\
\ket{\psi(t)} = e^{ -i \frac{ \hat{H} t }{\hbar} } \ket{\psi(0)} = \hat{U} \ket{\psi(0)}
\end{array}
$$

力学量期望的演化为

$$
\begin{array}{l}
\braket{A} &= \bra{\psi(t)} \hat{A} \ket{\psi(t)} \\\
&= \bra{\psi(0)} \hat{U}^{+} \hat{A} \hat{U} \ket{\psi(0)}
\end{array}
$$

后者为 Heisenberg 绘景。

> Heisenberg 绘景中， $\hat{A}(t) = \sum\_{m,n} \ket{m} A\_{m,n} e^{i \frac{ E\_{m} - E\_{n} }{\hbar} t } \bra{n}$

> 具体到坐标表象中， $\ket{\psi} = \sum\_{r} \ket{r} \psi(r)$ ， $\hat{H} = \frac{\hat{p}^{2}}{2m} + V(\hat{r})$
> 
> $$
 i\hbar \frac{\partial}{\partial t} \psi(r, t) = \left( - \frac{\hbar^{2}}{2m} \nabla^{2} + V(r) \right) \psi(r, t)
  $$
> 
> 我们一般先求解所谓定态 Schrodinger 方程
> 
> $$
 \hat{H} \psi\_{E}(r) = E \psi\_{E}(r)
  $$
> 
> 然后再将初态波函数以之为基底展开，求得任意时刻的波函数。（直接用上面的算符表达式计算波函数演化也行。）此后我们再求可测力学量 $\hat{A}$ 的本征函数
> 
> $$
 \hat{A} \psi\_{a}(r) = a \psi\_{a}(r)
  $$
> 
> 通过将某刻波函数与之做内积得到测量的概率分布。

最后，作为一个应用，我们来讨论不确定原理与最小不确定波包。

$$
\begin{aligned}
\sigma\_{A}^{2} \sigma\_{B}^{2} &= \braket{ (\hat{A} - \braket{A}) \psi | (\hat{A} - \braket{A}) \psi } \braket{ (\hat{B} - \braket{B}) \psi | (\hat{B} - \braket{B}) \psi } \\\
&\geq \left\lvert \braket{ (\hat{A} - \braket{A}) \psi | (\hat{B} - \braket{B}) \psi } \right\rvert^{2} \\\
&\geq \left\lvert \frac{1}{2i} ( \braket{ (\hat{A} - \braket{A}) \psi | (\hat{B} - \braket{B}) \psi } - \braket{ (\hat{B} - \braket{B}) \psi | (\hat{A} - \braket{A}) \psi } ) \right\rvert^{2} \\\
&\geq \left( \frac{1}{2i} \braket{ [\hat{A}, \hat{B}] } \right)^{2}
\end{aligned}
$$

$$
\iff (\hat{A} - \braket{A}) \psi = ia (\hat{B} - \braket{B}) \psi
$$

$$
\frac{d}{dt} \braket{A} = \frac{1}{i \hbar} \braket{ [\hat{A}, \hat{H}] } + \underbrace{ \braket{ \frac{\partial \hat{A}}{\partial t} } }\_{\mathrm{usually = 0}}
$$

$$
\sigma\_{A} \sigma\_{H} \geq \frac{\hbar}{2} \left\lvert \frac{d \braket{A}}{dt} \right\rvert \implies \frac{\sigma\_{A}}{ \lvert d\braket{A}/dt \rvert } \sigma\_{H} \geq \frac{\hbar}{2}
$$
