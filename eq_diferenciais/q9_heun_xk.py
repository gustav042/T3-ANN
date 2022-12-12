import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def heun(f, x0, y0, n):
    r = []
    x_values = [0.81805, 0.85861, 0.93024, 0.97932, 1.00611, 1.08869, 1.1414, 1.15883, 1.21721, 1.27831, 1.33106, 1.39079, 1.41104, 1.47968, 1.53188, 1.57323, 1.61461, 1.66171, 1.72623, 1.78696]
    h = x_values[0] - x0
    for _ in range(n):
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h * (m1 + m2) / 2
        x0 = x_values[_]
        y0 = y1
        r.append( (x0, y0) )
    return r

if __name__ == '__main__':

    def f(x, y):
        return  y * (2 - x) + x + 1
    
    x0 = 0.79913 
    y0 = 1.67611

    n  = 20
    r = heun(f, x0, y0, n)
    for ri in r:
        print(ri[1],',')

    # x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
