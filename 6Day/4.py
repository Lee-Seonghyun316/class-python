def cal(num):
    if num < 0:
        return 'error'
    else:
        return num*(2**(num-1))


data = input()
num = int(data)

sum = 0
for i in range(1, num+1):
    sum += cal(i)

print(sum)
