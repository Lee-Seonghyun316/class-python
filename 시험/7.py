num1, num2 = input("공백 기준 두 개의 양수를 입력하시오. ").split()

num1 = int(num1)
num2 = int(num2)


def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True


print("{}와 {}사이의 소수는 ".format(num1, num2), end='')
for i in range(num1+1, num2):
    if(isPrime(i)):
        print("{}".format(i))
