import numpy as np

students = ["Tejas", "Rahul", "Amit", "Sneha", "Priya"]
subjects = ["Maths", "Science", "English"]

marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [95, 92, 88],
    [60, 75, 70],
    [88, 84, 91]
])

total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)
topper_index = np.argmax(total_marks)
lowest_index = np.argmin(total_marks)

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"


def pass_fail(avg):
    if avg >= 40:
        return "Pass"
    else:
        return "Fail"

print("\n========== STUDENT RESULT REPORT ==========\n")

for i in range(len(students)):
    
    print(f"Student Name : {students[i]}")
    print("Marks:")
    for j in range(len(subjects)):
        print(f"{subjects[j]} : {marks[i][j]}")
    
    print(f"Total Marks  : {total_marks[i]}")
    print(f"Average      : {average_marks[i]:.2f}")
    print(f"Grade        : {calculate_grade(average_marks[i])}")
    print(f"Result       : {pass_fail(average_marks[i])}")
    
    print("------------------------------------------")


print("\n========== TOPPER ==========")
print(f"Topper Name  : {students[topper_index]}")
print(f"Highest Marks: {total_marks[topper_index]}")

print("\n========== LOWEST SCORER ==========")
print(f"Student Name : {students[lowest_index]}")
print(f"Marks        : {total_marks[lowest_index]}")

print("\n========== SUBJECT TOPPERS ==========")
for j in range(len(subjects)):
    
    subject_topper_index = np.argmax(marks[:, j])
    
    print(f"{subjects[j]} Topper : {students[subject_topper_index]} "
          f"({marks[subject_topper_index][j]} Marks)")

print("\n========== CLASS STATISTICS ==========")
print(f"Class Average Marks : {np.mean(total_marks):.2f}")
print(f"Highest Total Marks : {np.max(total_marks)}")
print(f"Lowest Total Marks  : {np.min(total_marks)}")

pass_count = 0
for avg in average_marks:
    if avg >= 40:
        pass_count += 1

fail_count = len(students) - pass_count

print(f"Passed Students : {pass_count}")
print(f"Failed Students : {fail_count}")

print("\n========== END OF REPORT ==========")