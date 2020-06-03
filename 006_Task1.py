# 1. Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence
# n - length of Fibonacci sequence.
# NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...

def fibo(n):
    f_list = [1]
    if n <= 0:
        return("Incorrect input")
    elif n == 1:
        return f_list
    else:
        f_list.append(1)
        while len(f_list) < n:
            k = f_list[len(f_list) - 2] + f_list[len(f_list) - 1]
            f_list.append(k)
    return f_list
