def euler_method(f, r, iterations, initial_point):
    h = (r[1] - r[0]) / iterations
    w = initial_point
    t = 0
    for i in range(0, iterations):
        w = w + h * f(t, w)
        t += h
    
    return w

def runge_kutta(f, r, iterations, initial_point):
    h = (r[1] - r[0]) / iterations
    w = initial_point
    t = 0
    for i in range(0, iterations):
        k1 = h * f(t, w)
        k2 = h * f(t + h / 2, w + (1/2) * k1)
        k3 = h * f(t + h / 2, w + (1/2) * k2)
        k4 = h * f(t + h, w + k3)
        w = w + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return w

if __name__ == "__main__":
    def f(t, y):
        return t - y*y
    
    e_m = euler_method(f, [0, 2], 10, 1)
    print(e_m)

    r_k = runge_kutta(f, [0, 2], 10, 1)
    print(r_k)