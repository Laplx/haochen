---
title: 'CC Theorem'
date: "2024-01-05"
tags: ["Finance", "Model"]
draft: false
---
{{< katex >}}
### CC 定理

（感谢 Y. S. Cao 的邀请！正好我也姓C，依葫芦画瓢搞了个搞笑版的 CC 定理）

我们打算评判一个学生的期末价值。这个价值为整学期知识流的折现和，但这里的知识流仅仅是针对考试的‘有用’，因此都可以通过期末考卷评估，最后被GPA所衡量。那么影响这个价值的有哪些因素呢？可以是多种结构的作用，如融课结构和时序结构，等等。（融课结构指学生选择的水硬课杠杆，时序结构指不同课考试时间的安排——这对期末复/预习的精力分配及最终的成绩异常重要）

$$
\text{ courses } \left\\{\begin{array}{l}
\text{ hard } H \text{ with honor tax } \tau\\\
\text{ easy } E
\end{array} \right.
$$

这个荣誉税 honor tax 指的是某些荣誉课每周加一些事情的现象，而且这些事情对期末成绩几乎没有影响，纯纯占用学习时间罢了（注意我们这里在功利的评判期末价值）。因此相当于上交了一定比例的精力（若用之学习带来的知识流的机会成本）。在不考虑荣誉税，且学生可以自由退选课以最大化绩点的情形下有：

$$
\begin{align}
&\text{ CC Theorem 1:} \\\
&\quad V = H + E = \frac{K}{r} \\\
&\text{ Proposition: Free Course Market }
\end{align}
$$

$K$ is the knowledge flow a student earned during each week. $r$ corresponds to the level of the student's learning skill or forgetting rate, while more risk means weaker ability and a higher $r$.  $r\_o$ is the standard forgetting rate of a person.

$$
\begin{align}
&\text{ CC Theorem 2:} \\\
&\quad V = H + E = \frac{K}{r} + \frac{-\tau H}{r\_o}
\end{align}
$$

Thus honor courses only to students if no academic value is considered. $walc = r (1+ \frac{\tau}{r\_o}\frac{H}{H+E})$ gets larger when the honor leverage $\frac{H}{H+E}$ becomes larger.

For market, we have

$$
r = r\_o + \beta(r\_M-r\_o)
$$

where $\beta = \frac{Cov(GPA\_M,GPA\_S)}{V(GPA\_M)}$ can be calculated by the average variation of the whole undergraduate students' GPA (the market GPA) and the correlation between the market GPA and the avergae GPA of students in the same learning level.

$$
\begin{align}
&\text{ Additional values: } \\\
&\quad V' = V + \sum\limits\_i r\_wT\_i + Ac(H)
\end{align}
$$

$T\_i$ is the reviewing time of course i and $r\_w$ is the knowledge output rate in reviewing weeks, $r\_w > r > r\_o$. Here we don't give a thorough consideration of how students arrange their time across different courses with different test dates. $Ac(H)$ is a function of academic value of $H$ honor course credits, probably concave. Then  we will get a maximizing point of $H^*$ (the best course structure).
