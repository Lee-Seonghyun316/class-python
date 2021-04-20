# 피보나치 수열 계산 프로그램

list1 = []
list2 = []

data = int(input("몇 번째 피보나지 수열까지 계산할건가요 "))
if 2 > data or data > 9:
    print("error")
# 범위 벗어나면 에러출력

for i in range(0, data+1):
    list1.append(i)
# 데이터까지 0부터 입력

fibo = 0

for i in range(0, len(list1)):
    if i == 0:
        fibo = 0
    elif i == 1:
        fibo = 1
    else:
        fibo = list2[i-1]+list2[i-2]
    list2.append(fibo)
# 피보나치 수열 함수, list1의 길이까지만 계산

result = dict(zip(list1, list2))
# 두 리스트를 합쳐서 딕션너리로 만드는 함수 zip

for i in result:
    print(i, "까지의 피보나치 수열은", result.get(i))
# get사용 딕션너리 객체 다루기
