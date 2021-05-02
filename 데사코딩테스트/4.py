# 4번
n = input()  # 필요없음
numbers = input().split(' ')

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

print(sum(numbers), min(numbers), max(numbers))
