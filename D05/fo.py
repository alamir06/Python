# loop :is one of a control flow used to iterate on data structure
# names=["alamirew","aklilu","GHN","Temesgen","bimrew","fkqadie"]
# for name in names:
#     print(name)
#     print("name is:",name)
# print(name)
# height_of_students=[]
# for i in range(5):
#     height=float(input("Enter the height of student:"))
#     height_of_students.append(height)
# print("The height of students are:",height_of_students)
# sum_of_height=0
# for height in height_of_students:
#     sum_of_height+=height
# average_height=sum_of_height/len(height_of_students)
# print("The average height of students is:",average_height)

# score_of_students=[]
# for i in range(5):
#     score=float(input("Enter the score of student:"))
#     score_of_students.append(score)
# print("The score of student is:",score_of_students)

# max_score=score_of_students[0]
# for score in score_of_students:
#     if score>max_score:
#         max_score=score
# print("The maximum score of students is:",max_score)

# min_score=score_of_students[0]  
# for score in score_of_students:
#     if score<min_score:
#         min_score=score
# print("The minimum score of students is:",min_score)

names=["alamirew","aklilu","GHN","Temesgen","bimrew","fkqadie"]
for name in names:
    if name=="GHN":
        continue
    print(name)
# for i in range(2,5):
#     print(i)