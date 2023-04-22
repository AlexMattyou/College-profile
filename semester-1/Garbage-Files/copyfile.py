from shutil import copyfile
copyfile('a.txt', 'b.txt')
f = open('b.txt', 'r')
print(f.read())