# 과제 1
# fin = open("data2.txt")
# fout = open("output2.txt", "w")
# lines = fin.readlines()
#
# hap = 0
#
# for line in lines:
#     line = line.rstrip()
#     score = int(line)
#     hap += score
#
# avg = hap / len(lines)
#
# result = "합계 : " + str(hap) + "\n" + "평균 : " + str(avg)
#
# fout.write(result)
#
# fin.close()
# fout.close()


# 과제 2

# f = open("data3.txt", "a")
# for i in range(3):
#     w = input("word: ")
#     f.write(w + " ")
# f.close()
# f = open("data3.txt")
# cnt = 0
# for line in f:
#     line = line.rstrip()
#     word = line.split()
#     for w in word:
#         cnt += 1
#         print(w, end=" ")
# print()
# print("total word : ", cnt)
# f.close()

# 과제 3

# f = open("score1.txt")
# print("이름, 합계, 평균")
# for line in f:
#     name, mid, final = line.split()
#
#     hap = int(mid) + int(final)
#     avg = hap / 2
#     print(name, hap, avg)
# f.close()


# 과제 4

# vote = {"가평":0, "대성리":0, "남이섬":0, "청평":0}
# print(vote)
#
# print("Best MT Spot")
# while True:
#     area = input("area: ")
#     if not area: break
#     vote[area] = vote[area] + 1
#
# print(vote)
# f = open("vote.txt", "w")
#
# for result in vote.keys():
#     f.write(result + " : " + str(vote[result]) + "\n")
#
# f.close()


# 과제 5
# f = open("score2.txt")
#
# data = dict()
# score_dict = dict()
#
# # 파일을 딕셔너리 형태로 저장
# for line in f:
#     line = line.rstrip()
#     word = line.split()
#     data[word[0]] = int(word[1])
#
# for score in data:
#     grade = ""
#     if data[score] >= 90:
#         grade = "A"
#     elif data[score] >= 80:
#         grade = "B"
#     elif data[score] >= 70:
#         grade = "C"
#     elif data[score] >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#
#     score_dict[score] = grade
#     print(score + " 학생의 성적은 " + grade + " 입니다.")
#
# f.close()

# 과제 6

f = open("weather.txt")
weather_data = dict()

for line in f:
    line = line.rstrip()
    word = line.split(",")
    # print(word)
    weather_data[word[0]] = [word[1], word[2]]

# print(weather_data)
for data in weather_data:
    print("{}월의 평균기온은 {}입니다.".format(data, (float(weather_data[data][0]) + float(weather_data[data][1])) / 2))

f.close()