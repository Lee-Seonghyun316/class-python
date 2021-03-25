repeat = True

while repeat:
    num = int(input("구구단 몇 단을 계산할까? \n"))

    if num == 0:
        repeat = False
        break
    elif num >= 10:
        print("error!")
        break
    else:
        print("구구단 %d단을 계산한다. " % num)
        for i in range(1, 10):
            print("%d x %d = %d" % (num, i, num*i))
