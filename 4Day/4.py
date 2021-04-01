list1 = []
list2 = []

data = int(input("몇 번째 피보나지 수열까지 계산할건가요 "))
if 2 > data or data > 9:
    print("error")

for i in range(0, data+1):
    list1.append(i)

fibo = 0

for i in range(0, len(list1)):
    if i == 0:
        fibo = 0
    elif i == 1:
        fibo = 1
    else:
        fibo = list2[i-1]+list2[i-2]
    list2.append(fibo)

result = dict(zip(list1, list2))

for i in result:
    print(i, "까지의 피보나치 수열은", result.get(i))
