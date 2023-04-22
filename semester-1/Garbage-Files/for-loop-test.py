a = [1,2,3,4,5]
def circulate(n,a):
    if n == 0: return a
    a = a[1:]+a[:1]
    return circulate(n-1,a)

print(circulate(201,a))