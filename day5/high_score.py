student_scores = [78, 65, 10, 86, 1, 91, 92, 89]
highest_score = student_scores[0]

for score in student_scores:
    if score >= highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
