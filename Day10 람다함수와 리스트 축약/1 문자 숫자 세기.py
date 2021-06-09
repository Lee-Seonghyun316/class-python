# Day9 폴더 안에 1.txt 있어야 실행 된다!
# 문자열 isalpha매소드 파일입출력 format

# 1. 임의의 문장(문자 숫자는 다 포함할 것!, 특수문자는 X)을 하나 적힌 파일을 하나 작성하시오.
# 이후 해당 파일의 문장을 읽어 들이고, 해당 문장에서 숫자가 몇 개인지, 문자가 몇 개인지 작성하시오.
# 내장함수 isalpha, isdigit, isalnum 등 을 조사하여 활용하시오

# 화면에 출력


f = open("./Day10 람다함수와 리스트 축약/1.txt", 'r')
data = f.read()
f.close()

alpha = 0
num = 0

for i in range(0, len(data)):
    if data[i].isalnum():
        if data[i].isalpha():
            alpha += 1
        elif data[i].isdigit():
            num += 1
    else:
        print('문자와 숫자 이외에는 카운트 하지 않습니다. ')

print('문장의 숫자는 {}개이고 문자는 {}개 입니다. '.format(num, alpha))
