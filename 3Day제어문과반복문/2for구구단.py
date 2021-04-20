# 구구단 출력
num = int(input("구구단 몇 단을 계산할까? \n"))
print("구구단 %d단을 계산한다. " % num)

for i in range(1, 10):
    print("%d x %d = %d" % (num, i, num*i))
