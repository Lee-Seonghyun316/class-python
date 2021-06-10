# 파일 포인터는 입출력 동작이 발생하는 위치를 나타낸다.
# 파일을 처음 열었을 때 포인터는 파일의 첫 번째 바이트를 가리키게 되고, 입출력 연산이 실행되면 파일 포인터가 자동적으로 이동한다.

# 예시 :
# f. read()
# 로 파일을 한번 읽은 후

# line = f.read()
# print(line)
# 을 하면 아무것도 출력되지 않는다.

# 그 이유는 앞서 f.read() 를 한번 실행한 뒤, 파일 포인터가 파일의 맨 끝으로 가버렸기 때문이다.
# 파일 포인터의 위치는 f.tell()을 이용해서 확인가능하다.
#  f.seek() 를 이용해 파일 포인터를 가장 앞으로 옮겨준 후, 원래 실행하려고 했던 read()의 반환 값을 변수에 저장하면 file 내용이 출력되는 것을 확인할 수 있다.


f = open("./review for final test/1.txt", 'r')

f. read()
line = f.read()
print(line)

print(f.tell())
f.seek(0)

line = f.read()
print(line)
