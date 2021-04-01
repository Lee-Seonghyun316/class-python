f = (1.8, 32)
print("본 프로그램은 섭씨온도를 화씨온도로 변화하는 프로그램입니다. ")
print("변환하고 싶은 섭씨온도를 입력하세요. ")
data = float(input())
print("섭씨온도 : ", data)
f_data = (data*f[0])+f[1]
print("화씨온도 : ", round(f_data, 2))
