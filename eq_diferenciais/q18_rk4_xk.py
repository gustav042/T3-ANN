import math

def rk4(f, x0, y0, n):
    r = []
    x_values = [1.1336, 1.1808, 1.2241, 1.2575, 1.3364, 1.3772, 1.4254, 1.4837, 1.5261, 1.5639, 1.6318, 1.6698, 1.7458, 1.7882, 1.8095, 1.8672, 1.9162, 1.9643, 2.0079, 2.0792]
    h = x_values[0] - x0
    for _ in range(n):
        #realizar as iterações
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores
        x0 = x_values[_]
        y0 = yk
        #colocando valores na lista
        r.append((x0, y0))
    return r

if __name__ == "__main__":
    #exemplo
    #y'= 1+xy, y(1)=2
    def f(x, y):
        return y*(1 - x) + x + 2

    x0 = 1.1014
    y0 = 0.9551
    n=20
    r = rk4(f, x0, y0, n)
    for ri in r:
        print(ri[1],',')