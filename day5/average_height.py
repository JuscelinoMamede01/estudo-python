student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0
number_of_students = len(student_heights)
average_height = 0

for height in student_heights:
    total_height += height

average_height = round(total_height/number_of_students)

print("The total Height of the students:", total_height)
print("Number of students:", number_of_students)
print(f"Average Height of the students {average_height}")
