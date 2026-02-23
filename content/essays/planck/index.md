---
title: Planck 公式在历史上是怎么诞生的
date: "2025-10-23"
weight: 4
tags: ["Physics"]
draft: false
---
{{< katex >}}
### Wein：热力学结合实验定律猜测

1896，Wien 考虑缓慢膨胀的球体中的单频平衡辐射场，由多普勒效应

$$
\nu / T = Const
$$

结合 Stefan-Boltzmann 的结果，平衡辐射场的能谱应为

$$
u d\nu = \nu^{3} f(\nu/T)
$$

结合实验规律，猜测未知函数为指数形式

$$
u d\nu = c\_{1} \nu^{3} e^{ - c\_{2} \nu / T }
$$

这个公式对实验的符合结果不错，替代了之前一系列猜的公式。

### Rayleigh：从电磁和统计的理论出发

1900，Rayleigh 不满 Wein 的结果没有电磁相关基础，考虑一个电磁方腔，内部所有允许的电磁驻波构成了一系列振子，某个频率附近的振子数 $\frac{8\pi}{c^3} V \nu^{2} d \nu$。

考虑能均分定理，每个振子的平均能量 $U = kT$，得到

$$
u d\nu = \frac{8\pi k}{c^{3}} \nu^{2} T d\nu
$$

这里出现了著名的紫外灾难，Rayleigh 于是强行在后面增加了指数衰减项。而在 1905 年 Jeans 算出了系数，并坚定地去掉了指数项。Jeans 敢于坚持紫外发散，又在历史上先于 Planck 接受了量子的观点，不失为一段趣事。

### Planck：内插法与量子解释

1900.10，Planck通过内插法，具体而言，考虑所有振子间能量的涨落

$$
\begin{array}{l}
U = \bar{E} = \frac{1}{Z} \sum E e^{- \beta E} = - \frac{\partial \ln Z}{\partial \beta}\\\
\overline{(E-U)^{2}} = \frac{1}{Z} \sum (E^2 - U^2) e^{- \beta E} = - \frac{1}{Z} \frac{\partial}{\partial \beta} (Z U) - U^2 = - \frac{\partial U}{\partial \beta}\end{array}
$$

对 Wien 公式

$$
\begin{array}{l}
U = c\_{1} \nu e^{- c\_{2} \nu / T} \\\
\overline{(E-U)^{2}} = k c\_{2} \nu U
\end{array}
$$

对 Rayleigh 公式

$$
\begin{array}{l}
U = kT \\\
\overline{(E - U)^{2}} = U^{2}
\end{array}
$$

注意此处用 U 表示而非用 T，可能因为 T 反应不同能级上分布？求解

$$
-k \frac{1}{\frac{d (1/T)}{d U}} = k c\_{2} \nu U + U^{2}
$$

$$
U = \frac{h \nu}{e^{h\nu / kT} - 1} = \frac{\sum nh\nu e^{-\beta nh\nu}}{\sum e^{- \beta nh\nu}}
$$

解释为每个振子的能量只能处在 $h\nu$ 的整数倍上。

<!-- 20230730 ljh -->