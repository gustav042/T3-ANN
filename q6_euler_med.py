def f(x, y):
    return y * (2 - x) + x + 1

def euler_mid(f, x0, y0, n):
    y = []
    x_values = [0.3273, 0.38924, 0.42497, 0.48435, 0.52965, 0.57724, 0.61529, 0.68711, 0.71234, 0.79111, 0.84055, 0.89476, 0.91618, 0.98659, 1.00889, 1.07548, 1.14126, 1.19082, 1.23237, 1.26057]    
    h = x_values[0] - x0
    for _ in range(n):
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 = x_values[_]

        print(y0,',')
    return y

if __name__ == '__main__':
    
    # t == x
    x0 = 0.30367
    y0 = 0.97074
    n = 20
    r1 = euler_mid(f, x0, y0, n)
