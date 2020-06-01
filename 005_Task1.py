# Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
import random
# even = odd = 0
a = []
for i in range(10):
    a.append(int(random.random() * 100))
print(a)
odd = [x for x in a if x%2 == 1]
even = [x for x in a if x%2 == 0]
print("Quantity of odd numbers is", len(odd))
print("Quantity of even numbers is", len(even))
