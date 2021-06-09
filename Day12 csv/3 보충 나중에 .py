# 학년별 성씨 별 최고점 이름 출력
# 3. 학년 별로 성씨 별로 가장 성적이 높은 사람의 이름을 출력

# csv 사용하기
import csv

# 파일 읽어오기 , 파일명과 path 변경
f = open('./Day12 csv/시험 성적.csv', 'r')
test = csv.reader(f)

# 맨 처음 학년, 성씨 초기화
# maxvalue = 0
# maxtext = ""
# maxlist = []
# maxname = ""
# first_name = '김'
####

first_name = []
grade = []
for line in test:
    if (line[3] == '성'):
        continue
    print(line[3])
    print(line[0])
    first_name.append(line[3])
    grade.append(line[0])


# first_name = list(test["성"])
# grade = list(test["학년"])

last_grade = 1
last_name = "김"
first_index = 0

# 이중 리스트로 csv 생성할 것임
text = ""
text_list = []

list_kim = []
list_lee = []
list_park = []


def grade_firstName_max(list_first_name, last_grade, first_name):
    kor_first_name_sort = test.iloc[list_first_name, :].sort_values('국어성적')
    kor_max = kor_first_name_sort.iloc[[len(kor_first_name_sort)-1], :].max()
    math_first_name_sort = test.iloc[list_first_name, :].sort_values('수학성적')
    math_max = math_first_name_sort.iloc[[
        len(math_first_name_sort)-1], :].max()
    eng_first_name_sort = test.iloc[list_first_name, :].sort_values('영어성적')
    eng_max = eng_first_name_sort.iloc[[len(eng_first_name_sort)-1], :].max()

    max_value = max(kor_max.iloc[4], math_max.iloc[5], eng_max.iloc[6])

    if max_value == kor_max.iloc[4]:
        name = kor_max.iloc[2]+kor_max.iloc[3]
    if max_value == math_max.iloc[5]:
        name = math_max.iloc[2]+math_max.iloc[3]
    if max_value == eng_max.iloc[6]:
        name = eng_max.iloc[2]+eng_max.iloc[3]
    text = ["{} 학년에서 {}씨에서 점수가 {}으로 가장 높은 사람 : {}".format(
        last_grade, first_name, max_value, name)]
    print(text)
    return text


for i in range(0, len(first_name)):
    now_name = first_name[i]
    now_grade = grade[i]

    if last_grade != now_grade:

        text1 = grade_firstName_max(list_kim, last_grade, "김")
        text_list.append(text1)
        text1 = grade_firstName_max(list_lee, last_grade, "이")
        text_list.append(text1)
        text1 = grade_firstName_max(list_park, last_grade, "박")
        text_list.append(text1)

        last_grade = now_grade

        list_kim = []
        list_lee = []
        list_park = []
        # print(text)

    if now_name == "김":
        list_kim.append(i)
    if now_name == "이":
        list_lee.append(i)
    if now_name == "박":
        list_park.append(i)

text1 = grade_firstName_max(list_kim, last_grade, "김")
text_list.append(text1)
text1 = grade_firstName_max(list_lee, last_grade, "이")
text_list.append(text1)
text1 = grade_firstName_max(list_park, last_grade, "박")
text_list.append(text1)


# 첫번째 행의 이름은 continue로 건너뛰기 : 열의 이름이라서
# 학년이 달라질때 최고점 연산을 통해 최고점을 가진 사람 저장
# 성씨별 리스트를 만들어 성씨별 max값을 출력할 수 있도록 함
# for line in rdr:
#     if (line[1] == '반'):
#         continue
#     # print(line[1])
#     if(grade == line[0]):
#         if(first_name == line[3]):
#             if(maxvalue < float(line[5])):
#                 maxvalue = float(line[5])
#                 maxname = line[3]+line[4]
#             if(maxvalue < float(line[6])):
#                 maxvalue = float(line[6])
#                 maxname = line[3]+line[4]
#             if(maxvalue < float(line[7])):
#                 maxvalue = float(line[7])
#                 maxname = line[3]+line[4]
#         else:
#             maxtext = "{}학년 {}씨 중에서 가장 높은 성적을 받은 이의 이름 : {}".format(
#                 grade, first_name, maxname)
#             maxlist.append([maxtext])
#             first_name = line[3]
#             maxvalue = 0
#             if(maxvalue < float(line[5])):
#                 maxvalue = float(line[5])
#                 maxname = line[3]+line[4]
#             if(maxvalue < float(line[6])):
#                 maxvalue = float(line[6])
#                 maxname = line[3]+line[4]
#             if(maxvalue < float(line[7])):
#                 maxvalue = float(line[7])
#                 maxname = line[3]+line[4]
#     else:
#         maxtext = "{}학년 {}씨 중에서 가장 높은 성적을 받은 이의 이름 : {}".format(
#             grade, first_name, maxname)
#         maxlist.append([maxtext])
#         first_name = line[3]
#         maxvalue = 0
#         grade = line[0]
#         if(maxvalue < float(line[5])):
#             maxvalue = float(line[5])
#             maxname = line[3]+line[4]
#         if(maxvalue < float(line[6])):
#             maxvalue = float(line[6])
#             maxname = line[3]+line[4]
#         if(maxvalue < float(line[7])):
#             maxvalue = float(line[7])
#             maxname = line[3]+line[4]

# maxtext = "{}학년 {}씨 중에서 가장 높은 성적을 받은 이의 이름 : {}".format(
#     grade, first_name, maxname)
# maxlist.append([maxtext])

f.close()

f = open('./Day12 csv/학년성씨별.csv', 'w', newline='')
wr = csv.writer(f)

for line in text_list:
    wr.writerow(line)
f.close()
