import numpy as np
import func

var = 0
while var not in [1,2]:
    var = int(input("Выберете метод 1 - релаксации, 2 - скорейшего спуска: "))

E = -1
while E < 0:
    E = float(input("Введите погрешность: "))
w = -1
while w < 0 or w > 2:
    w = float(input("Введите w: "))
A = np.array([[6.25, -1, 0.5],[-1, 5, 2.12],[0.5, 2.12, 3.6]])
print()

b = np.array([7.5, -8.68, -0.24])

print("Система:")
for i in range(A.shape[0]):
    row = ["{} * x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

if var == 1:
    func.Relax(A,b,w,E)
if var == 2:
    print()