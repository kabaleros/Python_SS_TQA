# 1. Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
# 2. Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.
# 3. Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
# 4. Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації. Програма будує список слів, знаки пунктуації виключаються.
#    Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації, за винятком відкриває дужки (пробіл перед нею).
# 5. Дана матриця. Знайти в ній рядок з максимальною сумою елементів, а також стовпець.
# 6. Генерується квадратна матриця. Знайти сума елементів її головнї та побічної діагоналей.
#    Головна діагональ йде з верхнього лівого кута в правий нижній, побічна - з верхнього правого кута в лівий нижній.
from random import random
N = 5
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)
for row in matrix:
    print(row)
m_diag = [row[matrix.index(row)] for row in matrix]
print("Sum of elements in main diagonal is", sum(m_diag), "elements are", m_diag)
o_diag = [row[len(matrix) - matrix.index(row)-1] for row in matrix]
print("Sum of elements in other diagonal is", sum(o_diag), "elements are", o_diag)
