import math

def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        #realizar as iterações
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores
        x0 += h
        y0 = yk
        #colocando valores na lista
        r.append((x0, y0))
    return r

if __name__ == "__main__":
    #exemplo
    #y'= 1+xy, y(1)=2
    def f(x, y):
        return y*(1 - x) + x + 2

    x0 = 1.687
    y0 = 2.7642
    h = 0.1092
    n=15
    r = rk4(f, x0, y0, h , n)
    for ri in r:
        print(ri[1],',')