---
title: 打卡软件 Swarm 数据分析报告
date: "2023-06-02"
weight: 7
tags: ["Data", "Statistics", "Multivariate", "Model"]
draft: false
---
{{< katex >}}

> Swarm 是 4sq 的一款依靠签到的社交应用。用户可以在自己感兴趣的地点打卡发照片，展示给好友。
>
> 本数据集中给出了三个城市范围内的签到数据和对应签到用户的个人信息数据，分别是纽约市（nyc）、旧金山（sfo）和香港（hk）。
>
> 各城市的签到数据包括 8 个字段：用户 id，本地/外地，签到地点 id， 地点类型，地点类型 id，地点经度、纬度，签到时间。
> 各城市对应签到的用 户数据包括 6 个字段：用户 id，本地/外地，男/女，签到发布数，照片发布数，好友数。
>
> 众所周知位置信息具有非常巨大的商业价值。本文仅作了一些初步的整理和观察。

**打卡的对数正态分布**

<img src="./SwarmTex/qq.png">

**用户偏好的因子模型**

<img src="./SwarmTex/fac2_oblique.png">
<img src="./SwarmTex/group.png">

**判别本地还是外来**

<img src="./SwarmTex/disc.png">
<img src="./SwarmTex/err_f.png">

---

下载链接：

[原数据集](./SwarmData.zip)

[完整报告](./Swarm.pdf)

[源码](./SwarmMatlab.zip)（MATLAB，包含实时脚本、函数及工作区快照）