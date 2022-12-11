import math
import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, n):
    result = []
    x_values = [1.85255, 1.90705, 1.95647, 2.01295, 2.04876, 2.12828, 2.14712, 2.22144, 2.25285, 2.31169, 2.36565, 2.40544, 2.47376, 2.4941, 2.56359, 2.5906, 2.65598, 2.72291, 2.77664, 2.79584]   
    h = x_values[0] - x0
    for i in range(n):
        if (i>=1):
            h = x_values[i] - x_values[i-1]
        y0 += f(x0, y0) * h
        x0 = x_values[i]
        result.append([x0, y0])
        #print(x0,y0)
        print(y0, ',')
        
    return result

if __name__ == '__main__':

    def f(x, y):
         return  y * (1 - x) + x + 2

    x0 = 1.83347
    y0 = 1.7933
    n = 20 #ate onde k vai
    #k = 0.0712

    #P3.7
    # def f(x, y):
    #     return y*(1 - x) + x + 2

    # x0, y0 = 1.47205, 2.16382
    # h = 0.13102
    # n = 10

    resposta = euler(f, x0, y0, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
