import csv
from os import write
# f = open('./Day12 csv/시험 성적.csv', "r")

test_data = []
header = []
rownum = 0
with open('./Day12 csv/시험 성적.csv', "r", encoding='UTF-8') as p_file:
    csv_data = csv.reader(p_file)

    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[0]
        if location.find(u"1") != -1:
            test_data.append(row)
        rownum += 1

with open('./Day12 csv/시험 성적2.csv', "w", encoding="utf8") as s_p_file:
    writer = csv.writer(s_p_file, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    writer.writerow(header)
    for row in test_data:
        writer.writerow(row)
