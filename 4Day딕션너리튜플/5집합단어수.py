# 단어 수 세는 프로그램
# 중복된 단어 노카운트 = 집합사용

setence = input()

list1 = setence.split()
# 모든 단어 리스트로 만들기

set1 = set(list1)
# 리스트 집합으로 바꾸기
print("사용 단어 : ", set1)

print("단어의 개수 : ", len(set1))
# 길이는 사용 단어의 개수
