import numpy as np


def Relax(A, b, w, E):
    maxA = 0
    for i in range(0, A.shape[0]):
        if A[i, i] > maxA:
            maxA = A[i, i]
    x = b / maxA
    it_count = 1
    while (True):
        x_new = b / maxA
        for i in range(0, A.shape[0]):
            # print("A[i, :i]: ", A[i, :i])
            # print("x_new[:i]: ", x_new[:i])
            s1 = np.dot(A[i, :i], x_new[:i])
            # print("s1: ", s1)
            # print("A[i, i + 1:]: ", A[i, i + 1:])
            # print("x[i + 1:]: ", x[i + 1:])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            # print("s2: ", s2)
            # print("x_new",[i]," = " ,b[i]/ A[i, i]," - ",s1/ A[i, i]," - ",s2/ A[i, i])
            x_new[i] = (1 - w) * x[i] + (w / A[i, i]) * (b[i] - s1 - s2)

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


def SpeedDescent(A, b, E):
    maxA = 0
    for i in range(0, A.shape[0]):
        if A[i, i] > maxA:
            maxA = A[i, i]
    x = b / maxA
    it_count = 1
    while (True):
        x_new = b / maxA
        r = np.dot(A, x) - b
        # print("r: ",r)
        # print("(r,r): ",np.dot(r,r))
        # print("(A*r,r): ", np.dot(np.dot(A,r),r))
        t = np.dot(r, r) / np.dot(np.dot(A, r), r)
        # print("t: ",t)
        # print("x_new = ", x ," - ",t*r)
        x_new = x - t * r
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
