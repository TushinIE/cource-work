#имя проекта: numpy-example
#номер версии: 1.0
#имя файла: example_20.py
#автор и его учебная группа: И.Тушин, ЭУ-142
#дата создания: 12.05.2019
# дата последней модификации: 12.05.2019
#связанные файлы: пакеты numpy, matplotlib
# описание: Создать квадратную матрицу A, имеющую N строк и N столбцов со
# случайными элементами. Определить произведение элементов,
# расположенных параллельно побочной диагонали (ближайшие к побочной).
# Элементы побочной диагонали имеют индексы от [N,0] до [0,N].
#версия Python: 3.6

import numpy as np

N = 4


A = np.random.randint(low=-9, high=10, size=(N, N))
print("Матрица:\r\n{}".format(A))

diagonal_elements = np.array([np.diagonal(A[::-1], i) for i in [1, -1]]).flatten()
print("Элементы, расположенные параллельно побочной диагонали:")
print(diagonal_elements)

print("Сумма элементов, расположенные параллельно побочной диагонали:")
print(np.prod(diagonal_elements))