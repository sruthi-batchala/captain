def fibonacci(n):
    if n<0:
        pass
    elif n==1:
        return 0
    elif n==2:
        return 1
    elif n>2:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input('enter the number:'))
print(fibonacci(n))
