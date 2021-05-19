# 3번

init_list = input('공백 기준 숫자 10개를 입력하시오')
# 예시 : 1 2 3 4 5 6 7 8 9 10

int_list = list(map(lambda x: int(x), init_list.split()))


ten_plus = list(map(lambda x: x + 10, int_list))
print(ten_plus)
