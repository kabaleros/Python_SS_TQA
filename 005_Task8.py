# 1. Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
# 2. Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.
# 3. Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
# 4. Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації. Програма будує список слів, знаки пунктуації виключаються.
#    Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації, за винятком відкриває дужки (пробіл перед нею).
# 5. Дана матриця. Знайти в ній рядок з максимальною сумою елементів, а також стовпець.
# 6. Генерується квадратна матриця. Знайти сума елементів її головнї та побічної діагоналей.
#    Головна діагональ йде з верхнього лівого кута в правий нижній, побічна - з верхнього правого кута в лівий нижній.
# 7. Дана матриця цілих чисел. Вводиться число. З'ясувати, які рядки і стовпці матриці містять дане число.
# 8. Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
file = input('Input a file:' + '\n')
filelist = file.split(".")
if filelist[1] in extensions:
    print("Extension is acceptble")
else:
    print("Extension is unacceptble")