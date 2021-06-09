# 공통사항
# 가능한한 모든 부분에서 람다 함수를 사용하시오
# 키보드로부터 10 개의 값을 입력 받으시오

# 2. 입력 받은 값을 리스트에 저장하고 홀수만 출력하시오
# 람다 함수와 필터 함수를 사용하여 작성하시오


init_list = input('공백 기준 숫자 10개를 입력하시오')
# 예시 : 1 2 3 4 5 6 7 8 9 10

int_list = list(map(lambda x: int(x), init_list.split()))


odd_list = list(filter(lambda x: x % 2 == 1, int_list))
print(odd_list)
