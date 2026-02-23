---
title: Newton 力学纲要
date: "2024-06-28"
weight: 13
tags: ["Physics", "Mechanics"]
draft: false
---
{{< katex >}}
### Galileo 时空

Galileo 模型把事件抽象为时空中的一个点，时空同胚于在 $\mathbb{R}$ 上的四维仿射空间 $\mathcal{A}^{4}$。

定义时间间隔 $t(a,b) \in \mathbb{R}$ 使所有与某事件同时的事件构成一个三维仿射子空间 $\mathcal{A}^{3}$。这一附加结构指定了绝对时间。

定义同时事件的空间间隔 $d(a,b)$ 使得同时事件空间成为三维欧式空间 $\mathbf{E}^3$。

某参照系 $(O,\hat{e\_{i}})$ 指定任一时刻的原点位置和笛卡尔坐标系的三个方向。此时任意事件在该参考系下具有一个时间坐标和三个空间坐标 $a \mapsto (t,\mathbf{r})$。我们描述物理过程总是离不开参考系。上述两个假定保证了不同参照系间的时间间隔不变性和空间间隔不变性。

### 质点与质点组

质点是描述力学系统运动最基本的单元，其运动用 $\mathbf{r}(t)$ 描述，具有内禀属性质量 m。

复杂的力学系统可以分解成质点的集合，系统的内部性质由质点间的相互作用表示。对质点的作用用力表示。

此时每个质点受到的力可以归结为外部作用力（包括保守力和非保守力）加上质点组内部的作用力。

$$
\mathbf{F}\_{i}=\sum\_{j\neq i} \mathbf{F}\_{ji}+\mathbf{F}\_{i}^{(e)}(+\mathbf{F}\_{i}^{(s)})
$$

### Newton 第一定律

有一类特殊的参照系，其时空平直，称为惯性系。惯性系中，自由质点有

$$
\ddot{\mathbf{r}}=0
$$

这是自然的，因为平直时空中不受外部作用的质点应当没有向任何方向运动的趋势。

根据惯性系中自由质点的要求可推出两惯性系间有Galileo 变换。

### Gailileo 变换

$$
\begin{pmatrix}
t^{^\prime } \\\
\mathbf{r}^{^\prime } \\\
1
\end{pmatrix}=
\begin{pmatrix}
1 & 0 & t\_{0} \\\
\mathbf{v} & \mathbf{R} & x\_{0} \\\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
t \\\
\mathbf{r} \\\
1
\end{pmatrix}
$$

其中$\mathbf{R}^{T}\mathbf{R}=\mathbf{I}$

> 由于 Galileo 的假定，引入的参照系可以是非局域的。

**推导**

时空中某点 $P$，在两个参照系下的坐标为 $(t,\mathbf{r}),(t^{^\prime },\mathbf{r}^{^\prime })$，考虑一个小偏移

$$
\left\\{
\begin{matrix}
\mathrm{d} t^{^\prime } = \mathrm{d} t \\\
\lvert \mathrm{d} \mathbf{r}^{^\prime } \rvert = \lvert \mathrm{d} \mathbf{r} \rvert
\end{matrix}
\right.
$$

代入到线性变换中得到

$$
\begin{pmatrix}
\mathrm{d} t^{^\prime } \\\
\mathrm{d} \mathbf{r}^{^\prime }
\end{pmatrix} =
\begin{pmatrix}
1 & 0 \\\
\mathbf{v} & \mathbf{R}
\end{pmatrix}
\begin{pmatrix}
\mathrm{d} t \\\
\mathrm{d} \mathbf{r}
\end{pmatrix}
$$

$$
\mathbf{R}^{T} \mathbf{R} = \mathbf{I}
$$

再由时空线性得到伽利略变换。

### Newton 第二定律

$$
m \ddot{ \mathbf{r} } = \mathbf{F}
$$

$\mathbf{F}$ 反应质点受到的作用。$\mathbf{F}=\mathbf{F}^{(e)}+\mathbf{F}^{(s)}$，前者为外界对质点的作用，与参照系无关；后者为惯性力，反应某参照系下时空不再各向同性的贡献。**此后研究问题默认在惯性系中。**

尽管从因果逻辑上讲是由力决定了加速度，但力作为对质点作用的描述，由 Newton 第二定律定标。

**推论：单质点的线动量与角动量定理，能量定理**

由牛顿定律推得

$$
\mathbf{F} \mathrm{d} t = \mathrm{d} ( m \dot{ \mathbf{r} } )
$$

$$
\mathbf{r} \times \mathbf{F} \mathrm{d}t = \mathrm{d} ( \mathbf{r} \times m \dot{ \mathbf{r} } )
$$

$$
\mathbf{F} \cdot \mathrm{d} \mathbf{r} = \mathrm{d} \left( \frac{1}{2} m \dot{ \mathbf{r} }^{2} \right)
$$

**推论：保守力与能量守恒**

在此基础上，若做功与路径无关，即外力为保守力

$$
\oint \mathbf{F}\cdot d\mathbf{r}=0 \iff \mathbf{F}=-\nabla V(\mathbf{r})
$$

有能量守恒

$$
T+V=E
$$

> 接下来我们的研究对象从单质点变为质点组。

### Newton 第三定律

弱形式

$$
\mathbf{F}\_{ji} = - \mathbf{F}\_{ij}
$$

强形式

$$
\mathbf{r}\_{i} \times \mathbf{F}\_{ji} + \mathbf{M}\_{ji} + \mathbf{r}\_{j} \times \mathbf{F}\_{ij} + \mathbf{M}\_{ij} = 0
$$

### 运动与牛顿方程

结合牛顿定律，可以将数学规律概括为如下形式。

n 点系统的运动为映射

$$
\mathbf{r}(t):\mathbf{I} \to \mathbb{R}^{3n}
$$

牛顿方程假设，存在映射

$$
\mathbf{F}(\mathbf{r},\dot{\mathbf{r}},t):\mathbb{R}^{3n}\times \mathbb{R}^{3n}\times \mathbb{R} \to \mathbb{R}^{3n}
$$

使

$$
\ddot{\mathbf{r}}=\mathbf{F}(\mathbf{r},\dot{\mathbf{r}},t)
$$

由常微分方程解的存在与唯一性定理，该映射与初始条件唯一决定一个运动，因此一个力学系统的初始位置和初速度唯一地决定其运动。

### 伽利略相对性原理

要求牛顿方程在伽利略变换下不变。
- 时间平移不变$\implies \ddot{\mathbf{r}}=\mathbf{F}(\mathbf{r},\dot{\mathbf{r}})$
- 空间平移不变$\implies \ddot{x}\_{i}=F\_{i}(x\_{j}-x\_{k},y\_{j},z\_{j};\dot{x}\_{j}-\dot{x}\_{k},\dot{y}\_{j},\dot{z}\_{j};t)$
- 空间正交变换不变 $\implies \mathbf{F}(\mathbf{R}\mathbf{x},\mathbf{R}\dot{\mathbf{x}},t)=\mathbf{R}\mathbf{F}(\mathbf{x},\dot{\mathbf{x}})$

### 守恒量

在多质点系统中类似有

$$
\sum\_{i}F\_{i}^{(e)}=\frac{d}{dt} \sum\_{i}m\_{i}\dot{\mathbf{r}}\_{i}
$$
$$
\sum\_{i} \mathbf{r}\_{i} \times \mathbf{F}\_{i}^{(e)}=\frac{d}{dt} \sum\_{i} \mathbf{r}\_{i} \times m\_{i} \dot{\mathbf{r}}\_{i}
$$
$$
\sum\_{i} \mathbf{F}\_{i}^{(e)} \cdot d \mathbf{r}\_{i} + \sum\_{i,j>i} \mathbf{F}\_{ji} \cdot (d \mathbf{r}\_{i}-d \mathbf{r}\_{j}) = d \sum\_{i} \frac{1}{2} m\_{i} \dot{\mathbf{r}}\_{i}^{2}
$$
$$
dW\_{外}+dW\_{内非}=d(T+V\_{内势})
$$
$$
(dW\_{外宏}+dQ+(-dE\_{微})=dE\_{宏})
$$

普遍情况见诺特定理。

### 质心

#### 质心运动

$$
\mathbf{r}\_{c} = \frac{\sum m\_{i} \mathbf{r}\_{i}}{\sum m\_{i}}
$$
$$
m \ddot{\mathbf{r}}\_{c} = \sum \mathbf{F}\_{i}^{(e)}
$$
可以推出质心像一个质点的守恒量，尤其是

$$
\sum \mathbf{F}\_{i}^{(e)} \cdot d \mathbf{r}\_{c} =d \left( \frac{1}{2} m \dot{r}\_{c}^{2} \right)
$$

#### 质心系 (相对质心运动的描述以及地系到质心系的转化)

地系中与质心系中物理量的变换有 Konig 定理

$$
T=T^{^\prime }+\frac{1}{2}m \dot{\mathbf{r}}\_{c}^{2}
$$

$$
L=L^{^\prime }+\mathbf{r}\_{c} \times m \dot{\mathbf{r}}\_{c}
$$

$$
p^{^\prime }=0
$$

以质心为参考点时惯性系定律成立。

### 坐标系及参照系变换
