number = int(input('약수를 구하고 싶은 숫자 입력:'))

d = []
for i in range(1, int(number**0.5)+1):
    if number % i == 0:
        d.append(i)
        if i != number//i:
            d.append(number//i)
sum_d = sum(d)
print(sum_d)
