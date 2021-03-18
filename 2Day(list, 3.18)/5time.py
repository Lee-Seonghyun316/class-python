second = int(input("변환할 초를 입력하시오 : "))
day = second//86400
hour = (second % 86400)//3600
minutes = ((second % 86400) % 3600)//60
second_real = (((second % 86400) % 3600) % 60) % 60
print(second, "초는 ", day, " 일 ", hour, " 시 ",
      minutes, " 분 ", second_real, " 초 입니다. ")
