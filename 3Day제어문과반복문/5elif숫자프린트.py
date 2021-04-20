# 두수의 크기비교

first = int(input("1번쨰 숫자: "))
second = int(input("2번쨰 숫자: "))

if first > second:
    print("처음 입력했던 %d가 %d 보다 더 큽니다. " % (first, second))
    # 숫자입력
elif second > first:
    print("나중에 입력했던 %d가 %d 보다 더 큽니다. " % (second, first))
else:
    print("두 숫자가 같습니다. ")
