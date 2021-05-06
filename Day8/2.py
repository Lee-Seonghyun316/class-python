# Day8 폴더 안에 있어야 실행 된다!

f = open("./Day8/1.txt", 'r')
data = f.read()
f.close()

# writedata.py
f = open("./Day8/2의 결과.txt", 'w')
a = data.split()
b = ''
for i in range(0, len(a)):
    b += a[i]
print(b)
print(len(b))
for i in range(0, len(b)):
    c = b[i] + '\n'
    f.write(c)
f.close()
