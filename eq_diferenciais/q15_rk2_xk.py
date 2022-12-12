import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2
'''
Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.126 e y0=1.922. Use o método de Runge-Kutta de ordem 2 com b=0.689 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.132.
'''

def RK2(f, x0, y0, n, b):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    x_values = [0.42835, 0.44251, 0.52833, 0.56585, 0.62136, 0.65103, 0.6932, 0.75271, 0.82481, 0.87474, 0.89289, 0.94237, 1.01641, 1.07557, 1.12016, 1.1705, 1.22317, 1.24902, 1.32759, 1.37915]
    h = x_values[0] - x0
    for _ in range(n):
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0,y0)
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 = x_values[_]
        yield [x0,y0]


#Q11 Prova:
def f(x,y):
    return y*(1-x)+x+2


x0 = 0.38418
y0 = 2.43469
b = 0.93214
n=20
e = RK2(f,x0,y0,n, b)
for yi in e:
    print(yi[1],',')

