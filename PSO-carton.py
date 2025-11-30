import numpy as np

# ==========================================================
# 1. Hàm mục tiêu: diện tích bề mặt S cần tối thiểu hóa
# ==========================================================
def surface_area(x, V):
    """
    x = [L, W], chiều dài và chiều rộng
    H = V / (L * W)
    Mục tiêu: Minimize S = 2(LW + LH + WH)
    """
    L, W = x
    if L <= 0 or W <= 0:
        return 1e30
    H = V / (L * W)
    return 2 * (L*W + L*H + W*H)


# ==========================================================
# 2. Hàm khởi tạo swarm
# ==========================================================
def init_swarm(n_particles, bounds):
    dim = len(bounds)
    X = np.zeros((n_particles, dim))
    V = np.zeros((n_particles, dim))

    for d in range(dim):
        low, high = bounds[d]
        X[:, d] = np.random.uniform(low, high, n_particles)
        V[:, d] = np.random.uniform(-abs(high-low), abs(high-low), n_particles)

    return X, V


# ==========================================================
# 3. PSO liên tục cơ bản
# ==========================================================
def pso_carton(V, n_particles=40, n_iterations=500):
    # Giới hạn kích thước thùng: bạn có thể chỉnh nếu muốn
    bounds = [(1, 100), (1, 100)]  # L, W từ 1 đến 100 cm

    dim = 2
    X, Velocity = init_swarm(n_particles, bounds)

    # Đánh giá ban đầu
    fitness = np.array([surface_area(x, V) for x in X])

    pbest = X.copy()
    pbest_val = fitness.copy()

    # Global best ban đầu
    gbest_idx = np.argmin(pbest_val)
    gbest = pbest[gbest_idx].copy()
    gbest_val = pbest_val[gbest_idx]

    # Tham số PSO
    w = 0.9
    c1 = 1.5
    c2 = 1.5

    for it in range(n_iterations):
        r1 = np.random.rand(n_particles, dim)
        r2 = np.random.rand(n_particles, dim)

        # Cập nhật vận tốc
        Velocity = (
            w * Velocity +
            c1 * r1 * (pbest - X) +
            c2 * r2 * (gbest - X)
        )

        # Cập nhật vị trí
        X = X + Velocity

        # Ép vào bounds
        for d in range(dim):
            low, high = bounds[d]
            X[:, d] = np.clip(X[:, d], low, high)

        # Đánh giá lại
        fitness = np.array([surface_area(x, V) for x in X])

        # update pbest
        improved = fitness < pbest_val
        pbest[improved] = X[improved]
        pbest_val[improved] = fitness[improved]

        # update gbest
        best_idx = np.argmin(pbest_val)
        if pbest_val[best_idx] < gbest_val:
            gbest_val = pbest_val[best_idx]
            gbest = pbest[best_idx].copy()

    L, W = gbest
    H = V / (L * W)
    return L, W, H, gbest_val


# ==========================================================
# 4. Chạy chính
# ==========================================================
def main():
    V = float(input("Nhập thể tích thùng (cm^3): "))

    L, W, H, S = pso_carton(V)

    print("\n=== KẾT QUẢ TỐI ƯU THÙNG CARTON ===")
    print(f"Thể tích yêu cầu: {V} cm^3")
    print(f"L = {L:.4f} cm")
    print(f"W = {W:.4f} cm")
    print(f"H = {H:.4f} cm")
    print(f"Diện tích bề mặt tối thiểu S = {S:.4f} cm^2")


if __name__ == "__main__":
    main()
