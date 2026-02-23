---
title: 优化
date: "2025-06-11"
weight: 3
tags: ["Math", "Algorithm", "Optimization"]
draft: false
---
{{< katex >}}

## 笔记

<div class="pdf-full" style="margin:1rem 0;">
  <iframe src="./optim_notes.pdf"
          width="100%"
          height="800"
          style="border:1px solid #e5e7eb; border-radius:8px;"
          allowfullscreen>
    你的浏览器不支持内嵌 PDF，点击 <a href="./optim_notes.pdf">这里下载</a>。
  </iframe>
</div>

---

## 重要算法示例

- 次梯度

    ```Python
    def subgradient_method(f, subgrad_f, x0, step_size_rule='constant', R=1.0, G=1.0, k_max=1000):
        x = x0
        for k in range(k_max):
            g = subgrad_f(x)
            if step_size_rule == 'constant':
                alpha = R / (G * sqrt(k+1))
            elif step_size_rule == 'Polyak':
                fk = f(x)
                alpha = (fk - f_star) / (norm(g)**2)
            x = x - alpha * g
            x = project_to_C(x)
        return x
    ```

- 近端梯度

    ```Python
    def proximal_gradient(grad_f, prox_h, x0, L, k_max=1000):
        x = x0
        for k in range(k_max):
            x = prox_h(x - (1/L) * grad_f(x))
        return x

    # Proximal Operators
    def prox_l1(x, gamma):
        return sign(x) * max.(abs(x) - gamma, 0)

    def prox_l2(x, gamma):
        return x / (1 + gamma)

    def prox_indicators(x, gamma, C):
        return project_to_C(x)

    def prox_group_lasso(x, gamma, groups):
        x_new = copy(x)
        for g in groups:
            norm_g = norm(x[g])
            if norm_g > gamma:
                x_new[g] = (1 - gamma/norm_g) * x[g]
            else:
                x_new[g] = 0
        return x_new
    ```

- FISTA
  
  ```Python
  def fista(g, grad_g, prox_h, x0, L, k_max=1000):
    x = x0
    y = x0
    t = 1
    for k in range(k_max):
        x_old = x
        x = prox_h(y - (1/L) * grad_g(y), 1/L)

        t_new = (1 + sqrt(1 + 4*t**2)) / 2
        y = x + ((t - 1) / t_new) * (x - x_old)
        t = t_new

        if norm(x - x_old) < 1e-12:
            break   
    return x
  ```

- ADMM

  ```Python
  def admm(f, g, A, B, c, prox_f, prox_g, x0, z0, rho=1.0, k_max=1000):
    n = len(x0)
    m = len(z0) 
    x = x0
    z = z0
    u = zeros(n)
    history = []
    for k in range(k_max):
        # min_x f(x) + (rho/2)||Ax + Bz - c + u||^2
        x = prox_f(x, 1/rho, A, B, z, c, u)
        # min_z g(z) + (rho/2)||Ax + Bz - c + u||^2
        z = prox_g(z, 1/rho, A, B, x, c, u)
        # dual
        u = u + (A @ x + B @ z - c)
        
        r_pri = norm(A @ x + B @ z - c)
        r_dual = rho * norm(A.T @ (z - z_old)) if k > 0 else inf
        history.append((r_pri, r_dual))

        if r_pri < 1e-6 and r_dual < 1e-6:
            break
    return x, z, history
  ```
