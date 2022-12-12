import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def ralston(f, x0, y0, n):
    r = []
    x_values = [0.39715, 0.43151, 0.48282, 0.54861, 0.56724, 0.64274, 0.69878, 0.71704, 0.79323, 0.83613, 0.90048, 0.91698, 1.00124, 1.05271, 1.06599, 1.12968, 1.17063, 1.22839, 1.29276, 1.34227]
    h = x_values[0] - x0
    for _ in range(n):
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + (3/4) * h, y0 + (3/4) * h * m1)
        y1 = y0 + h * (m1 + 2 * m2) / 3
        x0 = x_values[_]
        y0 = y1
        r.append( (x0, y0) )
    return r

if __name__ == '__main__':

    def f(x, y):
        return y * (2 - x) + x + 1

    x0 = 0.36012
    y0 = 1.59504
    n  = 20
    r = ralston(f, x0, y0, n)
    for ri in r:
        print(ri[1],',')

    # x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
