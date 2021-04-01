A = input("집합 A를 이룰 숫자 5 개를 입력하시요 : ")
a1, a2, a3, a4, a5 = A.split()
setA = {a1, a2, a3, a4, a5}
B = input("집합 A를 이룰 숫자 5 개를 입력하시요 : ")
b1, b2, b3, b4, b5 = A.split()
setB = {b1, b2, b3, b4, b5}
data = int(input("포함여부를 확인할 하나의 값을 입력하시오 : "))

print("집합 A와 B의 합집합은 ", setA.union(setB))
print("집합 A와 B의 교집합은 ", setA.intersection(setB))

none = True
if data in setA:
    print("입력받은 숫자 ", data, "는 집합 A 에 포함되어 있습니다. ")
else:
    none = False

if data in setB:
    print("입력받은 숫자 ", data, "는 집합 B 에 포함되어 있습니다. ")
else:
    if none == False:
        print("입력받은 숫자 ", data, " 는 어느 집합에도 포함되어 있지 않습니다. ")
