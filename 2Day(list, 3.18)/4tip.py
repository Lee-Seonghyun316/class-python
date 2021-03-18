food = int(input("음식 비용을 입력 하시오 : "))
tip = int(input("팁 비율을 입력하시오(%) : "))
result = food+food*(tip/100)
print("당신의 지불해야 하는 총 금액은 ", result, "원 입니다. ")
