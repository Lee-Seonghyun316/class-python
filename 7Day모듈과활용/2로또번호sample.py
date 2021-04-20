# sample로 로또 번호 뽑는 함수
import random as rd
# random module 활용
initial_list = []


def making_list(a_list):
    for i in range(1, 46):
        a_list.append(i)
    return a_list
# 1에서 45까지 생성해서 리스트에 넣는 함수


making_list(initial_list)
six_list = rd.sample(initial_list, 6)
# 랜덤으로 6개 뽑는 sample매소드
sort_list = sorted(six_list)
# 6개 오름차순 정렬

print(sort_list)
