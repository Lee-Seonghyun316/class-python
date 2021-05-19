# Day9 폴더 안에 있어야 실행 된다!
# 문자열 isalpha매소드 파일입출력 format
f = open("./Day9/1.txt", 'r')
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
