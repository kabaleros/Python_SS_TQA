# Вести значення (рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні.
# Ввести три значення (рік, місяць, день) у відповідні зміннію Визначити чи введені дані відповідають коректному запису дати.
# Для довільних чисел a, b i c визначти чи має рівняння ax2+bx+c=0 хоча б один дійсний коршнь і якщо так, то видрукувати його
# Задана три довільних числа. Визначити , чи модна побудувати трикутник з такими довжинами сторін. Якщо так, то видрукувати його периметр та площу.
# Нехай k - ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, ..., субота чи неділя) залежно від того,
# на який день тижня припадає k-й день не високосного року, в якому перше січня - понеділок.

a = float(input("Input a" + "\n"))
b = float(input("Input b" + "\n"))
c = float(input("Input c" + "\n"))
D=b**2-4*a*c

if a == 0:
    print("there is one root", -c/b)
elif D < 0:
    print("there are no roots")
elif D == 0:
    print("there is one root", -b/(2*a))
else:
    print("there are two distinct roots",(-b*+D**0.5)/(2*a),",", (-b-D**0.5)/(2*a))
