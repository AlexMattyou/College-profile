def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    next = n+1
    while not is_prime(next):
        next += 1
    return next

# Based on linear proping
def hash(arr, l = 0):
    if l == 0:
        l = len(arr)
    l = next_prime(l)
    hashed = [None for x in range(l)]
    for n in arr:
        pos = n % l
        while not hashed[pos] == None:
            pos += 1
            if pos == len(hashed):
                pos = 0
        hashed[pos] = n
    hashed.append(l)
    return hashed

def search(arr,item):
    arr,hash = arr[:-1],arr[-1]
    pos = item % hash
    if arr[pos] == item:
        return pos
    else:
        cur = int(pos)
        while not arr[pos] == item:
            pos += 1
            if pos == len(arr):
                pos = 0
            if cur == pos:
                return -1
        return pos

arr = [38,35,85,26,35,86]
print(arr)
arr = hash(arr)
print(arr)
a = search(arr,85)
print(85,a)
b = search(arr,38)
print(38,b)
c = search(arr,27)
print(27,c)