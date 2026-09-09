student_marks =[100, 45, 67, 89, 90, 100, 23, 22, 78, 80, 50, 70, 200, 49, 56, 20, 55, 500]


total_student = len(student_marks)
print("Total student:",total_student)

highest_marks = max(student_marks)
print("Highest Marks:",highest_marks)

lowest_marks = min(student_marks)
print("Lowest Marks:",lowest_marks)

avg_marks = sum(student_marks)/ total_student
print("Average Marks:",avg_marks)

passed_marks = 0
fail_marks = 0
for i in student_marks:
    if i >=40:
        passed_marks +=1
    else:
        fail_marks +=1

print("passed:",passed_marks)
print("Failed:",fail_marks)

pass_per =(passed_marks/total_student) * 100
print("pass perrcentage:",pass_per)

student_marks.sort()
print("sorted Marks(Ascending):",student_marks)

student_marks.sort(reverse=True)
print("sorted marks(Descending):",student_marks)

highest_sorted = sorted(set(student_marks))
second_highest = highest_sorted[-2]
print("second Highest:",second_highest)
second_lowest = highest_sorted[1]
print("second Lowest:",second_lowest)

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_e = 0
grade_f = 0

for i in student_marks:
    if i >= 90:
        grade_a +=1
    elif i >= 80:
        grade_b += 1
    elif i >= 70:
        grade_c += 1
    elif i >= 60:
        grade_d += 1
    elif i >= 40:
        grade_e += 1
    else:
        grade_f += 1

all_passed = grade_f == 0
any_failed = grade_f > 0
print("All students passed?",all_passed)
print("Any student Failed?",any_failed)

user_choice = int(input("Enter mark search for in list :"))
if user_choice in student_marks:
    print("Mark",user_choice,"exit in list")
else:
    print("mark",user_choice,"dosen't exit in list")

print("the grade distribution :")
print("grade A (>=90)", grade_a,"students")
print("grade_b (80-89)", grade_b,"students")
print("grade_c (70-79)", grade_d,"students")
print("grade_d (60-69)", grade_e,"students")
print("grade_e (40-59)", grade_b,"students")
print("grade_f (<40)", grade_c,"students")