import numpy as np

import func

var = 0
while var not in [1, 2]:
    var = int(input("Выберете метод 1 - релаксации, 2 - скорейшего спуска: "))

E = -1
while E < 0:
    E = float(input("Введите погрешность: "))

w = -1
if var == 1:
    while w < 0 or w > 2:
        w = float(input("Введите w: "))
# A = np.array([[10, 1, 1],[2, 10, 1],[2, 2, 10]])
A1 = np.array([[6.25, -1, 0.5], [-1, 5, 2.12], [0.5, 2.12, 3.6]])
A2 = np.array([[2.65, -1.27, 0.18], [-1.27, 2.73, -0.46], [0.18, -0.46, 2.16]])
print()
# b = np.array([12, 13, 14])
b1 = np.array([7.5, -8.68, -0.24])
b2 = np.array([2.25, 0.93, 1.33])

if var == 1:
    print("Система 1: ")
    for i in range(A1.shape[0]):
        row = ["{} * x{}".format(A1[i, j], j + 1) for j in range(A1.shape[1])]
        print(" + ".join(row), "=", b1[i])
    print()
    func.Relax(A2, b2, w, E)

if var == 2:
    print("Система 2: ")
    for i in range(A2.shape[0]):
        row = ["{} * x{}".format(A2[i, j], j + 1) for j in range(A2.shape[1])]
        print(" + ".join(row), "=", b2[i])
    print()
    func.SpeedDescent(A2, b2, E)
