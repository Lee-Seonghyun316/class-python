import string
# Day8 폴더 안에 있어야 실행 된다!

# 시저 암호를 구현하시오

# 평문이 들어있는 파일을 읽고
# 위의 암호표를 참고하여 변환한 후
# 평문 아래에 변환된 내용을 적으시오
# 모두 소문자로만 한정한다
# Ex) i am a boy
# -> o dp d erb

f = open("./Day8 예외 처리와 파일/3.txt", 'r')
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
f = open("./Day8 예외 처리와 파일/3의 결과.txt", 'w')

f.write(c)
f.close()
