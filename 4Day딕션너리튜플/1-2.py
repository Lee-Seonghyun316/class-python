# 수정
students = [
    {"이름 : ": "a", "국어 점수 : ": "49", "수학 점수 : ": "43", "영어 점수 : ": "49", },
    {"이름 : ": "b", "국어 점수 : ": "80", "수학 점수 : ": "60", "영어 점수 : ": "82", },
    {"이름 : ": "c", "국어 점수 : ": "20", "수학 점수 : ": "85", "영어 점수 : ": "48", },
    {"이름 : ": "d", "국어 점수 : ": "100", "수학 점수 : ": "30", "영어 점수 : ": "50", },
    {"이름 : ": "e", "국어 점수 : ": "80", "수학 점수 : ": "90", "영어 점수 : ": "100", }
]

for student in students:
    for i in student:
        print(i, student[i])
    print()

# for key in students:
#     for i in students.get(key):
#         print(i, students.get(key).get(i))
#     print()
