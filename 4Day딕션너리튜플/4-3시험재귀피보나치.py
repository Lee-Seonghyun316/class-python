# 피보나치 수열 계산 프로그램
# 재귀함수 사용
# 음수 입력 시 에러 출력
list1 = []
list2 = []


def fibonacci(n):
    if n <= 1:
        fibonacci_result = n
        return fibonacci_result
    else:
        fibonacci_result = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci_result


data = int(input("몇 번째 피보나지 수열까지 계산할건가요 "))
if data <= 0:
    print("양수 입력 필요")
else:
    for i in range(0, data+1):
        list1.append(i)
        # 데이터까지 0부터 입력
    for i in range(data):
        # print(fibonacci(i))
        list2.append(fibonacci(i))
    result = dict(zip(list1, list2))
    # 두 리스트를 합쳐서 딕션너리로 만드는 함수 zip
    for i in result:
        print(i, "까지의 피보나치 수열은", result.get(i))
    # get사용 딕션너리 객체 다루기
