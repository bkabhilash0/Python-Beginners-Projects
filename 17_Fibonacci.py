def fib_recurrsion(n):
    if n == 1:
        return 0
    elif n == 2:  
        return 1
    else:
        return fib_recurrsion(n-1) + fib_recurrsion(n - 2)

def fib_sequence(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c)

print(fib_recurrsion(9))
fib_sequence(9)
