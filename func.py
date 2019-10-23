import numpy as np
def Relax(A,b,w,E):
    maxA = 0
    for i in range(0, A.shape[0]):
        if A[i, i] > maxA:
            maxA = A[i, i]
    x = b / maxA
    it_count = 1
    while (True):
        x_new = b/maxA
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * x[j]
            x_new[i] = (1 - w) * x[i] + (w / A[i][i]) * (b[i] - sigma)

        iter = 0
        for n in range(0, A.shape[0]):
            if abs(x_new[n] - x[n]) <= E:
                iter += 1

        x = x_new
        print("Итерация ", it_count, " решение на данной итерации:", x)
        if iter == 3:
            break
        it_count += 1

    print()
    print("Решение системы: ")
    print(x)

    error = np.dot(A, x) - b
    print()
    print("Погрешность: ")
    print(error)
    pass

