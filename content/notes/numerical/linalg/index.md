---
title: 数值
date: "2026-01-12"
weight: 2
tags: ["Math", "Algorithm", "Numerical", "Linear Algebra", "Analysis"]
draft: false
---
{{< katex >}}
## 小结

{对于开篇提出的三大类基础数值问题，第二类最小二乘的大纲放入线性方程组中}

### 线性方程组 $Ax=b$

- **直接**

  - LU
    - Gauss 消去
    - Doolittle/Crout，Cholesky（或 LDL'）
    - Pivoting（PLU）
  - QR
    - GS 正交化（经典col/修正row）CGS, MGS, CGS2
    - Householder
    - Givens
  - SVD
  - 稀疏直接法
  - 特殊（Toeplitz，FFT，块）

- **迭代**

  - 定常

    - 分裂（$A=M-N, \rho(M^{-1}N)<1$，（弱）正则分裂，M-阵/H-阵）
      - Jacobi
      - Gauss-Seidel
      - SOR（或 SSOR）相容次序（Young's Thm）
      - Richardson
    - 交替方向 e.g. ADI

  - Krylov 子空间

    对称

    - CG（PCG）
    - MINRES

    非对称

    - GMRES
    - BiCG，QMR（$\in$ Petrov-Galerkin）
    - CG^2

    正规

    - CG for AA'/A'A

  - Multigrid

    - 几何
    - 代数

  - 区域分解 Domain Decomp.

    - 重叠 Schwartz
    - 非重叠 e.g. FETI, Neumann

- **技术**

  - 预条件 {见下}

  - 混合策略

    - 直接-迭代
    - 多级迭代

  - 专门问题

    - **最小二乘** $\min_x \|Ax-b\|^2_2$，超定

      直接

      - Normal（NC, NG）
      - QR
      - SVD

      迭代

      - Krylov e.g. NCG, LSQR/LSMR
      - Kaczmarz（Proj.）
      - （On-Line）SGD，RLS

      正则化 for 病态/秩亏

      - Truncated SVD
      - Tikhonov（L2），Damp LS i.e. 信任域's dual
      - Early-Stopping

      变体

      - Weighted
      - Constrained
      - Total
      - Sparse e.g. LASSO
      - Robust

    - 欠定（L0 norm，降维（e.g. 线性，随机 i.e. sketch $\Pi Ax-\Pi b$））

    - 鞍点 e.g. Uzawa

  - 并行

  - 学习型（自适应）

### 特征值问题 $Ax=\lambda x$

- **稠密**
  - QR（对称tridiag/非对称upper Hessenberg，buldge chasing）
  - 分治 D&C
  - Jacobi（经典max/循环/阈值）

- **迭代**

  - 单向量
    - 幂法
    - 反幂法
    - RQI（反幂自适应移位）
  - 区间
    - 二分法（计数 by Sturm 序列或惯性）
    - 谱切片
  - 投影
    - Ritz（$V^\prime AVy_i=\theta_iy_i$）
      - Krylov e.g. Arnoldi, Lanczos
      - (Jacobi-)Davison
      - 正交迭代（子空间迭代）
      - Rayleigh-Ritz Gradient（SGD, CG）
    - Petrov-Galerkin
  - 特殊（tridiag, Toeplitz）

- **技术**

  - 加速收敛
    - Preconditioner
      - 不完全分解 e.g. IC, ILU
      - 近似逆 e.g. AINV, SPAI
      - Multigrid
      - Domain Decomp.
    - 谱变换 i.e. 滤波 Filter
      - 多项式 e.g. Chebyshev
      - 有理 e.g. shift + invert iter. $(A-\mu I)^{-1}$, Cayley（Mobius transf.）, contour integral
    - 重启 Restart（隐式）e.g. IRA

  - 并行（块方法）e.g. LOBPCG, 块 Krylov

  - 变体

    - 广义特征值 $A-\lambda B$

    - 奇异值 e.g. Golub-Kahan

  - 内部特征值 {见上}

    - 子空间（直接）e.g. Rayleigh-Ritz, Ortho. Iter., Lanczos

    - Filter
    - 区间（二分，切片）
    - 收缩 Deflation（已有 eigenpairs 逐步）
      - Hotelling/Wielandt $A-\lambda_1v_1v_1'$
      - Ortho. Proj. $x\perp v_1$, Locking

## 笔记

<div class="pdf-full" style="margin:1rem 0;">
  <iframe src="./scripts.pdf"
          width="100%"
          height="800"
          style="border:1px solid #e5e7eb; border-radius:8px;"
          allowfullscreen>
    你的浏览器不支持内嵌 PDF，点击 <a href="./scripts.pdf">这里下载</a>。
  </iframe>
</div>