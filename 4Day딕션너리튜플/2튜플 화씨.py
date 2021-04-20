# 튜플이용 화씨 변환 프로그램
f = (1.8, 32)
# 튜플이용
print("본 프로그램은 섭씨온도를 화씨온도로 변화하는 프로그램입니다. ")
print("변환하고 싶은 섭씨온도를 입력하세요. ")
data = float(input())
# 실수로 데이터 받음
print("섭씨온도 : ", data)
f_data = (data*f[0])+f[1]
# 튜플 사용 연산
print("화씨온도 : ", round(f_data, 2))
