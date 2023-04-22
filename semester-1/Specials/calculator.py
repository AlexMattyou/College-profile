def add(a,b):return a + b
def sub(a,b):return a - b
def mul(a,b):return a * b
def div(a,b):return a / b

print(">> Enter 'x' to exit\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Divition")

ans = 0
while 1:
  opp = input("Select your operation {1,2,3,4}: ")
  if opp in ['x','X']:break
  elif opp not in ['1','2','3','4']:continue
  opp = int(opp)-1
  print(">> Input 'ans' to include last answer")
  n1,n2 = tuple(map(str,input('n1,n2: ').split(',')))
  n1 = ans if n1=='ans' else int(n1)
  n2 = ans if n2=='ans' else int(n2)
  func = [add(n1,n2),sub(n1,n2),mul(n1,n2),div(n1,n2)]
  ans = func[opp]
  print('= ',ans)