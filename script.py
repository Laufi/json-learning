import json
file = open("students.json")
data = json.load(file)
print(data)

age_sum = 0
grade_sum_U20 = 0
grade_sum_O30 = 0
grade_sum_O20U30 = 0
count_U20 = 0
count_O30 = 0
count_O20U30 = 0
for student in data["Students"]:
    age_sum += int(student["Age"])
    if int(student["Age"]) < 20:
        count_U20 += 1
        grade_sum_U20 += int(student["Grade "])
    elif int(student["Age"]) > 20 and int(student["Age"]) < 30:
        count_O20U30 += 1
        grade_sum_O20U30 += int(student["Grade "])
    else:
        count_O30 += 1
        grade_sum_O30 += int(student["Grade "])
    print(f"{student['FirstName']} {student['LastName']}")
avg_age = age_sum / len(data["Students"])
print(f"The students average age is {avg_age}!")
avg_grade_U20 = grade_sum_U20 / count_U20
avg_grade_O30 = grade_sum_O30 / count_O30
avg_grade_O20U30 = grade_sum_O20U30 / count_O20U30
print(f"Average grade for Under-20 students is {avg_grade_U20}")
print(f"Average grade for Over-30 students is {avg_grade_O30}")
print(f"Average grade for Over-20 and Under-30 students is {avg_grade_O20U30}")
