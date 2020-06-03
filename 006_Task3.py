# 1. Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence
# n - length of Fibonacci sequence.
# NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
# 2. Provide full program code of fibo_element(n) function which returns element of Fibonacci sequence which index has a value equal n.
# n - index of element of Fibonacci sequence.
# NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....
# 3. Provide full program code of parse_number(num) function which returns the dict with following structure:
# {odd: number of odd digits in input value, even: number of even digits of input value} or false when wrong input value.
# num - input number.
# NOTE: Assume that the "zero" digit also belongs to even numbers
# a = '1234'
# num = []
# for i in a:
#     i = int(i)
#     num.append(i)
# print(num)

def parse_number(num):
    if int(num):
        num = str(num)
        lst = []
        # print(num)
        for x in num:
            x = int(x)
            lst.append(x)
            print(lst)
            odd = [x for x in lst if x % 2 == 1]
            even = [x for x in lst if x % 2 == 0]
        print(odd)
        print(even)
    else:
        return "False"


# odd = [x for x in a if x%2 == 1]
# even = [x for x in a if x%2 == 0]
# print("Quantity of odd numbers is", len(odd))
# print("Quantity of even numbers is", len(even))


print(parse_number(34567))
print(parse_number(100))
print(parse_number("word"))
