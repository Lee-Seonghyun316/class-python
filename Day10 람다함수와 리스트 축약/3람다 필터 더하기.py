# 3번

# 공통사항
# 가능한한 모든 부분에서 람다 함수를 사용하시오
# 키보드로부터 10 개의 값을 입력 받으시오
# 3. 입력 받은 값을 리스트에 저장하고 각각의 요소에게 10 을 더하시오
# 람다 함수와 맵 함수를 사용하여 작성하시오

init_list = input('공백 기준 숫자 10개를 입력하시오')
# 예시 : 1 2 3 4 5 6 7 8 9 10

int_list = list(map(lambda x: int(x), init_list.split()))


ten_plus = list(map(lambda x: x + 10, int_list))
print(ten_plus)
