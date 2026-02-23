---
title: ODE 解的存在性
date: "2025-04-13"
weight: 14
tags: ["Math", "Analysis", "ODE"]
draft: false
---
{{< katex >}}
## ODE 解的存在性

我们考虑初值问题
$$
\frac{dy}{dt} = f(t, y), \quad y(t\_0) = y\_0
$$


设矩形区域 $ R = \\{(t, y) \in \mathbb{R}^2 : |t - t\_0| \le a, \ |y - y\_0| \le b\\} $，其中 $a, b > 0$。若函数 $ f: R \to \mathbb{R} $ 在 $R$ 上满足某些良好的连续性质，则存在性定理希望保证：至少存在一个解 $y(t)$ 定义在区间 $|t - t\_0| \le h$ 上，其中
$$
h = \min\left\\{a, \ \frac{b}{M}\right\\}, \quad M = \max\_{(t, y)\in R} |f(t, y)|
$$

### Picard–Lindelof Thm.

首先引入 Picard 的迭代解法，然后讨论它的实现保障。注意到 $f$ 连续，问题等价于（Volterra）

$$
y(t) = y\_0 + \int\_{t\_0}^{t} f(s, y(s))  ds
$$


递归定义函数列 $\\{\phi\_n(t)\\}$（Picard 迭代）
$$
\phi\_0(t) \equiv y\_0,\quad \phi\_{n+1}(t) = y\_0 + \int\_{t\_0}^{t} f(s, \phi\_n(s))  ds, \quad n = 0, 1, 2, \dots
$$
由于 $Mh \le b$，$|\phi\_n(t) - \phi\_0(t)| \le \int\_{t\_0}^{t} |f(s, \phi\_{n-1}(s))|  ds \le M |t - t\_0|$ 得所有 $\phi\_n(t)$ 均满足 $|\phi\_n(t) - y\_0| \le b$，故迭代始终保持在 $R$ 内。


Picard–Lindelof 定理假设 $f$ 关于 $y$ 满足一致的 Lipschitz 条件：
$$
\exists L > 0,\ \text{s.t. } |f(t, y\_1) - f(t, y\_2)| \le L |y\_1 - y\_2|,\ \forall (t, y\_1), (t, y\_2) \in R
$$
这一点将马上在积分项为我们控制函数提供便利，此时我们可以证明 $\phi\_n$ 一致收敛到解 $\phi$。

$$
\begin{aligned}
|\phi\_{k+1}(t) - \phi\_k(t)|
&\le \int\_{t\_0}^{t} |f(s, \phi\_k(s)) - f(s, \phi\_{k-1}(s))|  ds \le L \int\_{t\_0}^{t} |\phi\_k(s) - \phi\_{k-1}(s)|  ds \\
&\le L \int\_{t\_0}^{t} \frac{M L^{k-1} |s - t\_0|^k}{k!}  ds = \frac{M L^k |t - t\_0|^{k+1}}{(k+1)!} \quad \text{by induction}
\end{aligned}
$$

$$
\sum\_{k=0}^{\infty} |\phi\_{k+1}(t) - \phi\_k(t)| \le \sum\_{k=0}^{\infty} \frac{M L^k h^{k+1}}{(k+1)!} \le \frac{M}{L} (e^{Lh} - 1).
$$
Weierstrass M 判别法说明级数在 $|t - t\_0| \le h$ 上一致收敛，故 $\phi\_n(t)$ 一致收敛于某连续函数 $\phi(t)$。

那么验证极限方程：$\phi\_n \to \phi$ uniformly，且 $f$ 连续（事实上 Lipschitz），故 $f(t, \phi\_n(t)) \to f(t, \phi(t))$ uniformly。在迭代式 $\phi\_{n+1}(t) = y\_0 + \int\_{t\_0}^{t} f(s, \phi\_n(s))  ds$ 中取极限 $n \to \infty$，注意 $f$ 有界，得

$$
\phi(t) = y\_0 + \lim\_n\int\_{t\_0}^{t} f(s, \phi\_n(s))  ds = y\_0 + \int\_{t\_0}^{t} f(s, \phi(s))  ds
$$
因此 $\phi$ 是微分方程的解（且实际上 $C^1$）。唯一性同样令差值 $u(t) = |\phi\_1(t) - \phi\_2(t)|$，则 $u(t) \le L \int\_{t\_0}^{t} u(s)  ds$（对 $t \ge t\_0$，$t \le t\_0$ 类似），可解得 $u(t) \le 0 \cdot e^{L|t-t\_0|} = 0$。

考虑到 Lipschitz 的条件形式，更直接的视角是 Banach 不动点。记 $I=[t\_0-h, t\_0+h]$，$C(I)$ 在 $\|\cdot\|\_{\infty}$ 下是完备的，而 $\Phi \triangleq \\{y\in C(I):| y(t)-y\_0|\le b,\ \forall t\in I\\}$ 是 $C(I)$ 中的闭子集，为完备度量空间。

我们只需确认积分算子 $T(\phi) = y\_0 + \int\_{t\_0}^{t} f(s, \phi\_n(s))$ 满足压缩映射性质即可：$|(T\phi)(t)−y\_0|\le M|t-t\_0|\le b$，故 $T\phi\in \Phi$，同时可设 $Lh <1$，结果是显然的。

### Peano Thm.

没有 Lipschitz 即弱一些的条件仍可得到存在性，但不一定唯一（某些附加条件如 $f$ 关于 $y$ 单调或 Osgood 也可导出唯一）。我们这里再采用 Euler 折线法构造序列，利用 Arzela-Ascoli Thm. 提取一致收敛的子列及其极限函数。

先把折线法定义掉：对每个正整数 $n$，取步长 $h\_n > 0$ 满足 $h\_n \to 0$。在区间 $[t\_0-h, t\_0 + h]$ 上构造分段线性函数 $y\_n(t)$：$y\_n(t\_0) = y\_0$，$t\_{k, n} = t\_{0} + kh\_n,\ y\_n(t) = y\_n(t\_{k, n}) + f(t\_{k, n}, y\_n(t\_{k, n})) (t-t\_{k, n})$。


现在 show that $\\{y\_n\\}$ 一致有界和等度连续，前者由 $|y\_n(t)−y\_0|\le M|t-t\_0|\le b$，即 $|y\_n(t)|\le |y\_0| + b$，后者由 $\\{y\_n\\}$ M-Lipschitz 连续显然。

重要的 AA 定理告诉我们存在子列 $\\{y\_{n\_i}\\}$ 一致收敛到一个连续函数 $y: I \rightarrow \mathbb{R}$，有

$$
y\_{n\_i}(t) = y\_0 + \int\_{t\_0}^{t} f(s, y\_{n\_i}(s))  ds + e\_{n\_i}(t),
$$
其中误差项 $e\_n(t)$ 源于在每个小区间上用左端点值代替 $f$：
$$
e\_{n\_i}(t) = \int\_{t\_0}^{t} \tilde{f}\_{n\_i}(s)  ds -
\int\_{t\_0}^{t} f(s, y\_{n\_i}(s))  ds \quad (\tilde{f}\_n(s)\triangleq f(t\_{k, n}, y\_n(t\_{k, n}),\ t\_{k,n}\le s < t\_{k+1,n})
$$
（$s$ 属于 $t\_{k,n\_i}$ 段时）$|y\_{n\_i}(s)-y\_{n\_i}(t\_{k,n})|\le Mh\_{n\_i} \to 0$ uniformly，鉴于 $f$ 在 $R$ 上的一致连续，故 $|\tilde{f}\_{n\_i}(s) - f(s, y\_{n\_i}(s))| \to 0$ uniformly。因此当 $n\_i \to \infty$ 时 $e\_{n\_i}(t) \to 0$ unifromly。

那么极限后同样由一致收敛性及 $f$ 的连续性得证 $y(t) = y\_0 + \int\_{t\_0}^{t} f(s, y(s))  ds$。

最后再附注一个不保证唯一性的经典反例，$y^\prime=\sqrt{|y|},\ y(0)=0$，零解和右侧 $\frac{t^2}{4}$ 均满足，此处 Lipschitz 条件不成立。

### Solution Extension

从局部行为推到整体行为的思路不少，紧性一定是最重要的之一。设 $D\subset \mathbb{R}^2$ 连通开集，$f \in C(D,\mathbb{R})$ 对每个区域 $D$ 内的点，初值问题在某个邻域内存在唯一解（常由局部 Lipschitz 保证），则可以把解延拓到最大（无穷远或 $D$ 边界）。我们要说明 $(t,y(t))$ 不会停留在 $D$ 的紧子集中。
