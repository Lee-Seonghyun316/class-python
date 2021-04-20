# 집합연산 프로그램
A = input("집합 A를 이룰 숫자 5 개를 입력하시요 : ")
list1 = A.split()
# 리스트(문자열)형태로 집합 입력받기
int_list1 = []
for i in range(0, len(list1)):
    int_list1.append(int(list1[i]))
# 자료형 정수형으로 변환

setA = set(int_list1)
# 집합으로 생성

B = input("집합 B를 이룰 숫자 5 개를 입력하시요 : ")
list2 = B.split()
int_list2 = []
for i in range(0, len(list2)):
    int_list2.append(int(list2[i]))
setB = set(int_list2)

data = int(input("포함여부를 확인할 하나의 값을 입력하시오 : "))
# 정수형으로 데이터 입력받음

sum = setA.union(setB)
# 합집합 연산 매소드

print("집합 A와 B의 합집합은 ", end='')
for i in sum:
    print(i, end=' ')
print('')
# 줄바꿈 없이 쉽표없이 출력하기 위한 부분

together = setA.intersection(setB)
# 교집합 연산 매소드

print("집합 A와 B의 교집합은 ", end='')
for i in together:
    print(i, end=' ')
print('')

none = True
# 둘다 없는지 확인하기 위한 변수

if data in setA:
    # 집합에 있는 요소인지 확인하기 위한 부분
    print("입력받은 숫자 ", data, "는 집합 A 에 포함되어 있습니다. ")
else:
    none = False

if data in setB:
    print("입력받은 숫자 ", data, "는 집합 B 에 포함되어 있습니다. ")
else:
    if none == False:
        print("입력받은 숫자 ", data, " 는 어느 집합에도 포함되어 있지 않습니다. ")
