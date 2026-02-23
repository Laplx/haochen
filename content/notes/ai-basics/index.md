---
title: 智能引论
date: "2025-12-02"
weight: 18
tags: ["AI", "Algorithm", "Search", "Knowledge Representation"]
draft: false
---
{{< katex >}}
## 0 Intro

#### 智能计算的方法：

- 推理（符号主义），包括归纳、演绎、因果，e.g. 专家系统

- 搜索（问题求解），包括无信息（深/广度优先）、有信息（启发式）、对抗（e.g. Minimax, alpha-beta, MCT）

- 机器学习（数据驱动），包括

  - 监督：判别式 $P(y|x)$（e.g. 回归, 提升, SVM, DecisionTree）与生成式 $P(X,Y)$（e.g. LDA, HMM）
  - 无监督：聚类（e.g K-means, 层次, 谱）、降维（线性（e.g. PCA, LDA/FDA, CCA）与非线性 i.e. 流形学习）、EM
  - 半监督等

- 强化学习（行为主义），MDP，exploration-exploitation tradeoff，MARL {博弈论可以提供多智能体环境下结果的刻画，或寻找合理解的非启发的方式，但不认为是核心}

  esp. 深度学习（联结主义）作为监督学习方法，并和强化学习结合（如拟合 Q 函数）；类脑计算

#### AI 发展技术形态：

从数据到知识到决策的大数据智能、多模态智能、群体智能、人机混合的增强智能、机器人的智能自主系统
{总而言之是大量的具备学习探索能力、独立交互各类信息、人在回路的融合社会}

## 1 搜索 Search





## 2 表示与推理 Representation and Reasoning

知识表示方法：





## 3 决策与智能体 Decision-Making and Agent





## 4 系统架构 System Architecture