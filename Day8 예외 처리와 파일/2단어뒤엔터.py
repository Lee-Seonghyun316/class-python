# Day8 폴더 안에 있어야 실행 된다!
# 실습 1 과 내용은 같으나
# 문자 단위로 읽어서 저장하시오


f = open("./Day8 예외 처리와 파일/1.txt", 'r')
data = f.read()
f.close()

# writedata.py
f = open("./Day8 예외 처리와 파일/2의 결과.txt", 'w')
a = data.split()
b = ''
for i in range(0, len(a)):
    b += a[i]
print(b)
print(len(b))
for i in range(0, len(b)):
    c = b[i] + '\n'
    f.write(c)
f.close()
