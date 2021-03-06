#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_13.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 10.05.2019
# дата последней модификации: 10.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать прямоугольную матрицу A, имеющую N строк и M столбцов со
# случайными элементами. Разделить элементы каждого столбца матрицы на
# элемент этого столбца с наибольшим значением.
#версия Python: 3.6

import numpy as np
import random

N = np.random.randint(2,10)
M = np.random.randint(2,10)

print(N,M)

matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

col_max = np.max(matrix, axis=0)
matrix = matrix / col_max
print("Полученная матрица:\r\n {}".format(matrix))
