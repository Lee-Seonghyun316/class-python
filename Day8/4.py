import math
# Day8 폴더 안에 있어야 실행 된다!

f = open("./Day8/4.txt", 'r')
data = f.read()


f.close()
# writedata.py
f = open("./Day8/4.txt", 'a')
a = data.split("\n")
for i in range(0, len(a)):
    a[i] = float(a[i])

average = sum(a)/len(a)

b = math.floor(average*10)/10
f.write('\n'+str(b))
f.close()
