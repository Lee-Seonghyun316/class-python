print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다. ")
print("변환하고 싶은 섭씨 온도, 학번, 이름을 공백을 두고 입력하세요. ")
info = input().split(' ')
tem_F = (float(info[0]))*1.8+32
print("섭씨온도 : ", float(info[0]), ", 화씨온도 : ",
      tem_F, ", 학번 : ", info[1], ", 이름 : ", info[2])
