# something booring, Array have no use in python. It's old C++ data type. But they said to create something like this lol

class Array:
    def __init__(self,size):
        self.size = size
        self.array = []
    def isFull(self):
        if len(self.array) == self.size: return True
    def isEmpty(self):
        if len(self.array) == 0: return True
    def append(self,val):
        if self.isFull():
            raise Exception("Maximum array size reached")
        self.array.append(val)
    def insert(self,val,pos):
        if self.size <= pos or self.isFull():
            raise Exception("Array index out of range")
        self.array.insert(pos,val)
    def pop(self,pos = -1):
        if self.size <= pos or self.isEmpty():
            raise Exception("Array index out of range")
        self.array.pop(pos)
        
a = Array(4)
print(a.array) # []
a.append(3)
print(a.array) # [3]
a.append(2)
print(a.array) # [3, 2]
a.insert(5,1)
print(a.array) # [3, 5, 2]
a.append(5)
print(a.array) # [3, 5, 2, 5]

b = Array(2)
print(b.array) # []
b.append(6)
print(b.array) # [6]
b.insert(5,0)
print(b.array) # [5, 6]
b.pop()
print(b.array) # [5]
b.append(7)
print(b.array) # [5, 7]
b.append(6)
print(b.array) # Exception: Maximum array size reached