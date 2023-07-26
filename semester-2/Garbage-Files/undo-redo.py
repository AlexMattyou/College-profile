class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[-1]

class Writer(Stack):
    def __init__(self,path):
        Stack.__init__(self)
        self.path = path
        self.re = []
        f = open(self.path, "w")
        f.write('')
    def read(self, disp = False):
        f = open(self.path, "r")
        if disp:
            print(f.read())
        return f.read()
        
    def write(self,txt,clean = 1):
        w = str(txt)+' '
        f = open(self.path, "a")
        f.write(w)
        self.push(w)
        f.close()
        
    def undo(self):
        state = self.pop()
        self.re.append(state)
        content = self.read().split(state)
        content = content[0] + content[-1]
        f = open(self.path, "w")
        f.write(content)
    def redo(self):
        state = self.re.pop()
        self.write(state,0)
    
a = Writer("./test-file.txt")
a.write("The first sentence.")
a.write("second")
a.write("third")
a.read(1)
a.undo() 
a.undo()
a.read(1)
a.redo()
a.read(1)


# D:/Projects/Git/College-profile/semester-2/Garbage-Files/test-file.txt

# f = open(path, "r")
# print(f.read())