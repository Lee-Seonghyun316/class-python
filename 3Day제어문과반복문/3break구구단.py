# 무한루프 구구단출력
repeat = True

while repeat:
    num = int(input("구구단 몇 단을 계산할까? \n"))

    if num == 0:
        repeat = False
        break
    # 0이면 끝내기
    elif num >= 10:
        print("error!")
        break
    # 조건에 안맞으면 에러발생
    else:
        print("구구단 %d단을 계산한다. " % num)
        for i in range(1, 10):
            print("%d x %d = %d" % (num, i, num*i))
