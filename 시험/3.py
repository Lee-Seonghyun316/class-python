# 조금 뒤 수정
repeat = True

while repeat:
    num = int(input("(1-9)중 하나의 숫자를 입력하시오 \n"))

    if num <= 0:
        print("error!")
        break
    # 0이면 끝내기
    elif num >= 10:
        print("error!")
        break
    # 조건에 안맞으면 에러발생
    else:
        print("구구단 계산")
        for j in range(1, 10):
            for i in range(1, num+1):
                print("%d x %d = %d" % (i, j, i*j), end='    ')
            print()
