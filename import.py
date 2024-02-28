import fibo
fibo.fib(50)
print("\n")
print(fibo.__name__)


from fibo import fib
fib(50)


from fibo import fib as fibonacci
fibonacci(50)


import fibo, sys
dir(sys)
