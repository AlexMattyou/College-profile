def recurFib(n):
    if n<= 1:
        return n
    else:
        return recurFib(n-1)+recurFib(n-2)
n = 7
print('Using Recursion:')
if n == 0: print(n)
else: 
    for i in range(n):
        print(recurFib(i), end=' ')
    print()
        
def fib(n):
    f,s = 0,1 
    while (n>0):
        print(f, end=' ')
        f,s = s, f+s
        n = n-1

print('Without using recursion:')     
fib(n)
