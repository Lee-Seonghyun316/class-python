import string
# Day8 폴더 안에 있어야 실행 된다!

f = open("./Day8/3.txt", 'r')
data = f.read()
f.close()


# 소문자만 받는 시저 암호
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = chr((ord(s[i]))+3)
        else:
            s[i] = " "

    return "".join(s)


c = solution(data, len(data))


# writedata.py
f = open("./Day8/3의 결과.txt", 'w')

f.write(c)
f.close()
