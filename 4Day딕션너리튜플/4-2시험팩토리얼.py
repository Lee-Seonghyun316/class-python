# 팩토리얼 프로그램
# 예상 : 1. 사용자 함수로 만들어서
# 예상 : 2. 범위 에러 출력하고
# 예상 : 3. 딕션너리 객체로 만들기
# 예상 : 3. 재귀함수 사용


list1 = []
# 인덱스 넣을 리스트
list2 = []
# 계산 결과 넣을 리스트

data = int(input("몇 번째 팩토리얼까지 연산할건가요 "))
if 0 >= data or data > 20:
    print("error")
# 범위 벗어나면 에러출력
# 팩토리얼은 0 이하 계산 불가 기억

for i in range(0, data+1):
    list1.append(i)
# 데이터까지 0부터 입력

# fibo = 0

# for i in range(0, len(list1)):
#     if i == 0:
#         fibo = 0
#     elif i == 1:
#         fibo = 1
#     else:
#         fibo = list2[i-1]+list2[i-2]
#     list2.append(fibo)
# # 피보나치 수열 함수, list1의 길이까지만 계산


def factorial(n):
    if n <= 1:
        factorial_result = 1
        list2.append(factorial_result)
        return factorial_result
    else:
        factorial_result = n * factorial(n-1)
        list2.append(factorial_result)
        return factorial_result


factorial(data)

result = dict(zip(list1, list2))
# 두 리스트를 합쳐서 딕션너리로 만드는 함수 zip

for i in result:
    print(i, "까지의 팩토리얼 계산은", result.get(i))
# get사용 딕션너리 객체 다루기
