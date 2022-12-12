def f(x, y):
    return y * (2 - x) + x + 1

def euler_mid(f, x0, y0, h, n):
    y = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        print(y0,',')
    return y

if __name__ == '__main__':
    
    # t == x
    x0 = 1.95308
    y0 = 2.87605    
    n = 15
    h = 0.1849
    r1 = euler_mid(f, x0, y0,h, n)
