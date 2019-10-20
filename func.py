import numpy as np
def Relax(A,b,w,E):
    x = np.zeros_like(b)
    it_count = 0
    while (True):
        print("Итерация ", it_count, " решение на данной итерации:", x)
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * x[j]
            x_new[i] = (1 - w) * x[i] + (w / A[i][i]) * (b[i] - sigma)

        exit = False
        for n in range(0, A.shape[0]):
            if abs(x_new[n] - x[n]) <= E:
                exit = True
        if exit == True:
            break
        x = x_new
        it_count += 1

    print()
    print("Решение системы: ")
    print(x)

    error = np.dot(A, x) - b
    print()
    print("Погрешность: ")
    print(error)
    pass

