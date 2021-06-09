# Day8 폴더 안에 있어야 실행 된다!

# 텍스트 파일을 하나 만들고 아래 내용을 저장하시오
# I have a dream that one day down in Alabama with its vicious racists with its governor having his lips dripping with the words of interposition and nullification that one day right down in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers
# 문장안의 콤마나 마침표 같은 문장 부호는 없는 문장으로 입력하시오
# 해당 문장을 단어 단위로 줄바꿈을 하여 새로운 텍스트 파일에 저장하시오.
# 띄어쓰기(빈칸)는 모두 삭제하시오


f = open("./Day8 예외 처리와 파일/1.txt", 'r')
data = f.read()
f.close()

# writedata.py
f = open("./Day8 예외 처리와 파일/1의 결과.txt", 'w')
a = data.split()
for i in range(0, len(a)):
    b = a[i] + '\n'
    f.write(b)
f.close()
