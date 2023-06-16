class Matrix:
    def __init__(self, inp, size = (0,0), type = 'list'):
        if len(inp) == 0:
            inp = [0 for x in range(size[0]*size[1])]
        self.raw = inp
        self.size = size
        self.matrix = self.convert(inp) if type == 'list' else inp
        
    def convert(self,inp):
        column, c = [], 0
        for i in range(self.size[0]):
            row = []
            for j in range(self.size[1]):
                row += [inp[c]]
                c += 1
            column += [row]
        return column
    
    def _operation(self,opp,inp = 0):
        if inp == 0: inp = self.matrix
        elif isinstance(inp, list):
            inp = Matrix(inp,self.size,'mat')
        column= []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])): # type: ignore
                if opp == 'add':
                    row += [self.matrix[i][j] + inp.matrix[i][j]] # type: ignore
                elif opp == 'sub':
                    row += [self.matrix[i][j] - inp.matrix[i][j]] # type: ignore
                elif opp == 'div':
                    row += [self.matrix[i][j] / inp.matrix[i][j]] # type: ignore
                elif opp == 'T':
                    row+= [self.matrix[j][i]] # type: ignore
                elif opp == 'I':
                    row+= [1 if j == i else 0]
                elif opp == 'mul':
                    val = 0
                    for k in range(len(self.matrix)):
                        val += self.matrix[i][k] * inp.matrix[k][j] #type: ignore
                    row += [val]
            column += [row]
        return Matrix(column,self.size, 'mat')
    def T(self):return self._operation('T')
    def I(self):return self._operation('I')
    def __add__(self, inp):return self._operation('add',inp)
    def __sub__(self, inp):return self._operation('sub',inp)
    def __mul__(self, inp):return self._operation('mul',inp)
    
    def display(self):
        gap = len(str(max(max(self.matrix)))) # type: ignore
        print(f"{self.size[0]}X{self.size[1]} MATRIX  ->[")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])): # type: ignore
                print(self.matrix[i][j], end=' '*(gap-len(str(self.matrix[i][j]))+1)) # type: ignore
            print()
        print(']')

null = Matrix([],[3,3])
(print(null.matrix))
A = Matrix([1,2,2,3],(2,2))
A.display()
B = Matrix([2,4,6,1],(2,2))
B.display()
C = B * A
C.display()
C.T().display()
null.I().display()
D = Matrix([153,263,845,404,258,956],(2,3))
D.display()

# One useful thing I learned is Pandas and Numpy are ADT, and we can also create one like that 🔷
# But these code have no use
