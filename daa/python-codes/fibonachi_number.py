def fib(n, cnt = 0):
    cnt += 1
    if n <= 1:
        return n, cnt
    fib_n1, cnt = fib(n - 1, cnt)
    fib_n2, cnt = fib(n - 2, cnt)
    return fib_n1 + fib_n2, cnt

n = input("Enter the position of fibonachi no: ")
fib_ans, cnt = fib(int(n))
print(fib_ans, cnt)